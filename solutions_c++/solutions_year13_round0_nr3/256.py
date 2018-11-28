#include <algorithm>
#include <string>
#include <vector>
#include <cstdio>
#include <cstdlib>
#include <cstring>

#include <cmath>

using namespace std;

#define MAXSIZE 1000
#define DIGIT 4
#define MAX_VALUE 10000

class Bigint {
   public:
   int sign;
   int vn;
   int v[MAXSIZE];

   Bigint() :sign(0), vn(0) { }
   
   Bigint(const int a) :sign(0), vn(0) {
      int carry = 0;

      if (a < 0) {
         sign = -1;
         carry = -a;
      }
      else if (a > 0) {
         sign = 1;
         carry = a;
      }

      for ( ; carry ; vn++) {
         v[vn] = carry%MAX_VALUE;
         carry /= MAX_VALUE;
      }
   }
   
   Bigint(const Bigint &a) :sign(a.sign), vn(a.vn) {
      for (int i = 0 ; i < vn ; i++) {
         v[i] = a.v[i];
      }
   }

   void trim() {
      for ( ; vn > 0 && !v[vn - 1] ; vn--);
      if (vn == 0)
         sign = 0;
   }

   Bigint &operator =(const Bigint &a) {
      if (this == &a) return *this;

      sign = a.sign;
      for (vn = 0 ; vn < a.vn ; vn++)
         v[vn] = a.v[vn];

      return *this;
   }

   void load (const char*str) {
      int len = (int)strlen(str);
      int pre = 0;
      for ( ; str[pre] == ' ' ; pre++);
      if (str[pre] == '-') {
         sign = -1;
         pre++;
      }
      else {
         sign = 1;
      }
      vn = (len - pre - 1)/DIGIT + 1;
      if (vn >= MAXSIZE) {
         fprintf(stderr, "Bigint Overflow!\n");
         exit(1);
      }
      for (int i = 0 ; i < vn ; i++)
         v[i] = 0;
      for (int i = pre ; i < len ; i++) {
         int pos = (len - i - 1)/DIGIT;
         v[pos] = v[pos]*10 + (str[i] - '0');
      }
      trim();
   }

   void print() const {
      if (sign == 0)
         printf("0");
      else {
         if (sign < 0) printf("-");
         printf("%d", v[vn - 1]);
         for (int i = vn - 2 ; i >= 0 ; i--)
            printf("%04d", v[i]);
      }
   }

   void println() const {
      print();
      printf("\n");
   }

   static bool abscmp(const Bigint &a, const Bigint &b) {
      if (a.vn == b.vn) {
         for (int i = a.vn - 1 ; i >= 0 ; i--) {
            if (a.v[i] == b.v[i]) continue;
            return a.v[i] < b.v[i];
         }
         return false;
      }

      return a.vn < b.vn;
   }

   bool operator <(const Bigint &a) const {
      if (sign == a.sign) {
         if (sign < 0)
            return abscmp(a, *this);
         return abscmp(*this, a);
      }

      return sign < a.sign;
   }

   bool operator ==(const Bigint &a) const {
      return !(operator<(a) || a.operator<(*this));
   }

   bool operator <=(const Bigint &a) const {
     return (operator<(a) || operator==(a));
   }

   static Bigint add(const Bigint &a, const Bigint &b) {
      Bigint c;

      c.sign = a.sign;
      int i = 0;
      int carry = 0;
      for ( ; i < b.vn ; i++) {
         int v = a.v[i] + b.v[i] + carry;
         c.v[i] = v%MAX_VALUE;
         carry = v/MAX_VALUE;
      }
      for ( ; i < a.vn ; i++) {
         int v = a.v[i] + carry;
         c.v[i] = v%MAX_VALUE;
         carry = v/MAX_VALUE;
      }
      if (carry) {
         c.v[i++] = carry;
      }
      c.vn = i;

      return c;
   }

   static Bigint sub(const Bigint &a, const Bigint &b) {
      Bigint c;

      c.sign = a.sign;
      int i = 0;
      int carry = 0;
      for ( ; i < b.vn ; i++) {
         int v = a.v[i] - b.v[i] + carry;
         c.v[i] = (v < 0) ? (v + MAX_VALUE) : (v);
         carry = (v < 0) ? -1 : 0;
      }
      for ( ; i < a.vn ; i++) {
         int v = a.v[i] + carry;
         c.v[i] = (v < 0) ? (v + MAX_VALUE) : (v);
         carry = (v < 0) ? -1 : 0;
      }
      c.vn = i;
      c.trim();

      return c;
   }
   
