// Template by Akigeor
#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
#include <algorithm>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cmath>
#define ff first
#define ss second
#define pb push_back
#define PII pair<int,int>
#define rep(i,n) for (i=0;i<(n);i++)
#define fo(i,L,R) for (i=(L);i<=(R);i++)
#define cls(x) memset(x,0,sizeof(x))
#define cin(x) scanf("%d",&x)
#define mINF 0x3f
#define INF 0x3f3f3f3f
#define MOD7 1000000007
#define MOD9 1000000009
#define PI acos(-1.0)
using namespace std;
int f[105][105],h,w,ans=0;
bool v[105][105];
char m[105][105];
PII test(int x,int y,char d)
{
	if (d=='^')
	{
		while (--x>=0) if (m[x][y]!='.') return PII(x,y);
	}
	else if (d=='v')
	{
		while (++x<h) if (m[x][y]!='.') return PII(x,y);
	}
	else if (d=='<')
	{
		while (--y>=0) if (m[x][y]!='.') return PII(x,y);
	}
	else
	{
		while (++y<w) if (m[x][y]!='.') return PII(x,y);
	}
	return PII(-1,-1);
}
bool emp(int x,int y)
{
	int i;
	rep(i,h) if (i!=x && m[i][y]!='.') return 0;
	rep(i,w) if (i!=y && m[x][i]!='.') return 0;
	return 1;
}
void dfs(int x,int y)
{
	if (v[x][y]) return;
	v[x][y]=1;
	PII p=test(x,y,m[x][y]);
	if (p.ff!=-1) dfs(p.ff,p.ss); else ans++;
}
int main()
{
	int t,z;
	cin(t);
	fo(z,1,t)
	{
		int i,j,k,l;
		ans=0;
		cin(h); cin(w);
		rep(i,h) scanf("%s",m[i]);
		cls(v);
		bool no=0;
		rep(i,h) rep(j,w)
		{
			if (m[i][j]!='.' && !v[i][j])
			{
				if (emp(i,j)) {no=1; goto eee;}
				PII p;
				p=test(i,j,m[i][j]);
				if (p.ff!=-1) {dfs(p.ff,p.ss); continue;}
				ans++;
				v[i][j]=1;
				p=test(i,j,'^');
				if (p.ff!=-1) {dfs(p.ff,p.ss); continue;}
				p=test(i,j,'v');
				if (p.ff!=-1) {dfs(p.ff,p.ss); continue;}
				p=test(i,j,'<');
				if (p.ff!=-1) {dfs(p.ff,p.ss); continue;}
				p=test(i,j,'>');
				if (p.ff!=-1) {dfs(p.ff,p.ss); continue;}
			}
		}
eee:
		if (no)
		{
			printf("Case #%d: IMPOSSIBLE\n",z);
		}
		else
		{
			printf("Case #%d: %d\n",z,ans);
		}
	}
}
