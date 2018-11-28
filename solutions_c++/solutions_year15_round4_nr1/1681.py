#include <iostream>
#include <algorithm>
#include <cstdio>
#include <string>
#include <cstring>
#include <cmath>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <functional>
#include <sstream>
#include <iomanip>
#include <cmath>
#include <cstdlib>
#include <ctime>
#pragma comment(linker, "/STACK:102400000,102400000")
typedef long long ll;
//typedef pair<int,int> pii; 
#define INF 1e16
#define MAXN 100005
#define MAXM 100
const int maxn = 105;
const int mod = 1000000009;
#define eps 1e-6
#define PI 3.1415926535897932384626433
#define rep(i,n) for(int i=0;i<n;i++)
#define rep1(i,n) for(int i=1;i<=n;i++)
#define scan(n) scanf("%d",&n)
#define scan2(n,m) scanf("%d%d",&n,&m)
#define scans(s) scanf("%s",s);
#define ini(a) memset(a,0,sizeof(a))
#define FILL(a,n) fill(a,a+maxn,n)
#define out(n) printf("%d\n",n)
ll gcd(ll a,ll b) { return b==0?a:gcd(b,a%b);}
#define mk(n,m) make_pair(n,m)
using namespace std;
typedef long long LL;
#define rep(i,n) for(int i = 0;i < n;i ++)
char mp[maxn][maxn];
map<char,int> p;
int dir[] = {-1,0,1,0,0,1,0,-1};
int n,m;
int check(int r,int c)
{
	char ch = mp[r][c];
	int ox = r, oy = c;
	int ans = 0;
	for(int i = 0;i < 4; i++)
	{
		int dx = dir[i*2], dy = dir[i*2+1];
		r = ox, c = oy;
		while(r >= 1 && r <= n && c >= 1 && c <= m)
		{
			r += dx;
			c += dy;
			if(!(r >= 1 && r <= n && c >= 1 && c <= m)) break;
			if(mp[r][c] != '.') 
			{
				if(i == p[ch]) return 1;
				else ans = 2;
			}
		}
	}
	return ans;
}
int solve()
{
	int ans = 0;
	rep1(i,n)
	{
		rep1(j,m)
		{
			if(mp[i][j] == '.') continue;
			int kk = check(i,j);
			if(kk == 0)
			{
				return -1;
			}
			else if(kk == 2) ans++;
		}
	}
	return ans;
}
int main() {
#ifndef ONLINE_JUDGE  
	freopen("in.txt","r",stdin);  
	   freopen("out.txt","w",stdout);  
#endif
	p['^'] = 0; p['v'] = 1; p['>'] = 2; p['<'] = 3;
	int cas = 1;
	int T;
	cin>>T;
	while(T--)
	{
		scanf("%d%d",&n,&m);
		rep1(i,n) rep1(j,m) scanf(" %c",&mp[i][j]);
		int ans = solve();
		printf("Case #%d: ",cas++);
		if(ans == -1) puts("IMPOSSIBLE");
		else out(ans);
	}
	return 0;
}

