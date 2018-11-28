#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <climits>
#include <cfloat>
#include <map>
#include <utility>
#include <set>
#include <iostream>
#include <memory>
#include <string>
#include <cstring>
#include <vector>
#include <algorithm>
#include <functional>
#include <sstream>
#include <complex>
#include <stack>
#include <queue>
#include <fstream>
using namespace std;
static const double EPS = 1e-9;
typedef long long ll;
typedef long long LL;
typedef pair<int,int>            PI;
typedef map<PI, int> MPI;
typedef vector<int>	VI;
typedef vector<LL>	VLL;
typedef set<int>	SI;
typedef set<LL>	SLL;
typedef vector< vector<int> >	VII;
typedef unsigned int UINT32;
typedef unsigned short UINT16;
typedef unsigned char UINT8;
#define ALL(c) (c).begin(), (c).end()
#define REP(i, n) for (int i = 0; i < (int)(n); i++)
#define PB push_back
#define MP make_pair

//#define DEBUG

//‘½”{’·®”‚±‚±‚©‚ç----------------------------------------------
#include <assert.h>
#include <iomanip>
typedef long long Int;
const Int B = 10000;      // base (power of 10)
const int BW = 4;         // log B
const int MAXDIGIT = 100; // it can represent 4*MAXDIGIT digits (in base 10)
struct BigNum {
  Int digit[MAXDIGIT];
  int size;
  BigNum(int size = 1, Int a = 0) : size(size) {
    memset(digit, 0, sizeof(digit));
    digit[0] = a;
  }
};
const BigNum ZERO(1, 0), ONE(1, 1);

// Comparators
bool operator<(BigNum x, BigNum y) {
  if (x.size != y.size) return x.size < y.size;
  for (int i = x.size-1; i >= 0; --i)
    if (x.digit[i] != y.digit[i]) return x.digit[i] < y.digit[i];
  return false;
}
bool operator >(BigNum x, BigNum y) { return y < x; }
bool operator<=(BigNum x, BigNum y) { return !(y < x); }
bool operator>=(BigNum x, BigNum y) { return !(x < y); }
bool operator!=(BigNum x, BigNum y) { return x < y || y < x; }
bool operator==(BigNum x, BigNum y) { return !(x < y) && !(y < x); }

// Utilities
BigNum normal(BigNum x) {
  Int c = 0;
  for (int i = 0; i < x.size; ++i) {
    while (x.digit[i] < 0)
      x.digit[i+1] -= 1, x.digit[i] += B;
    Int a = x.digit[i] + c;
    x.digit[i] = a % B;
    c          = a / B;
  }
  for (; c > 0; c /= B) x.digit[x.size++] = c % B;
  while (x.size > 1 && x.digit[x.size-1] == 0) --x.size;
  return x;
}
BigNum convert(Int a) {
  return normal(BigNum(1, a));
}
BigNum convert(const string &s) {
  BigNum x;
  int i = s.size() % BW;
  if (i > 0) i -= BW;
  for (; i < (int)s.size(); i += BW) {
    Int a = 0;
    for (int j = 0; j < BW; ++j)
      a = 10 * a + (i + j >= 0 ? s[i+j] - '0' : 0);
    x.digit[x.size++] = a;
  }
  reverse(x.digit, x.digit+x.size);
  return normal(x);
}
// Input/Output
ostream &operator<<(ostream &os, BigNum x) {
  os << x.digit[x.size-1];
  for (int i = x.size-2; i >= 0; --i)
    os << setw(BW) << setfill('0') << x.digit[i];
  return os;
}
istream &operator>>(istream &is, BigNum &x) {
  string s; is >> s;
  x = convert(s);
  return is;
}

