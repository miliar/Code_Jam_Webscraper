#include<cstdio>
#include<algorithm>
using namespace std;
int nr,p,maxi,X,pt,T,i,j,k,n,dp[12][4096],ap[1009];
double mini,a[1009],b[1009];
int ceiau(int mask,double val)
{
    double ras=1000000;
    int i,p;
    for(i=0;i<n;i++)
        if(mask&(1<<i)&&b[i+1]>val&&b[i+1]<ras) ras=b[i+1],p=i+1;
    if(ras==1000000)
    {
        for(i=0;i<n;i++)
            if(mask&(1<<i)&&b[i+1]<ras) ras=b[i+1],p=i+1;
        return p;
    }
    return p;
}
void back(int poz,int mask,int pct)
{
    if(poz==n+1)
    {
        if(pct>maxi) maxi=pct;
        return ;
    }
    int i,p;
    for(i=1;i<=n;i++)
        if(ap[i]==0)
        {
            ap[i]=1;
            p=ceiau(mask,a[i]);
            if(b[p]<a[i]) back(poz+1,mask-(1<<(p-1)),pct+1);
            else back(poz+1,mask-(1<<(p-1)),pct);
            ap[i]=0;
        }
}
bool ok(int P)
{
    int i;
    for(i=1;i<=P;i++)
        if(a[n-P+i]<b[i]) return 0;
    return 1;
}
int main()
{
//freopen("input","r",stdin);
//freopen("output","w",stdout);
scanf("%d",&T);
while(T)
{
    pt++;
    T--;
    printf("Case #%d: ",pt);
    scanf("%d",&n);
    for(i=1;i<=n;i++)
        scanf("%lf",&a[i]);
    for(i=1;i<=n;i++)
        scanf("%lf",&b[i]);
    sort(a+1,a+n+1);
    sort(b+1,b+n+1);
    ok(2);
    for(i=n;i>=1;i--)
        if(ok(i)) break;
    printf("%d ",i);
    nr=0;
    for(i=1;i<=n;i++)
    {
        mini=10000000;
        for(j=1;j<=n;j++)
            if(b[j]!=-1&&b[j]>a[i]&&b[j]<mini) mini=b[j],k=j;
        if(mini==10000000)
        {
            mini=100000000;
            for(j=1;j<=n;j++)
                if(b[j]!=-1&&b[j]<mini) mini=b[j],k=j;
            b[k]=-1;
            nr++;
        }
        else b[k]=-1;
    }
    p=1;
    printf("%d\n",nr);
}
return 0;
}
