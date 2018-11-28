#include <set>
#include <cmath>
#include <stack>
#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <cstdlib>
#include <numeric>
#include <vector>
#include <ctime>
#include <queue>
#include <list>
#include <map>
#define pi acos(-1.0)
#define INF 0x3f3f3f3f
#define clr(x)  memset(x,0,sizeof(x));
#define clrto(x,siz,y)  for(int xx=0;xx<=siz;xx++)  x[xx]=y;
#define clrset(x,siz)  for(int xx=0;xx<=siz;xx++)  x[xx]=xx;
#define clr_1(x) memset(x,-1,sizeof(x));
#define clrmax(x) memset(x,0x3f,sizeof(x));
#define clrvec(x,siz) for(int xx=0;xx<=siz;xx++)  x[xx].clear();
#define fop2   freopen(".in","r",stdin); //freopen(".out","w",stdout);
#define fop   freopen("in.txt","r",stdin);//freopen("out.txt","w",stdout);
#define getfile char fin[11], fout[11]; sprintf(fin, "%d.in", i); sprintf(fout, "%d.out", i); freopen(fin, "r", stdin); freopen(fout, "w", stdout);
#define makefile char fout[11]; sprintf(fout, "%d.in", i); freopen(fout, "w", stdout);
#define myprogram By_135678942570
#define clrcpy(x,siz,y)  for(int xx=0;xx<siz;xx++)  x[xx]=y[xx];
#define pb push_back
using namespace std;
int n, r, p, s;
int check(string sp)
{
	int rr = 0, pp = 0, ss = 0;
	for(int i = 0; i < 1 << n; i++)
		if(sp[i] == 'R')
			rr++;
		else if(sp[i] == 'P')
			pp++;
		else ss++;
	return rr == r && pp == p && ss == s;
}
string dfs(char now, int depth)
{
	if(depth == 0)
	{
		string sp = "";
		return sp + now;
	}
	string s1 = "", s2 = "";
	if(now == 'S')
		s1 = dfs('P', depth - 1), s2 = dfs('S', depth - 1);
	else if(now == 'P')
		s1 = dfs('P', depth - 1), s2 = dfs('R', depth - 1);
	else s1 = dfs('R', depth - 1), s2 = dfs('S', depth - 1);
	return min(s1 + s2, s2 + s1);
}
int main()
{
	int T, cas = 0;
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	scanf("%d", &T);
	while(T--)
	{
		scanf("%d%d%d%d", &n, &r, &p, &s);
		printf("Case #%d: ", ++cas);
		string res = dfs('P', n);
		if(check(res))
		{
			cout<<res<<endl;
			continue;
		}
		res = dfs('R', n);
		if(check(res))
		{
			cout<<res<<endl;
			continue;
		}
		res = dfs('S', n);
		if(check(res))
		{
			cout<<res<<endl;
			continue;
		}
		puts("IMPOSSIBLE");
	}
}