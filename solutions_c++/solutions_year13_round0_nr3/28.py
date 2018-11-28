#include <algorithm>
#include <cmath>
#include <iostream>
#include <string>
#include <vector>
using namespace std;

struct SimpleBigInt {
  bool neg;
  string dig;
  SimpleBigInt() : dig("0"), neg(false) {}
  SimpleBigInt(int x)
    {if ((neg=x<0)) x=-x; do {dig.push_back(x%10+'0'); x /= 10;} while (x); reverse(dig.begin(), dig.end());}
  SimpleBigInt(long long x)
    {if ((neg=x<0)) x=-x; do {dig.push_back(x%10+'0'); x /= 10;} while (x); reverse(dig.begin(), dig.end());}
  SimpleBigInt(const string& s) {if ((neg=(s[0]=='-'))) dig = s.substr(1); else dig = s;}
  SimpleBigInt(const string& dig, bool neg) : dig(dig), neg(neg) {}
  static bool LessThan(const string& a, bool an, const string& b, bool bn, bool count_eq) {
    if (an != bn) return an;
    if (a.size() != b.size()) return (a.size() < b.size()) ^ an;
    for (int i = 0; i < a.size(); i++) if (a[i] != b[i]) return (a[i] < b[i]) ^ an;
    return count_eq;
  }
  static SimpleBigInt AddOrSubtract(const string& a, bool an, const string& b, bool bn) {
    SimpleBigInt ret("", an);
    if (an == bn) {
      for (int i = 0, c = 0; i < a.size() || i < b.size() || c; i++) {
        if (i < a.size()) c += a[a.size()-1-i]-'0';
        if (i < b.size()) c += b[b.size()-1-i]-'0';
        ret.dig += c%10 + '0'; c /= 10;
      }
    } else {
      bool swp = LessThan(a, false, b, false, an);
      if (swp) ret.neg = bn;
      const string& s1 = (swp ? b : a), s2 = (swp ? a : b);
      for (int i = 0, c = 0; i < s1.size(); i++) {
        c += 10 + s1[s1.size()-1-i]-'0';
        if (i < s2.size()) c -= s2[s2.size()-1-i]-'0';
        ret.dig += c%10 + '0'; c = c/10-1;
      }
      for (int i = ret.dig.size()-1; i >= 0; i--)
        if (i==0 || ret.dig[i]!='0') {ret.dig = ret.dig.substr(0, i+1); break;}
    }
    reverse(ret.dig.begin(), ret.dig.end());
    return ret;
  }
  SimpleBigInt operator+(const SimpleBigInt& b) const {return AddOrSubtract(dig, neg, b.dig, b.neg);}
  SimpleBigInt& operator+=(const SimpleBigInt& b) {*this = AddOrSubtract(dig, neg, b.dig, b.neg); return *this;}
  SimpleBigInt operator-(const SimpleBigInt& b) const {return AddOrSubtract(dig, neg, b.dig, !b.neg);}
  SimpleBigInt& operator-=(const SimpleBigInt& b) {*this = AddOrSubtract(dig, neg, b.dig, !b.neg); return *this;}
  SimpleBigInt operator-() const {return SimpleBigInt(dig, !(neg || dig=="0"));}
  SimpleBigInt operator*(int x) const {  // NOTE: x*10 should not overflow int.
    if (x == 0) return SimpleBigInt();
    SimpleBigInt ret("", neg);
    if (x < 0) {x = -x; ret.neg = !neg && dig != "0";}
    for (int i = 0, c = 0; i < dig.size() || c; i++) {
      if (i < dig.size()) c += x * (dig[dig.size()-1-i]-'0');
      ret.dig += c%10 + '0'; c /= 10;
    }
    reverse(ret.dig.begin(), ret.dig.end());
    return ret;
  }
  SimpleBigInt& operator*=(int x) {return *this = *this * x;}
  SimpleBigInt operator*(const SimpleBigInt& b) const {
    if (b == 0 || *this == 0) return SimpleBigInt();
    SimpleBigInt ret;
    for (int i = 0; i < b.dig.size(); i++) {
      char ch = b.dig[b.dig.size()-1-i];
      if (ch == '0') continue;
      SimpleBigInt v = *this * (int)(ch-'0');
      for (int j = 0; j < i; j++) v.dig += '0';
      ret += v;
    }
    if (b.neg) ret.neg = !ret.neg;
    return ret;
  }
  SimpleBigInt& operator*=(const SimpleBigInt& b) {return *this = *this * b;}
  SimpleBigInt operator/(SimpleBigInt b) const {
    if (b == 0 || *this == 0) return SimpleBigInt();
    SimpleBigInt ret("", neg ^ b.neg), rem(dig, false);
    b.neg = false;
    int d = 0;
    while (b <= rem) {b.dig += '0'; d++;}
    if (d == 0) return SimpleBigInt();
    ret.dig = string(d, '0');
    for (d--; d >= 0; d--) {
      b.dig.resize(b.dig.size()-1);
      while (b <= rem) {rem -= b; ret.dig[ret.dig.size()-1-d]++;}
    }
    return ret;
  }
  SimpleBigInt& operator/=(const SimpleBigInt& b) {return *this = *this / b;}
  SimpleBigInt operator%(const SimpleBigInt& b) const {return *this - b * (*this / b);}
  SimpleBigInt& operator%=(const SimpleBigInt& b) {return *this -= b * (*this / b);}
  bool operator<(const SimpleBigInt& b) const {return LessThan(dig, neg, b.dig, b.neg, false);}
  bool operator<=(const SimpleBigInt& b) const {return LessThan(dig, neg, b.dig, b.neg, true);}
  bool operator>(const SimpleBigInt& b) const {return !LessThan(dig, neg, b.dig, b.neg, true);}
  bool operator>=(const SimpleBigInt& b) const {return !LessThan(dig, neg, b.dig, b.neg, false);}
  bool operator==(const SimpleBigInt& b) const {return neg == b.neg && dig == b.dig;}
  bool operator!=(const SimpleBigInt& b) const {return neg != b.neg || dig != b.dig;}
  string tostring() const {return (neg ? "-" : "") + dig;}
  friend SimpleBigInt abs(const SimpleBigInt& b) {return SimpleBigInt(b.dig, false);}
  friend istream& operator>>(istream& in, SimpleBigInt& b) {string s; in >> s; b = SimpleBigInt(s); return in;}
  friend ostream& operator<<(ostream& out, const SimpleBigInt& b) {if (b.neg) out << '-'; out << b.dig; return out;}
};

