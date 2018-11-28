#include <algorithm>
#include <assert.h>
#include <bitset>
#include <complex>
#include <ctime>
#include <fstream>
#include <iomanip>
#include <limits.h>
#include <list>
#include <map>
#include <math.h>
#include <queue>
#include <set>
#include <stack>
#include <stdio.h>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <utility>
#include <vector>

using namespace std;

typedef long long LL;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<LL> VLL;
typedef pair<LL, LL> PLL;
typedef pair<int,int> PII;
typedef pair<int, int> PII;
typedef pair<LL, PLL> PLPLL;
typedef pair<PLL, PLL> PPLLPLL;
typedef pair<PLL,LL> PPLLL;
typedef pair<LL, char> PLC;
typedef pair<PLL, char> PPLLC;
typedef pair<char, char> PCC;
typedef pair<LL, VLL> PVLL;
typedef vector<PLL> VPLL;
typedef vector<PII> VPII;
typedef vector<std::string> VS;
typedef std::vector<LL>::iterator VLLitr;

#define arjun int main()
#define FOR(i, x, y) for (LL i = (x); i < (y); ++i)
#define FORC(i, x, y, in) for (LL i = (x); i < (y); i = i + in)
#define RFOR(i, x, y) for (LL i = (x); i >= (y); i--)
#define FORO(it, c)                                                            \
      for (__typeof((c).begin()) it = (c).begin(); it != (c).end(); it++)
#define pb(e) push_back(e)
#define mp make_pair
#define F first
#define S second
#define All(x) x.begin(), x.end()
#define scll(x) scanf("%lld",&x);
#define scll2(x,y) scanf("%lld%lld",&x,&y);
#define sci2(x,y) scanf("%d%d",&x,&y);
#define scll3(x,y,z) scanf("%lld%lld%lld",&x,&y,&z);
#define sci(x) scanf("%d",&x);
#define scc(x) scanf("%c",&x);
#define fast                                                                   \
      ios_base::sync_with_stdio(false);                                            \
  cin.tie(NULL);
#define PI 3.14159265
#define RESET(a, b) memset(a, b, sizeof(a))

template <typename T> T maxm(T a, T b) { return (a > b) ? a : b; }
template <typename T> T minm(T a, T b) { return (a < b) ? a : b; }
template <typename T> T power(T e, T n) {
      T x = 1, p = e;
        while (n) {
                if (n & 1)
                          x = x * p;
                    p = p * p;
                        n >>= 1;
                          }
          return x;
}
template <typename T> T powerm(T e, T n, T m) {
      T x = 1, p = e;
        while (n) {
                if (n & 1)
                          x = (x * p) % m;
                    p = (p * p) % m;
                        n >>= 1;
                          }
          return x;
}
template <typename T> T InverseEuler(T a, T m) {
      return (a == 1 ? 1 : power(a, m - 2, m));
}
template <typename T> T lcm(T a, T b) { return (a * (b / __gcd(a, b))); }

string StringToUpper(string strToConvert) {
      std::transform(strToConvert.begin(), strToConvert.end(), strToConvert.begin(),
                               ::toupper);
        return strToConvert;
}

string StringToLower(string strToConvert) {
      std::transform(strToConvert.begin(), strToConvert.end(), strToConvert.begin(),
                               ::tolower);
        return strToConvert;
}

LL MAX = (LL)(3 * 1e18);
LL MOD = (LL)(1e9 + 7);

#include <fstream>

arjun{
  string s;
  std::ifstream cin("input.txt");
  std::ofstream cout("output.txt");
  LL t,k,count;
  cin>>t;
  bool f = 0;
  FOR(l,1,t+1)
  {
    cin>>s>>k;
    count = 0;
    f = 0;
    for (int i = 0; i < s.length(); ++i)
    {
      if(s[i] == '+') continue;
      for (int j = i; j < i+k; ++j)
      {
        if(i+k-1>=s.length()){
          cout<<"Case #"<<l<<": IMPOSSIBLE"<<endl;
          f = 1;
          break;
        }
        if(s[j] == '-') s[j] = '+';
        else s[j] = '-';
      }
      if(f){
        break;
      }
      count++;
    }
    if(!f)
        cout<<"Case #"<<l<<": "<<count<<endl;

  }
}
