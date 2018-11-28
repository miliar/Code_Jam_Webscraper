#include <stdio.h>
#include <iostream>
#include <stdlib.h>
#include <cmath>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <deque>
#include <cstring>
#include <memory.h>
#include <bitset>
#include <time.h>
#define sf(x) scanf("%d", &x)
#define sff(x) scanf("%lf", &x)
#define sfc(x) scanf(" %c", &x)
#define pf(x) printf("%d ", x)
#define pff(x) printf("%lf", x)
#define pfc(x) printf("%c", x)
#define pfs(x) printf("%s", x)
#define sfl(x) scanf("%I64d", &x)
#define sfl2(x,y) scanf("%I64d %I64d", &x,&y)
#define ENDL printf("\n")
#define INF 2147483647
#define pf2(x,y) printf("%d %d ", x,y)
#define sf2(x,y) scanf("%d %d", &x,&y)
#define pb(x) push_back(x)
#define ppb() pop_back()
#define mp(x,y) make_pair(x,y)
#define sf3(x,y,z) scanf("%d %d %d", &x,&y,&z)
#define print(x) puts(#x)
#define error(x) cerr<<#x<<' '<<x<<'\n'


using namespace std;

typedef long long ll; 
typedef unsigned int uint;
typedef unsigned long long ull;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;
typedef pair<double, double> pdd;
typedef vector<int> vec;



int m[31];


bool foo(int v,int base)
{
	if(base>v) return false;
	if(m[v]) return true;
	for(int i=base; i<=v; i++)
	{
		if(m[i])
		if(foo(v-i,i+1))
		return true;
	}
	return false;
}


int main()
{
    
    freopen("C-small-attempt1.in","r",stdin);
    freopen("C-small-attempt1.out","w",stdout);
    
    /**/
    
    int T;
    sf(T);
    for(int t=1; t<=T; t++)
    {
    	int c,d,v;
    	sf3(c,d,v);
    	memset(m,0,sizeof(m));
    	int a;
    	for(int i=0; i<d; i++)
    	{
    		sf(a);
    		m[a]=1;
    	}
    	int res=0;
    	for(int i=1; i<=v; i++)
    	{
    		if(!m[i])
    		{
    			if(!foo(i,1))
    			{
    				m[i]=1;
    				res++;
    			}
    		}
    	}
    	printf("Case #%d: %d\n",t,res);
    }
    return 0;
}








