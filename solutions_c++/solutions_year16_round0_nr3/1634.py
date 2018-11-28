#include <cstdio>
#include <cmath>
#include <cstring>
#include <cstdlib>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <queue>
#include <algorithm>
#include <limits>
#include <iostream>
#include <utility>

using namespace std;

#define TRACE(x...) x
#define WATCH(x) TRACE(cout << #x" = " << x << endl)
#define PRINT(x...) TRACE(printf(x); fflush(stdout))

#define gc getchar  //unlocked linux
#define all(v) (v).begin(), (v).end()
#define FU(i, a, b) for(decltype(b) i = (a); i < (b); ++i)
#define fu(i, n) FU(i, 0, n)
#define FD(i, a, b) for (decltype(b) i = (b)-1; i >= a; --i)
#define fd(i, n) FD(i, 0, n)
#define mod(a, b) ((((a)%(b))+(b))%(b))
#define pb push_back
#define sz(c) int((c).size())
#define mk make_pair

const int INF = 0x3F3F3F3F; const int NEGINF = 0xC0C0C0C0;

const double EPS = 1e-8;

typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<double> vd;
typedef long long ll;
typedef vector<ll> vll;
typedef vector<vll> vvll;

int cmp_double(double a, double b, double eps = 1e-9){
  return a + eps > b ? b + eps > a ? 0 : 1 : -1;  //0 = iguais, 1 = a maior
}

inline void scanint(int &x){
  register int c = gc();
  x = 0;
  int neg = 0;
  for(;((c<48 || c>57) && c != '-');c = gc());
  if(c=='-') {neg=1;c=gc();}
  for(;c>47 && c<58;c = gc()) {x = (x<<1) + (x<<3) + c - 48;}
  if(neg) x=-x;
}

#include <limits>

const int MAXD = 1005, DIG = 9, BASE = 1000000000;
const unsigned long long BOUND = numeric_limits <unsigned long long> :: max () - (unsigned long long) BASE * BASE;

struct bignum
{
    int D, digits [MAXD / DIG + 2];

    inline void trim ()
    {
        while (D > 1 && digits [D - 1] == 0)
            D--;
    }

    inline void init (long long x)
    {
        memset (digits, 0, sizeof (digits));
        D = 0;

        do
        {
            digits [D++] = x % BASE;
            x /= BASE;
        }
        while (x > 0);
    }

    inline bignum (long long x)
    {
        init (x);
    }

    inline bignum (int x = 0)
    {
        init (x);
    }

    inline bignum (char *s)
    {
        memset (digits, 0, sizeof (digits));
        int len = strlen (s), first = (len + DIG - 1) % DIG + 1;
        D = (len + DIG - 1) / DIG;

        for (int i = 0; i < first; i++)
            digits [D - 1] = digits [D - 1] * 10 + s [i] - '0';

        for (int i = first, d = D - 2; i < len; i += DIG, d--)
            for (int j = i; j < i + DIG; j++)
                digits [d] = digits [d] * 10 + s [j] - '0';

        trim ();
    }

    inline char *str ()
    {
        trim ();
        char *buf = new char [DIG * D + 1];
        int pos = 0, d = digits [D - 1];

        do
        {
            buf [pos++] = d % 10 + '0';
            d /= 10;
        }
        while (d > 0);

        reverse (buf, buf + pos);

        for (int i = D - 2; i >= 0; i--, pos += DIG)
            for (int j = DIG - 1, t = digits [i]; j >= 0; j--)
            {
                buf [pos + j] = t % 10 + '0';
                t /= 10;
            }

        buf [pos] = '\0';
        return buf;
    }

    inline bool operator < (const bignum &o) const
    {
        if (D != o.D)
            return D < o.D;

        for (int i = D - 1; i >= 0; i--)
            if (digits [i] != o.digits [i])
                return digits [i] < o.digits [i];

        return false;
    }

    inline bool operator == (const bignum &o) const
    {
        if (D != o.D)
            return false;

        for (int i = 0; i < D; i++)
            if (digits [i] != o.digits [i])
                return false;

        return true;
    }

    inline bignum operator << (int p) const
    {
        bignum temp;
        temp.D = D + p;

        for (int i = 0; i < D; i++)
            temp.digits [i + p] = digits [i];

        for (int i = 0; i < p; i++)
            temp.digits [i] = 0;

        return temp;
    }

    inline bignum operator >> (int p) const
    {
        bignum temp;
        temp.D = D - p;

        for (int i = 0; i < D - p; i++)
            temp.digits [i] = digits [i + p];

        for (int i = D - p; i < D; i++)
            temp.digits [i] = 0;

        return temp;
    }

    inline bignum range (int a, int b) const
    {
        bignum temp = 0;
        temp.D = b - a;

        for (int i = 0; i < temp.D; i++)
            temp.digits [i] = digits [i + a];

        return temp;
    }

    inline bignum operator + (const bignum &o) const
    {
        bignum sum = o;
        int carry = 0;

        for (sum.D = 0; sum.D < D || carry > 0; sum.D++)
        {
            sum.digits [sum.D] += (sum.D < D ? digits [sum.D] : 0) + carry;

            if (sum.digits [sum.D] >= BASE)
            {
                sum.digits [sum.D] -= BASE;
                carry = 1;
            }
            else
                carry = 0;
        }

        sum.D = max (sum.D, o.D);
        sum.trim ();
        return sum;
    }

