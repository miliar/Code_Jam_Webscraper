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


int n, D;
const int maxn = 2000008;
int S[maxn], M[maxn];
struct arr
{
	int u, v;
	arr(){}
	arr(int u1, int v1){
		u = u1; v = v1;
	}
	bool operator<(const arr &t)const
	{
		return v > t.v;
	}
}tmp[maxn];
vector<int> e[maxn];
priority_queue<arr> Q;
int h[maxn];
int in[maxn];
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
    	int As, Cs, Rs, Am, Cm, Rm;
    	scanf("%d%d", &n,&D);
    	scanf("%d%d%d%d", &S[0], &As, &Cs, &Rs);
    	scanf("%d%d%d%d", &M[0], &Am, &Cm, &Rm);
    	rep(i,1,n-1)
    	{
    		S[i] = ((LL)S[i-1] * As +Cs) % Rs;
    		M[i] = ((LL)M[i-1] * Am + Cm) % Rm;
    	}
    	rep(i,0,n) e[i].clear();
    	M[0] = 0;
    	rep(i,1,n-1)
    	{
    		M[i] = M[i] % i;
    		e[M[i]].pb(i);
    	}
    	rep(i,0,n-1)
    		tmp[i] = arr(i, S[i]);
    	sort(tmp, tmp+n);
    	rep(i,0,n/2-1)
    		swap(tmp[i], tmp[n-i-1]);
    }
    void work()
    {
    	while (!Q.empty()) Q.pop();
    	memset(in, 0, n+1<<2);
    	int pos = 0;
    	while (tmp[pos].v + D < S[0]) pos++;
    	
    	int small = tmp[pos].v;
		int l = 1, r = 0; 
		h[++r] = 0; in[0] = 1;
    	int cnt = 1, ans = 1;
		while (l <= r)
		{
			int u = h[l++];
			for (int i = 0; i < e[u].size(); i++)
			{
				int u1 = e[u][i];
				if (S[u1] - small <= D && S[u1] >= small)
				{
					h[++r] = u1;
					in[u1] = 1;
					cnt++;
				}
				else if (S[u1] - small > D)
					Q.push(arr(u1, S[u1]));
			}
		}
		ans = cnt;
		int j = pos;
		for (pos++; pos < n && tmp[pos].v <= S[0]; pos++)
    	{
    		small = tmp[pos].v;
    		int l = 1, r = 0;
    		while (1)
    		{
    			while (!Q.empty() && in[M[Q.top().u]] == 0) Q.pop();
    			if (Q.empty()) break;
    			if (Q.top().v > small + D) break;
    			int u = Q.top().u;
    			Q.pop();
    			h[++r] = u;
			}
    		while (l <= r)
    		{
    			int u = h[l++]; cnt++; in[u] = 1;
    			for (int i = 0; i < e[u].size(); i++)
    			{
    				int u1 = e[u][i];
    				if (S[u1] - small <= D && S[u1] >= small)
    				{
    					h[++r] = u1;
    				}
    				else if (S[u1] - small > D)
						Q.push(arr(u1, S[u1]));
    			}
    		}
    		while (tmp[j].v < small)
    		{
    			int u = tmp[j++].u;
	    		if (in[u])
	    		{
	    			cnt--; 
	    			int l = 1, r = 1; h[1] = u;
	    			while (l <= r)
	    			{
	    				int u = h[l++]; in[u] = 0;
	      				for (int i = 0; i < e[u].size(); i++)
	    				{
	    					int u1 = e[u][i];
	    					if (in[u1])
	    					{
	    						cnt--; h[++r] = u1;
	    					}
	    				}
	    			}
	    		}
	    	}
    		ans = max(ans, cnt);
    	}
    	printf("%d\n", ans);
    }
}Program;
int main()
{
	freopen("A.in","r", stdin);
	freopen("A.out", "w", stdout);
	int T;
	scanf("%d", &T);
	rep(i,1,T)
	{
    //Program.open();
    	printf("Case #%d: ", i);
    	Program.init();
    	Program.work();
    }
    //Program.close();
    return 0;
}
