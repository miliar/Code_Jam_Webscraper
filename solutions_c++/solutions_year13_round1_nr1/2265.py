#include <cstdio>
#include <math.h>
#include <algorithm>
#define FOR(a,b,c) for(int i=a; i<b; i+=c)

using namespace std;

unsigned long long r,t,req,a;
int ans=0;

int main()
{
	int T=0,cas=1;
	scanf("%d",&T);
	while(T--)
	{
        printf("Case #%d: ",cas++);
        scanf("%llu %llu",&r,&t);
        ans=0;
        //printf("%llu\n",t);
        a = (2*r) + 1;
        req = (2 + sqrt(((a-2)*(a-2)) + (8 * t)) - a)/4;
        printf("%llu\n",req);
        /*while(1)
        {
            req = (2 * r) + 1;
            if(req>t)break;
            t-= req;
            r+=2;
            ans++;
            //printf("%llu ",t);
        }*/
        //printf("%d\n",ans);
	}
}
