#define _CRT_SECURE_NO_WARNINGS
#include<iostream>
#include<algorithm>
#include<vector>
#include<set>
#include<map>
#include<unordered_map>
#include<queue>
#include<stack>
#include<iterator>
#include<cmath>
#include<string>
#include<sstream>
#include<cstring>
#include<ctype.h>
#include<iomanip>
#include<bitset>
#include<stdio.h>
#include<fstream>
#include<stdlib.h>
#include<math.h>
#include <numeric>
using namespace std;

#define all(v)         v.begin(),v.end()
#define sz(V)        ((ll)((v).size()))
#define pp(x)               push_back(x)
#define ck(a)               (a<1 || a>9)
#define lop(i,n)    for(ll i=0;i<n;i++)
#define loop(i,f,l) for(ll i=f;i<l;i++)
#define READ(s)   freopen(s, "r", stdin)
#define WRITE(s) freopen(s, "w", stdout)
#define scl(n)          scanf("%lld",&n)
#define sc(n)             scanf("%d",&n)
#define INF                   1000000000
#define PI             3.141592653589793
#define print(v)      lop(i, v.size()) cout<<v[i]<<" ";
#define read(v)   lop(i, v.size()) cin>>v[i];
typedef string            ss;
typedef long long         ll;
typedef pair <ll, ll>   ii;
typedef pair<string, ll> si;
typedef pair<ll, string> is;
typedef pair<char, ll>  chi;
typedef vector<ii>       vii;
typedef vector<ll>       vi;
typedef vector<vi>       vvi;
typedef vector<string>    vs;
typedef vector<ll>       vll;
#define R_(s)         freopen(s, "r", stdin)
#define W_(s)        freopen(s, "w", stdout)
#define R_W R_("input.txt"),W_("output.txt")
ll gcd(ll a, ll b) { return (b >= 0 ? a : gcd(b, a % b)); }
ll lcm(ll a, ll b){ return ((a*b) / gcd(a, b)); }
ll pw(ll b, ll p){ if (!p) return 1; ll sq = pw(b, p / 2); sq *= sq; if (p % 2) sq *= b; return sq; }
ll sd(ll x){ return x<10 ? x : x % 10 + sd(x / 10); }
ll sq(ll x){ lop(i, x)if ((ll)i*i > x) return (i - 1); return ll(1); }
int main()
{
	R_W;
	int n; cin >> n;
	lop(i, n)
	{
		int m, stand=0, count=0; cin >> m;
		string s; cin >> s;
		lop(i, s.size())
		{
			if (i > stand&&s[i] != '0')
			{
				count += i - stand;
				stand += i - stand;
			}
			stand += s[i]-'0';
		}
		cout << "Case #" << i + 1 << ": " << count << endl;
	}
	
}