   const Bigint operator +(const Bigint &a) const {
      if (sign*a.sign < 0) {
         if (abscmp(*this, a))
            return sub(a, *this);
         else
            return sub(*this, a);
      }
      else {
         if (abscmp(*this, a))
            return add(a, *this);
         else
            return add(*this, a);
      }   
   }

   const Bigint operator -(const Bigint &a) const {
      if (sign*a.sign < 0) {
         if (abscmp(*this, a))
            return add(a, *this);
         else
            return add(*this, a);
      }
      else {
         if (abscmp(*this, a))
            return sub(a, *this);
         else
            return sub(*this, a);
      }
   }

   static Bigint mul(const Bigint &a, const Bigint &b) {
      Bigint c;
      c.sign = a.sign*b.sign;

      int carry;
      c.vn = a.vn + b.vn;
      if (c.vn >= MAXSIZE) {
         fprintf(stderr, "Bigint overflow!\n");
         exit(1);
      }
      for (int i = 0 ; i < c.vn ; i++)
         c.v[i] = 0;
      for (int i = 0 ; i < a.vn ; i++) {
         if (a.v[i] == 0) continue;
         carry = 0;
         for (int j = 0 ; j < b.vn ; j++) {
            int v = a.v[i]*b.v[j] + carry;
            c.v[i + j] += v%MAX_VALUE;
            carry = v/MAX_VALUE;
         }
         c.v[i + b.vn] += carry;
      }
      carry = 0;
      int i = 0;
      for (int i = 0 ; i < c.vn ; i++) {
         c.v[i] += carry;
         carry = c.v[i]/MAX_VALUE;
         c.v[i] %= MAX_VALUE;
      }
      c.trim();

      return c;
   }

   Bigint operator *(const Bigint &a) const {
      if (sign*a.sign == 0) return Bigint();

      return mul(*this, a);
   }

   static Bigint divint(const Bigint &a, const int b, bool isMod) {
      if (b >= MAX_VALUE) fprintf(stderr, "Invalid call\n");
      Bigint c;
      int b2 = (b > 0) ? b : -b;
      if (b > 0)
         c.sign = a.sign;
      else
         c.sign = -a.sign;

      c.vn = a.vn;
      int r = 0;
      for (int i = a.vn - 1 ; i >= 0 ; i--) {
         r = MAX_VALUE*r + a.v[i];
         c.v[i] = r/b2;
         r %= b2;
      }
      c.trim();
      if (c.sign < 0 && r > 0) {
         c = c - 1;
         r = b2 - r;
      }
      if (isMod)
         return Bigint(r);
      return c;
   }
};

vector<Bigint> vb;
int len;

void backtr(string s, int sum, int m) {
  if (s.size() == len) {
    string r = s;
    reverse(r.begin(), r.end());

    if (m == 1) r = r.substr(1);
    Bigint b;
    b.load((s + r).c_str());
    //= Bigint(s + r);
    vb.push_back(b * b);
    return;
  }
  int last = 1, mv = 2;
  if (s.size() == len - 1 && m == 1) { last = 2; mv = 1; }
  for (int i = 0; i <= last; ++i) {
    int next = sum + mv * i * i;
    if (next < 10) {
      backtr(s + string(1, i + '0'), next, m);
    }
  }
}

int main() {
  vb.push_back(1);
  vb.push_back(4);
  vb.push_back(9);
  vb.push_back(121);
  vb.push_back(484);

  for (len = 2; len <= 25; ++len) {
    // odd len
    for (int s = 1; s <= 2; ++s) {
      backtr(string(1, s + '0'), 2 * s * s, 1);
    }
    // even len
    for (int s = 1; s <= 2; ++s) {
      backtr(string(1, s + '0'), 2 * s * s, 2);
    }
  }

  int T;
  scanf("%d", &T);
  char s[105], t[105];

  for (int cn = 1; cn <= T; ++cn) {
    scanf("%s%s", s, t);
    Bigint b1, b2;
    b1.load(s);
    b2.load(t);
    int ret = 0;
    for (int i = 0; i < vb.size(); ++i) {
      if (b1 <= vb[i] && vb[i] <= b2) ret++;
    }
    printf("Case #%d: %d\n", cn, ret);
  }
}

