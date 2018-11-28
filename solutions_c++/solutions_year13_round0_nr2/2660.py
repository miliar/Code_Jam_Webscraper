#include<cstdio>
#include<iostream>
#include<algorithm>
#include<cstring>
#include<string>
#include<cmath>
#include<queue>
#include<map>
using namespace std;
typedef long long int int64;
int main()
{
//freopen("in.txt","r",stdin);
//freopen("out.txt","w",stdout);
int64 i,j,k,t,n,m,mv,ra[105],ca[105],krf,kcf,fl,cnt=1,a[105][105];
cin>>t;
while(t--)
{
scanf("%lld %lld",&n,&m);mv=-1;
for(i=0;i<n;i++)for(j=0;j<m;j++){scanf("%lld",&a[i][j]);if(a[i][j]>mv)mv=a[i][j];}
for(k=mv;k>=1;k--)
  {
   memset(ra,0,sizeof(ra));memset(ca,0,sizeof(ca));krf=kcf=0;fl=1;
   for(i=0;i<n;i++){ra[i]=0;for(j=0;j<m;j++)if(a[i][j]<=k)ra[i]++;}
   for(j=0;j<m;j++){ca[j]=0;for(i=0;i<n;i++)if(a[i][j]<=k)ca[j]++;}
   for(i=0;i<n;i++)if(ra[i]==m)krf++;
   for(i=0;i<m;i++)if(ca[i]==n)kcf++;
   for(i=0;i<n;i++)if(!(ra[i]==m||ra[i]==kcf))fl=0;
   for(i=0;i<m;i++)if(!(ca[i]==n||ca[i]==krf))fl=0;
  }
if(fl==1)printf("Case #%lld: YES\n",cnt);
else printf("Case #%lld: NO\n",cnt);
cnt++;
}
return 0;
}
