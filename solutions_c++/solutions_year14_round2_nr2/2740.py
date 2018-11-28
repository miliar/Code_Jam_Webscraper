#include<iostream>
#include<stdio.h>
#include<cmath>
#include<cstring>
#include<stdlib.h>
#include<algorithm>
#include<limits.h>
using namespace std;

/*printing definitions*/
#define pi(x) printf("%d\n",(x))
#define pii(x,y) printf("%d %d\n",(x),(y))
#define pl(x) printf("%lld\n",(x))
#define pll(x,y) printf("%lld %lld\n",(x),(y))
#define pil(x,y) printf("%d %lld\n",(x),(y))
#define pli(x,y) printf("%lld %d\n",(x),(y))
#define plf(x) printf("%lf\n",(x))
#define plflf(x,y) printf("%lf %lf\n",(x),(y))

/*scanning definitions*/
#define si(x) scanf("%d",&x)
#define sii(x,y) scanf("%d %d",&x,&y)
#define sl(x) scanf("%lld",&x)
#define sll(x,y) scanf("%lld %lld",&x,&y)
#define sil(x,y) scanf("%d %lld",&x,&y)
#define sli(x,y) scanf("%lld %d",&x,&y)
#define slf(x) scanf("%lf",&x)
#define slflf(x,y) scanf("%lf %lf",&x,&y)
      
//  CREATED BY: ATUL SEHGAL

int main()
{
    freopen("input-Bsmall.txt","r",stdin);
    freopen("output-Bsmall.txt","w",stdout);
	long long int T=1,a,b,k,t,i,j,n,ans;
	sl(t);
	while(t--)
	{
	    ans=0;
		sll(a,b);sl(k);
		/*long long int maxx=max(a,b),minn=min(a,b);
		/*if(k>=minn)
        {
            ans=maxx*minn;
        }
        else
        {
            long long int q=maxx/k;
            ans=k*maxx+q;
        }*/
        for(i=0;i<a;i++)
        {
            for(j=0;j<b;j++)
            {
                if((i&j)<k)
                    ans++;
            }
        }
		printf("Case #%lld: ",T++);
		pl(ans);
	}
	return 0;
}
