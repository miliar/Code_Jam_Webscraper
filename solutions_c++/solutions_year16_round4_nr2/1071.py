#include <stdio.h>
#include <stdlib.h>
int t;
int n;
int k;
double A[20];
int shuffle[20];
int cutshuffle[20];
int cnt;
int cnt2;
double val[20];
double rounds;
double ans;
void res2()
{
 for(int i=1;i<=n;i++)
 {
  cutshuffle[i]=0;
 }
}
void pri2()
{
 printf("2>>");
 for(int i=1;i<=k;i++)
 {
  printf("%d",cutshuffle[i]);
 }
 printf("\n");
}
void pri1()
{
 printf("1>>");
 for(int i=1;i<=n;i++)
 {
  printf("%d",shuffle[i]);
 }
 printf("\n");
}
bool chk2()
{
 for(int i=k;i>=1;i--)
 {
  if(cutshuffle[i]==0)
  {
   cutshuffle[i]=1;
   cnt2++;
   for(int j=i+1;j<=k;j++)
   {
    cutshuffle[j]=0;
    cnt2--;
   }
   return true;
  }
  else if(i==1){return false;}
 }
}
double solve2()
{
double myans=0;
double thisans;
double mytmp;
 cnt2=0;
 res2();
 do
 {
  if(cnt2==(k/2))
  {
   thisans=1;
   for(int i=1;i<=k;i++)
   {
    if(cutshuffle[i]==1){mytmp=val[i];}
    else{mytmp=(double)1-val[i];}
    thisans=thisans*mytmp;
   }
  // pri2();
  // printf("%lf\n",thisans);
   myans=myans+thisans;
  }
 }
 while(chk2());
 return myans;
}
bool chk()
{
 for(int i=n;i>=1;i--)
 {
  if(shuffle[i]==0)
  {
   shuffle[i]=1;
   cnt++;
   for(int j=i+1;j<=n;j++)
   {
    shuffle[j]=0;
    cnt--;
   }
   return true;
  }
  else if(i==1){return false;}
 }
}
void solve()
{
double kk;
//printf("in\n");
cnt=0;
 do{
  //pri1();
  if(cnt==k)
  {
  // printf("yes\n");
   cnt2=0;
   for(int i=1;i<=n;i++)
   {
    if(shuffle[i]==1){cnt2++;val[cnt2]=A[i];}
   }
   kk=solve2();
   //printf("ans = %lf\n",kk);
   if(kk>ans){ans=kk;}
  }
 }
 while(chk());
}
void res1()
{
 for(int i=1;i<=n;i++)
 {
  shuffle[i]=0;
 }
}
main()
{
 freopen("B-small-attempt0.in","r",stdin);
 freopen("B-small-attempt0.out","w",stdout);
 scanf("%d",&t);
 for(int tests=1;tests<=t;tests++)
 {
  scanf("%d%d",&n,&k);
  res1();
  ans=0;
  for(int i=1;i<=n;i++)
  {
   scanf("%lf",&A[i]);
  }
  solve();
  printf("Case #%d: ",tests);
  printf("%.10lf\n",ans);
 }
 
 return 0;
}
