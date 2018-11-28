#include<bits/stdc++.h>
#include<cstdlib>   
#define sf(x) scanf("%d",&x)
#define pf(x) printf("%d ",x)
#define sf2(x,y) scanf("%d %d",&x,&y)
#define pf2(x,y) printf("%d %d ",x,y)
#define sf3(x,y,z) scanf("%d %d %d",&x,&y,&z)
#define pf3(x,y,z) printf("%d %d %d ",x,y,z)
#define sfc(c) scanf(" %c",&c)
#define pfc(c) printf("%c",c)
#define pb(x) push_back(x)
#define mp(x,y) make_pair(x,y)
#define INF 2000000000
#define ENDL puts("")


using namespace std;

typedef long long ll;
typedef pair<int,int> pii;
typedef pair<ll,ll> pll;
typedef unsigned int uint;
typedef long double ld;

    

bool u[11];

bool check(ll n)
{
	ll tmp=n;
	while(tmp)
	{
		u[tmp%10]=1;
		tmp/=10;
	}
	for(int i=0; i<10; i++)
	{
		if(!u[i])
		{
			return 0;
		}
	}
	return 1;
}

int main()
{
    /*
    freopen("input","r",stdin);
    freopen("output","w",stdout);      
    /**/

             
    int T;
    sf(T);
    for(int t=1; t<=T; t++)
    {
        int n;
        sf(n);
        if(n==0)
        {
            printf("Case #%d: INSOMNIA\n",t);
        }
        else
        {
            memset(u,0,sizeof(u));
            int j;
    	    for(j=1; j<1000000; j++)
    	    {
    		    if(check((ll)j*n))
    		    break;
        	}
            printf("Case #%d: %I64d\n",t,(ll)j*n);
        }
    }



    return 0;
}










