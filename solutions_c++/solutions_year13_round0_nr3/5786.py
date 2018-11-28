#include<stdio.h>
#include<string.h>

int t,i,j,k,l,a[10000],x,y,ans;
int main()
{
    freopen("C-small-attempt0.in","r",stdin);
    freopen("output.txt","w",stdout);
    memset(a,0,sizeof(a));
    a[1]=a[4]=a[9]=a[121]=a[484]=1;
    for(i=1;i<=1000;i++)
    {
        a[i]+=a[i-1];
    }
    scanf("%d",&t);
    for(i=1;i<=t;i++)
    {
        scanf("%d %d",&x,&y);
        ans=a[y]-a[x-1];
        printf("Case #%d: %d\n",i,ans);
    }
    return 0;
}