// Basic Operations 
BigNum operator+(BigNum x, BigNum y) {
  if (x.size < y.size) x.size = y.size;
  for (int i = 0; i < y.size; ++i)
    x.digit[i] += y.digit[i];
  return normal(x);
}
BigNum operator-(BigNum x, BigNum y) {
  assert(x >= y);
  for (int i = 0; i < y.size; ++i)
    x.digit[i] -= y.digit[i];
  return normal(x);
}
BigNum operator*(BigNum x, BigNum y) {
  BigNum z(x.size + y.size);
  for (int i = 0; i < x.size; ++i)
    for (int j = 0; j < y.size; ++j)
      z.digit[i+j] += x.digit[i] * y.digit[j];
  return normal(z);
}
BigNum operator*(BigNum x, Int a) {
  for (int i = 0; i < x.size; ++i)
    x.digit[i] *= a;
  return normal(x);
}
pair<BigNum, Int> divmod(BigNum x, Int a) {
  Int c = 0, t;
  for (int i = x.size-1; i >= 0; --i) {
    t          = B * c + x.digit[i];
    x.digit[i] = t / a;
    c          = t % a;
  }
  return pair<BigNum, Int>(normal(x), c);
}
BigNum operator/(BigNum x, Int a) {
  return divmod(x, a).first;
}
Int operator%(BigNum x, Int a) {
  return divmod(x, a).second;
}
pair<BigNum, BigNum> divmod(BigNum x, BigNum y) {
  if (x.size < y.size) return pair<BigNum, BigNum>(ZERO, x);
  int F = B / (y.digit[y.size-1] + 1); // multiplying good-factor
  x = x * F; y = y * F;
  BigNum z(x.size - y.size + 1);
  for (int k = z.size-1, i = x.size-1; k >= 0; --k, --i) {
    z.digit[k]  = (i+1 < x.size ? x.digit[i+1] : 0) * B + x.digit[i];
    z.digit[k] /= y.digit[y.size-1];
    BigNum t(k + y.size);
    for (int m = 0; m < y.size; ++m)
      t.digit[k+m] = z.digit[k] * y.digit[m];
    t = normal(t);
    while (x < t) {
      z.digit[k] -= 1;
      for (int m = 0; m < y.size; ++m)
        t.digit[k+m] -= y.digit[m];
      t = normal(t);
    }
    x = x - t;
  }
  return pair<BigNum, BigNum>(normal(z), x / F);
}
BigNum operator/(BigNum x, BigNum y) {
  return divmod(x, y).first;
}
BigNum operator%(BigNum x, BigNum y) {
  return divmod(x, y).second;
}

// Advanced Operations
BigNum shift(BigNum x, int k) {
  if (x.size == 1 && x.digit[0] == 0) return x;
  x.size += k;
  for (int i = x.size - 1; i >= k; --i) x.digit[i] = x.digit[i-k];
  for (int i = k-1; i >= 0; --i) x.digit[i] = 0;
  return x;
}
BigNum sqrt(BigNum x) { // verified UVA 10023
  const BigNum _20 = convert(2*B);
  BigNum odd = ZERO;
  BigNum rem(2,0);
  BigNum ans = ZERO;
  for (int i = 2*((x.size-1)/2); i >= 0; i -= 2) {
    int group = (i+1 < x.size ? x.digit[i+1] : 0) * B + x.digit[i];
    odd =  _20 * ans + ONE;
    rem = shift(rem, 2) + convert(group);
    int count = 0;
    while (rem >= odd) {
      count = count + 1;
      rem = rem - odd;
      odd.digit[0] += 2;
      odd = normal(odd);
    }
    ans = shift(ans,1) + convert(count);
  }
  return ans;
}
BigNum gcd(BigNum x,BigNum y)
{
  if(x<y)
  {
    BigNum tmp;
    tmp = x;
    x = y;
    y = tmp;
  }
  BigNum m = x%y;
  if(m==ZERO)return y;
  return gcd(y,m);
}
//‘½”{’·®”‚±‚±‚Ü‚Å----------------------------------------------



int main(void)
{
  int T,t;
  cin>>T;
  for(t=1;t<=T;t++)
  {
    cout<<"Case #"<<t<<": ";
    int K,C,S;
    cin>>K>>C>>S;
    BigNum val = convert(1);
    BigNum val_K = convert(K);
    BigNum val_K_C1 = convert(1);
    //k^(C-1)‚ðŒvŽZ
    for(int i = 0 ; i < C - 1 ; i++){
      val_K_C1 = val_K_C1 * val_K;
//cout<<val_K_C1<<endl;
    }
    for(int i = 0 ; i < K ; i++){
      cout<<val<<" ";
      val = val + val_K_C1;
    }
    cout<<endl;
  }
  return 0;
}

