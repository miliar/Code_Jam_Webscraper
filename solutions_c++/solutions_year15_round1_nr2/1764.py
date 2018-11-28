#include <cstdio>
#include <iostream>
#include <queue>
#define PI pair<long long,long long>
using namespace std;
priority_queue <PI> Q;
long long a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z;
long long arr[100100],seq[100100];
long long ta[101000];
long long gcd(long long a,long long b)
{
    if(b==0)return a;
    return gcd(b,a%b);
}
int main()
{
    scanf(" %lld",&t);
    for(l=1; l<=t; l++)
    {
        printf("Case #%lld: ",l);
        scanf(" %lld %lld",&b,&n);
        for(i=0;i<b;i++)
        {
            scanf(" %lld",&arr[i]);
            ta[i]=arr[i];
        }
        for(i=0; i<b; i++)
        {
            long long c,d;
            if(i>0)
            {
                c=ta[i-1];
                d=ta[i];
                d=gcd(c,d);
                //printf("%d %d\n",ta[i],ta[i-1]);
                ta[i]=(ta[i]*ta[i-1])/d;
                //printf("%lld\n",ta[b]);
            }
            Q.push(PI(0,i*-1));
        }
        s=1,v=0;
        //for(i=0;i<b;i++)s*=arr[i]/g;
        s=ta[b-1];
        for(i=0; i<b; i++)v+=s/arr[i];
        //printf("%d %d\n",s,v);
        for(i=0; i<v; i++)
        {
            a=Q.top().first*-1;
            c=Q.top().second*-1;
            q+=arr[c];
            a+=arr[c];
            seq[z++]=c;
            //printf("%d %d\n",a,c);
            if(i==v)break;
            Q.pop();
            Q.push(PI(a*-1,c*-1));
        }
        printf("%lld\n",seq[(n-1)%(v)]+1);
        while(!Q.empty())Q.pop();
        z=0;
        s=0;
        g=0;
        q=0;
    }
    return 0;
}
