#include<iostream>
#include<cstdlib>
#include<cstdio>
#include<algorithm>
#include<cstring>
#include<queue>
#include<cmath>
using namespace std;

int n,m;
int a[1001000];
int check(int p)
{
    int i;
    int now=m;
    for(i=1;i<=n&&p>=0;i++)
    {
        if(now>a[i])now+=a[i];
        else if(n-i+1<=p)
            return 1;
        else 
            now=now*2-1,p--,i--;
    }
    if(p<0)return 0;
    else   return 1;                 
}    
int main()
{
        int i,j,tot,ttl;
        scanf("%d",&tot);
        for(ttl=1;ttl<=tot;ttl++)
        {
            scanf("%d%d",&m,&n);
            int ans=0;
            for(i=1;i<=n;i++)
                scanf("%d",&a[i]);
            sort(a+1,a+1+n);
            int low=-1,up=40;
            while(low+1!=up)
            {
                int mid=(low+up)>>1;
                if(check(mid))
                    up=mid;
                else low=mid;
                    
            }                
            printf("Case #%d: %d\n",ttl,up);
        }
        
        return 0;
}
