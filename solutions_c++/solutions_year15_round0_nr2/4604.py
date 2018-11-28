#include <bits/stdc++.h>
using namespace std;
int a[1000005],b,n1,t;
bool f[1000005];

void fn(int n,int i)
{
       int m=max_element(a,a+n)-a;
       swap(a[n-1],a[m]);
       b=min(b,a[n-1]+i);
       if(a[n-1]==1)return;
       int p=a[n-1]/2; int r=a[n-1];
         a[n]=p;
         a[n-1]=r-a[n];
         fn(n+1,i+1);
         if(p>=2){
         a[n]=p-1;
         a[n-1]=r-a[n];
         fn(n+1,i+1);}
         a[n-1]=r;
       swap(a[n-1],a[m]);
       return ;
       }
int main ()
{
//freopen("B-small-attempt4.in","r",stdin);
//freopen("Output.txt","w",stdout);
cin>>t;
for(int j=1;j<=t;j++)
{
  for(int i=0;i<1000000;i++)
  f[i]=0;

  scanf("%d",&n1);
  for(int i=0;i<n1;i++)
    scanf("%d",&a[i]);

  sort(a,a+n1);
  b=a[n1-1];
  fn(n1,0);
  printf("Case #%d: %d\n",j,b);
}
return 0;
}
