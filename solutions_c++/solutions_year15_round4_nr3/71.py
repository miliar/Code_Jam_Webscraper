/*.....................
Author : PTY
Time : 15/05/01
Desprition :
Analyse : 
Attention : 
.....................*/
#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <set>
#include <queue>
#include <stack>
#include <fstream>
#include <numeric>
#include <iomanip>
#include <bitset>
#include <list>
#include <stdexcept>
#include <functional>
#include <utility>
#include <ctime>
#include <map>
using namespace std;
#define rep(i,l,r) for(int i=l;i<=r;i++)
#define drep(i,r,l) for(int i=r;i>=l;i--)
#define max(a,b) (a>b?a:b)
#define min(a,b) (a<b?a:b)
#define LL long long
#define Travel(E, u) for(int i=E.start[u],v;v=E.e[i].a,i;i=E.e[i].next)
#define sqr(x) ((x)*(x))
#define pb push_back
#define read() (strtol(ipos, &ipos, 10))
#define pb push_back
#define pi 3.1415926535897


char s[208][208];
int t[208][208];
int n, m;
int be[1008];

struct Tprogram
{
    void open()
    {
        freopen("", "r", stdin);
        freopen("", "w", stdout);
    }
    void close()
    {
        fclose(stdin);
        fclose(stdout);
    }
    void init()
    {
    	scanf("%d", &n);
    	rep(i,1,n)
    	{
    		while (1)
    		{
    			string S = "";
    			while (1)
    			{
    				scanf("%c", &c);
    				if (c == ' ') break;
    				if (c == '\n') goto die;
    				S.pb(c);
    			}
    			F[i].pb(S);
    		}
    		die:;
    	}
    	foreach(t, F[1])
    	{
    		G[0][*t]++;
    	}
    	foreach(t, F[2])
    	{
    		G[1][*t]++;
    	}
    }
    void dfs(int d)
    {
    	if (d>n)
    	{
    		ans++;
    		return;
    	}
    	foreach(t, F[d])
    	{
    		G[0][*t]++;
    	}
    	dfs(d+1);
    	foreach(t, F[d])
    	{
    		G[0][*t]--;
    		G[1][*t]++;
    	}
    	dfs(d+1);
    }
    void work()
    {
    	dfs(3);
    	printf("%d\n", ans); 
    }
}Program;
int main()
{
	int T;
	scanf("%d", &T);
	rep(i,1,T)
	{
    //Program.open();
    	printf("Case #%d: ", i);
    	Program.init();
    }
    //Program.close();
    return 0;
}
