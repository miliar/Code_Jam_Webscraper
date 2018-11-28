#include<iostream>
#include<algorithm>
#include<stdio.h>
#include<string.h>
#include<math.h>
using namespace std;
#define eps 1e-9
#define zero(x) ((fabs(x)<eps?0:x))
int n;
int dos1(double a[],double b[])
{
    int ans=0;
    int j=1;
    int p=1;
    for(int i=1;i<=n;i++)
    {
        if(a[i]>b[j])
        {
            ans++;j++;
        }
        if(a[i]==b[j])
        {
            j++;
        }
    }
    return ans;
}
int  dos2(double a[],double b[])
{
    int ans=0;
    int j=n;
    for(int i=n;i>=1;i--)
    {
        if(a[i]>b[j])ans++;
        else if(a[i]<b[j])j--;
        else if(a[i]==b[j])j--;
    }
    return ans;
}
int main()
{
    freopen("data.in","r",stdin);
  freopen("data.out","w",stdout);
  int T,t;
  cin>>T;
  double a[1100],b[1100];
  for(t=1;t<=T;t++)
  {
      int i;
      cin>>n;
      for(i=1;i<=n;i++)scanf("%lf",&a[i]);
      for(i=1;i<=n;i++)scanf("%lf",&b[i]);
      sort(a+1,a+n+1);
      sort(b+1,b+n+1);
      printf("Case #%d: %d %d\n",t,dos1(a,b),dos2(a,b));
  }
  return 0;
}
