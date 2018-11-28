#include<iostream>
#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<algorithm>
using namespace std;
int C,T,n,i,j,k,ans1,ans2,a[2000],b[2000];
double xx;
bool used[2000];
int main()
{
    freopen("D-large.in","r",stdin);
    freopen("D-large.out","w",stdout);
    scanf("%d",&T);
    for (C=1;C<=T;C++)
    {
        scanf("%d",&n);
        //memeset(f,false,sizeof(f));
        for (i=1;i<=n;i++)
        {
            scanf("%lf",&xx);    
            a[i]=xx*100000;
            //f[a[i]]=true;
        }
        for (i=1;i<=n;i++)
        {
            scanf("%lf",&xx);    
            b[i]=xx*100000;
            //f[b[i]]=true;
        }        
        sort(a+1,a+n+1); sort(b+1,b+n+1);
        ans1=0; ans2=0;
        memset(used,false,sizeof(used));
        for (i=1;i<=n;i++)
        {
            for (j=1;j<=n;j++) 
            if ((!used[j])&&b[j]>a[i]) break;
            if (j<=n)
            {
                 used[j]=true;   
            } else ans2++;   
        }
        memset(used,false,sizeof(used));
        for (i=1;i<=n;i++)
        {
            for (j=1;j<=n;j++) 
            if ((!used[j])&&a[j]>b[i]) break;
            if (j<=n)
            {
                 used[j]=true;   
                 ans1++;
            }  
        }
        //for (i=1;i<=n;i++) cout<<a[i]<<" "; cout<<endl;
        //for (i=1;i<=n;i++) cout<<b[i]<<" "; cout<<endl;
        printf("Case #%d: %d %d\n",C,ans1,ans2);
    }
    
    
    return 0;    
}
