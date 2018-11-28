#include<iostream>
#include<cstdio>
#include<string.h>
#include<algorithm>
#include<map>
#include<math.h>
#include<vector>
using namespace std;
#define maxn 50
int n,m,i,j,k;
int x;
int a[maxn],w[maxn],l[maxn],r[maxn];
int nowr[maxn],nowl[maxn];
int tst,cas;
void getnow()
{
     int i,j,mi;
     for (i=0;i<n;i++)
     {
         nowr[i]=0;
         for (j=0;j<i;j++)
             if (a[j]<a[i] && nowr[j]>nowr[i]) nowr[i]=nowr[j];
         nowr[i]++;
     }
     for (i=n-1;i>=0;i--)
     {
         nowl[i]=0;
         for (j=n-1;j>i;j--)
             if (a[j]<a[i] && nowl[j]>nowl[i]) nowl[i]=nowl[j];
         nowl[i]++;
     }
}
int inf=0x7f7f7f7f;
bool getans;
void dfs(int x)
{
     if (x>=n)
     {
        getans=1;
        return;
     }
     int i,nnl[maxn],nnr[maxn];
     memcpy(nnl,nowl,sizeof(nowl));
     memcpy(nnr,nowr,sizeof(nowr));
     for (i=0;i<n;i++)
         if (a[i]>=inf && nowl[i]==l[i] && nowr[i]==r[i])
         {
             w[x]=i;
             a[i]=x;
             getnow();
             dfs(x+1);
             if (getans) return;
             memcpy(nowl,nnl,sizeof(nowl));
             memcpy(nowr,nnr,sizeof(nowr));
             a[i]=inf;
             w[x]=0;
         }
//            cout<<x+1<<" "<<i<<endl;
}
int main()
{
    cin>>tst;
    for (cas=1;cas<=tst;cas++)
    {
        cin>>n;
        for (i=0;i<n;i++) cin>>r[i];
        for (i=0;i<n;i++) cin>>l[i];
        memset(a,127,sizeof(a));
        for (i=0;i<n;i++) nowr[i]=nowl[i]=1;
        getans=0;
        dfs(0);
        if (!getans) goto Wrong;
        cout<<"Case #"<<cas<<":";
        for (i=0;i<n;i++) cout<<" "<<a[i]+1;
        cout<<endl;
        if (0) Wrong:cout<<"Wrong!!\n";
    }
    return 0;
}
