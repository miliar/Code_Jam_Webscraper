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
    	memset(t, 0, sizeof(t));
    	scanf("%d%d", &n, &m);
    	rep(i,1,n)
    		scanf("%s", &s[i][1]);
    	rep(i,1,n)
    	{
    		int j = 1;
    		while (s[i][j] == '.') j++;
    		t[i][j] += 1;
    		j = m;
    		while (s[i][j] == '.') j--;
    		t[i][j] += 2;
    	}
    	rep(j,1,m)
    	{
    		int i = 1;
    		while (s[i][j] == '.') i++;
    		t[i][j] += 4;
    		i = n;
    		while (s[i][j] =='.') i--;
    		t[i][j] += 8;
    	}
    	be['<'] = 1;
    	be['>'] = 2;
    	be['^'] = 4;
    	be['v'] = 8;
    	
    	int ans = 0;
    	rep(i,1,n)
    		rep(j,1,m)
    			if (t[i][j] == 15)
    			{
    				printf("IMPOSSIBLE\n");
    				return;
    			}
    			else 
				{
					int k = be[s[i][j]];
					if (t[i][j] & k) ans++;
				}
    	printf("%d\n", ans);
    }
    void work()
    {
    	
    }
}Program;
int main()
{
	freopen("A.in", "r", stdin);
	freopen("A.out", "w", stdout);
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