    inline bignum operator - (const bignum &o) const
    {
        bignum diff = *this;

        for (int i = 0, carry = 0; i < o.D || carry > 0; i++)
        {
            diff.digits [i] -= (i < o.D ? o.digits [i] : 0) + carry;

            if (diff.digits [i] < 0)
            {
                diff.digits [i] += BASE;
                carry = 1;
            }
            else
                carry = 0;
        }

        diff.trim ();
        return diff;
    }

    inline bignum operator * (const bignum &o) const
    {
        bignum prod = 0;
        unsigned long long sum = 0, carry = 0;

        for (prod.D = 0; prod.D < D + o.D - 1 || carry > 0; prod.D++)
        {
            sum = carry % BASE;
            carry /= BASE;

            for (int j = max (prod.D - o.D + 1, 0); j <= min (D - 1, prod.D); j++)
            {
                sum += (unsigned long long) digits [j] * o.digits [prod.D - j];

                if (sum >= BOUND)
                {
                    carry += sum / BASE;
                    sum %= BASE;
                }
            }

            carry += sum / BASE;
            prod.digits [prod.D] = sum % BASE;
        }

        prod.trim ();
        return prod;
    }

    inline double double_div (const bignum &o) const
    {
        double val = 0, oval = 0;
        int num = 0, onum = 0;

        for (int i = D - 1; i >= max (D - 3, 0); i--, num++)
            val = val * BASE + digits [i];

        for (int i = o.D - 1; i >= max (o.D - 3, 0); i--, onum++)
            oval = oval * BASE + o.digits [i];

        return val / oval * (D - num > o.D - onum ? BASE : 1);
    }

    inline pair <bignum, bignum> divmod (const bignum &o) const
    {
        bignum quot = 0, rem = *this, temp;

        for (int i = D - o.D; i >= 0; i--)
        {
            temp = rem.range (i, rem.D);
            int div = (int) temp.double_div (o);
            bignum mult = o * div;

            while (div > 0 && temp < mult)
            {
                mult = mult - o;
                div--;
            }

            while (div + 1 < BASE && !(temp < mult + o))
            {
                mult = mult + o;
                div++;
            }

            rem = rem - (o * div << i);

            if (div > 0)
            {
                quot.digits [i] = div;
                quot.D = max (quot.D, i + 1);
            }
        }

        quot.trim ();
        rem.trim ();
        return make_pair (quot, rem);
    }

    inline bignum operator / (const bignum &o) const
    {
        return divmod (o).first;
    }

    inline bignum operator % (const bignum &o) const
    {
        return divmod (o).second;
    }

    inline bignum power (int exp) const
    {
        bignum p = 1, temp = *this;

        while (exp > 0)
        {
            if (exp & 1) p = p * temp;
            if (exp > 1) temp = temp * temp;
            exp >>= 1;
        }

        return p;
    }
};

inline bignum gcd (bignum a, bignum b)
{
    bignum t;

    while (!(b == 0))
    {
        t = a % b;
        a = b;
        b = t;
    }

    return a;
}

string to_binary(int x, int T){
  string ans = "1";
  while(x != 0){
    if (x%2 == 0) ans += '0';
    else ans += '1';
    x = x/2;
    T--;
  }
  while(T--) ans += '0';
  ans += "1";
  return ans;
}

bignum mypow(ll b, ll e){
  bignum bx(b);
  //cout <<  b << " " << e << endl;
  if (e == 0) return bignum(1);
  if (e == 1) return bx;
  e--;
  bignum ans = bx;
  while(e--) ans = ans * bx;
 // cout << ans.str() << endl;
  return ans;
}

bignum base_str(string s, int bx){
  bignum ans (0);
  bignum b ((ll)bx);
 // cout << b.str() << endl;
  for (int i = 0; i < s.size(); i++){
    if (s[i] == '1') ans = ans + mypow((ll)bx, (ll)i);
  }
  return ans;
}

bignum getDiv(bignum n){
  for (ll i = 2; i < 100; i++){
    if (bignum(i) == n) return bignum(0);
    if ( (n%bignum(i)) == bignum(0)) return bignum(i);
  }
  return bignum(0);
}


int main(){
  int cases = 1;
  int ax;
  cin >> ax;
  printf("Case #%d: \n", cases++);
  int T, J;
  cin >> T;
  T-=2;
  cin >> J;
  int M = 1 << T;
  int cnt = 0;
  for (int i = 0; i < M; i++){
    string bin = to_binary(i, T);
   //printf("%d %s\n", i, bin.c_str());

    bool ok = true;
    vector<bignum> div;
    for (int b = 2; b <= 10; b++){
      bignum num = base_str(bin, b);
     // printf("Na base %d, num %s\n", b, num.str());
      bignum d = getDiv(num);
     // cout << d.str() << endl;
      if (d == bignum(0)) ok = false;
      if (!ok) break;
      div.pb(d);
    }
    if (!ok) continue;

    reverse(bin.begin(), bin.end());
    cout << bin;
    for (bignum &x : div) cout << " " << x.str();
    cout << endl;

    cnt++;
    //cout << cnt << endl;
    if (cnt == J) break;
  }
  return 0;
}
