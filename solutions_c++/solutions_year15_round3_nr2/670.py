#define _CRT_SECURE_NO_WARNINGS
#include<algorithm>
#include<stdlib.h>
#include<iterator>
#include<iostream>
#include<numeric>
#include<sstream>
#include<cstring>
#include<ctype.h>
#include<iomanip>
#include<stdio.h>
#include<fstream>
#include<vector>
#include<bitset>
#include<string>
#include<math.h>
#include<queue>
#include<stack>
#include<cmath>
#include<set>
#include<map>

using namespace std;

#define all(v)             v.begin(),v.end()
#define sz(v)            ((int)((v).size()))
#define psh(x)                  push_back(x)
#define sc(x)                 scanf("%d",&x)
#define sc2(x,y)         scanf("%d%d",&x,&y)
#define scl(x)              scanf("%lld",&x)
#define lop(i,n)        for(int i=0;i<n;++i)
#define loop(i,f,l)     for(int i=f;i<l;++i)
#define R_(s)         freopen(s, "r", stdin)
#define W_(s)        freopen(s, "w", stdout)
#define R_W R_("input.txt"),W_("output.txt")
#define PI           acos(-1)
#define INF             1<<30
#define DFS_GRAY           -1
#define DFS_WHITE           0
#define DFS_BLACK           1

typedef string            ss;
typedef long long         ll;
typedef pair <int, int>   ii;
typedef pair<ss, int>     si;
typedef pair<int, ss>     is;
typedef pair<char, int>  chi;
typedef pair<ss, ss>     pss;
typedef vector<ii>       vii;
typedef vector<int>       vi;
typedef vector<vi>       vvi;
typedef vector<ss>        vs;
typedef vector<ll>       vll;
typedef vector<vll>     vvll;

ll pw(ll b, ll p){ if (!p) return 1; ll sq = pw(b, p / 2); sq *= sq; if (p % 2) sq *= b; return sq; }
ll gcd(ll a, ll b)  { return (b == 0 ? a : gcd(b, a % b)); }
ll sd(ll x)  { return x<10 ? x : x % 10 + sd(x / 10); }
ll lcm(ll a, ll b){ return ((a*b) / gcd(a, b)); }

int t, k, l, s,cnt,temp,tot,mx;
ss keys, target,x;
void rec()
{
	
	if (x.length() == s)
	{
		temp = 0;
		lop(i, s)
		{
			if (x.substr(i, l) == target)++cnt,++temp;
		}
		mx = max(mx, temp);
		return;
	}
	lop(i, k)
	{
		x += keys[i];
		rec();
		x.pop_back();
	}
}
int main()
{
	//R_W;
	cin >> t;
	lop(i, t)
	{
		cin >> k >> l >> s>>keys>>target;
		cnt =0;
		mx = 0;
		tot = pw(k,s);
		rec();
		printf("Case #%d: ", i + 1);
		cout <<fixed<<setprecision(12)<<mx-double(cnt)/tot<<endl;
	}
}