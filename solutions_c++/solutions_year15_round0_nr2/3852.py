#include<bits/stdc++.h>
using namespace std;
int b[1000100];
int getans(int *a, int n)
{
    int ans,tmp,j,i,c[10000];
    sort(a,a+n);
    ans=a[n-1];
    if(ans==1) return 1;
    tmp=a[n-1]/2;
    for(i=0;i<n;i++) c[i]=a[i];
    for(j=2;j<=tmp;j++)
    {
        a[n-1]-=j;
        a[n]=j;
        ans=min(ans,getans(a,n+1)+1);
        for(i=0;i<n;i++) a[i]=c[i];
    }
    return ans;
}
int main()
{
    int t,j,i,n,ans;
    scanf("%d",&t);
    for(j=1;j<=t;j++)
    {
        scanf("%d",&n);
        for(i=0;i<n;i++)
        {
            scanf("%d",&b[i]);
        }
        ans=getans(b,n);
        printf("Case #%d: %d\n",j,ans);
    }
}
