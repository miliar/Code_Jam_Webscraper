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
#define sff2(x,y) scanf("%lf %lf", &x,&y)
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






int main()
{



    freopen("B-small-attempt4.in","r",stdin);
    freopen("B-small-attempt4.out","w",stdout);
    /**/
    
    int T;
    sf(T);
    for(int t=1; t<=T; t++)
    {
    	int n;
    	double v,x;
    	scanf("%d %lf %lf",&n, &v, &x);
    	double r0,r1,c0,c1,t0,t1;
    	sff2(r0,c0);
    	if(n==1)
    	{
    		if(x!=c0)
    		{
    			printf("Case #%d: IMPOSSIBLE\n",t);
    		}
    		else
    		{
    			printf("Case #%d: %.8lf\n",t,1.0*v/r0);
    		}
    	}
    	else
    	{
    		sff2(r1,c1);
    		if(c0==c1)
    		{
    			if(c0==x)
    			{
    				t0=1.0*v/(r0+r1);
    				printf("Case #%d: %.8lf\n",t,t0);
    			}
    			else
    			{
    				printf("Case #%d: IMPOSSIBLE\n",t);
    			}
    			
    		}
    		else if(c0==x)
    		{
    			t0=1.0*v/r0;
    			printf("Case #%d: %.8lf\n",t,t0);
    		}
    		else if(c1==x)
    		{
    			t1=1.0*v/r1;
    			printf("Case #%d: %.8lf\n",t,t1);
    		}
    		else
    		{
    			t0=1.0*v*(x-c0)/(c1-c0)/r1;
    			t1=(v-r1*t0)/r0;
    			if(t1<0||t0<0)
    			{
    				printf("Case #%d: IMPOSSIBLE\n",t);
	    		}
	    		else
	    		{
	    			printf("Case #%d: %.8lf\n",t,max(t0,t1));
	    		}
    		}
    		
    	}
    	
    }
    
    return 0;
}