vector<SimpleBigInt> v;

void trynum(string s) {
  SimpleBigInt n(s);
  string t = n.dig;
  reverse(t.begin(), t.end());
  assert(t == n.dig);
  n = n * n;
  t = n.dig;
  reverse(t.begin(), t.end());
  assert(t == n.dig);
  v.push_back(n);
}

main() {
  // Generating the solutions took too long, so hopefully this heuristic
  // pattern-recognition works and there are no weird exceptions. :)
  trynum("1");
  trynum("2");
  trynum("3");
  for (int xnd = 2; xnd <= 50; xnd++) {
    int hnd = xnd/2-1;
    for (int b = 0; b < (1<<hnd); b++) {
      int nb = 0;
      for (int i = 0; i < hnd; i++) if (b&(1<<i)) nb++;
      if (nb > 3) continue;
      string s = "1";
      for (int i = hnd-1; i >= 0; i--) if (b&(1<<i)) s += '1'; else s += '0';
      string t = s;
      reverse(t.begin(), t.end());
      if (xnd%2) {
        for (char mid = '0'; mid <= '1' + (nb <= 1); mid++)
          trynum(s + mid + t);
      } else {
        trynum(s + t);
      }
    }
    trynum('2' + string(xnd-2, '0') + '2');
    if (xnd%2)
      trynum('2' + string((xnd-3)/2, '0') + '1' + string((xnd-3)/2, '0') + '2');
  }
  int T, prob=1;
  SimpleBigInt A, B;
  for (cin >> T; T--;) {
    cin >> A >> B;
    int apos = lower_bound(v.begin(), v.end(), A) - v.begin();
    int bpos = upper_bound(v.begin(), v.end(), B) - v.begin();
    cout << "Case #" << prob++ << ": " << bpos-apos << endl;
  }
}
