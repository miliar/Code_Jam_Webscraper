#include<cstdio>
#include<cstring>
#include<iostream>
#include<cstdlib>
#include<cmath>
#include<algorithm>
#include<vector>
#include<queue>
#include<stack>
#include<set>
#include<map>

#define il(n) scanf("%lld",&n)
#define i(n) scanf("%d",&n)

using namespace std;
double arr[1005],brr[1005],crr[1005],drr[1005],err[1005],frr[1005];
int main()
{
int tc,j,pos,k,i,n;
cin>>tc;
for(j=1;j<=tc;j++)
{
cin>>n;
for(i=1;i<=n;i++)
cin>>arr[i];
for(i=1;i<=n;i++)
cin>>brr[i];

double miny;
for(i=1;i<=n;i++)
{
    miny =2;
    for(k=1;k<=n;k++)
    {
        if(arr[k]<miny)
        {
            pos=k;
            miny=arr[k];
        }
    }
    crr[i]=arr[pos];
    err[i]=arr[pos];
    arr[pos]=2;
}
for(i=1;i<=n;i++)
{
    miny=2;
    for(k=1;k<=n;k++)
    {
        if(brr[k]<=miny)
        {
            pos=k;
            miny=brr[k];
        }
    }
    drr[i]=miny;
    frr[i]=miny;
    brr[pos]=2;
}

int co=0,ch=1,endy=n;
for(i=1;i<=n;i++)
{
    if(crr[i]>drr[ch])
    {
        co++;
        ch++;
    }else
    {
        drr[endy]=0;
        endy--;
    }
}
int coi=n;
for(i=1;i<=n;i++)
{
    for(k=1;k<=n;k++)
    {
        if(err[i]<frr[k])
        {
            coi=coi-1;
            frr[k]=0;
            break;
        }
    }
}
printf("Case #%d: %d %d\n",j,co,coi);
}
return 0;
}
