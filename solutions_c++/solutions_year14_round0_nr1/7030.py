//
using namespace std;
#include <algorithm>
#include <cmath>
#include <ctime>
#include <cstdio>
#include <cctype>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <bitset>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <list>

typedef long long ll;
typedef unsigned long long ull;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<string> vs;
typedef map<int,int>mii;
typedef map<string,int> msi;

#define MEM(a,b) memset(a, b, sizeof(a))
#define all(x) x.begin(), x.end()
#define len(x) (int)length()
#define sz(x) (int)x.size()
#define pb push_back
#define sqr(x) ((x)*(x))
#define popcount(a) __builtin_popcount(a)
#define gcd(a, b) __gcd(a,b)
#define lcm(a, b) ((a)*((b)/gcd(a,b)))

#define rep(i, n) for(int i=0;i< n;i++)
#define repi(i, m, n) for(int i=m;i<=n;i++)
#define repr(i, m, n) for(int i=m;i>=n;i--)

#define pi acos(-1.0)
#define INF 0x7fffffff

int dx[]={-1,0,1,0,-1,1,1,-1}, dy[]={0,-1,0,1,-1,-1,1,1};
int kx[]={2,1,-1,-2,-2,-1,1,2},ky[]={1,2,2,1,-1,-2,-2,-1};

template< class T > T _pow(T N, T P) { return (P == 0) ? 1 : N * _pow (N, P-1);}
template< class T > T _max(T a, T b) { return (!(a < b) ? a : b); }
template< class T > T _min(T a, T b) { return (a < b ? a : b); }

bool isVowel(char ch){ch = tolower(ch); return ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' || ch == 'u';}
ll bigmod(ll B,ll P,ll M){ll R = 1; while(P > 0) {if(P % 2){R = (R * B) % M;}P /= 2;B = (B * B) % M;}return (int)R;}
ll nCr(double n,double r){double ans=1; if(r > n - r)r = n - r; repi(i, 1, r){ans *= (n - i + 1); ans /= i;} return (ll)ans;}
ll modmul(ll a, ll b, ll m) {return  ((a % m) * (b % m)) % m;}
string toString(int n){stringstream ss; ss << n; return ss.str();}
int toInt(string s){int r = 0;istringstream sin(s);sin >> r; return r;}
//void sieve(int n){MEM(isprime, 1); isprime[1] = 0; for(int i = 2; i * i <= n; i++)for(int j = i * i; j <= n; j += i) isprime[j] = 0;}

int a[4][4], b[4][4];

int main()
{
   freopen("i.txt","r",stdin);
   freopen("o.txt","w",stdout);

   int t;
   cin >> t;

   rep(cs, t) {
       int n, m;
       cin >> n, n--;
       rep(i, 4) rep(j, 4) cin >> a[i][j];
       cin >> m, m--;
       rep(i, 4) rep(j, 4) cin >> b[i][j];
       int cnt = 0, ans;
       rep(i, 4) rep(j, 4) {
           if(a[n][i] == b[m][j]) ans = a[n][i], cnt++;
       }
       cout << "Case #" << cs + 1 <<": ";
       if(cnt == 1) cout << ans << endl;
       else if(!cnt) cout << "Volunteer cheated!" << endl;
       else cout <<  "Bad magician!" << endl;
   }

   return 0;
}

