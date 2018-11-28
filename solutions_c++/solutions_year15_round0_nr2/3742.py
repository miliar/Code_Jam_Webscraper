#include <cstdio>
#include <algorithm>
using namespace std;
int arr[1010],a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z;
int main()
{
    scanf(" %d",&t);
    for(l=1;l<=t;l++)
    {
        printf("Case #%d: ",l);
        scanf(" %d",&d);
        for(i=0;i<d;i++)scanf(" %d",&arr[i]);
        z=2000000;
        for(i=1;i<=1000;i++)
        {
            s=0;
            for(j=0;j<d;j++)s+=(arr[j]-1)/i;
            s+=i;
            z=min(s,z);
        }
        printf("%d\n",z);
    }
    return 0;
}
