#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;
struct diao
{
    int shei;
    double weight;
    bool operator < (const diao &x)const
    {
        return weight<x.weight;
    }
}a[2010];
int main(void){
    freopen("D-large.in","r",stdin);
    freopen("laobi.out","w",stdout);
   int casenum;
   scanf("%d",&casenum);
   for(int k=1;k<=casenum;k++)
   {
      int n;
      scanf("%d",&n);
      for(int i=1;i<=n;i++)
      {
            scanf("%lf",&a[i].weight);
            a[i].shei=1;
      }
      for(int i=n+1;i<=2*n;i++)
      {
            scanf("%lf",&a[i].weight);
            a[i].shei=2;
      }
      sort(a+1,a+1+2*n);
      /*for(int i=1;i<=n;i++)
            printf("%lf  ",a[i]);
            printf("\n");
      for(int i=1;i<=n;i++)
            printf("%lf  ",b[i]);
            printf("\n");*/
     //for(int i=1;i<=2*n;i++)
       //     printf("%lf  %d\n",a[i].weight,a[i].shei);
      int ans1,ans2;
      int res=0;
      int temp=0;
      for(int i=1;i<=2*n;i++)
      {
          if(a[i].shei==1)
          {
            res++;
          }
          else
          {
              if(res>0){res--;temp++;}
          }
      }
      ans2=n-temp;
      res=0;
       temp=0;
      for(int i=2*n;i>=1;i--)
      {
          if(a[i].shei==1)
          {
            res++;
          }
          else
          {
              if(res>0)
              {res--;temp++;}
          }
      }
    ans1=temp;
    printf("Case #%d: %d %d\n",k,ans1,ans2);
   }
    return 0;
}
