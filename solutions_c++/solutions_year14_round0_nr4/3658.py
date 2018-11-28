#include<stdio.h>
#include<algorithm>
using namespace std;
int main()
{
    
    freopen("inl.in","r",stdin);
    freopen("out.txt","w",stdout);
    int t,n,i,l1,l2,ans,ctr,cases=1;
    scanf("%d",&t);
    while(t--)
    {
              scanf("%d",&n);
              double a[n],b[n];
              for(i=0;i<n;i++)
              scanf("%lf",&a[i]);
              for(i=0;i<n;i++)
              scanf("%lf",&b[i]);
              
              
              sort(a,a+n);
              sort(b,b+n);
              
              
              l1 = 0;
              l2 = 0;
              ans = 0;
              while(l1!=n)
              {
                          if(a[l1] > b[l2])
                          l1++,l2++,ans++;
                          else
                          l1++;
              }
              
              
              l1=n-1;
              l2=n-1;
              ctr = 0;
              while(l1>=0)
              {
                          if(a[l1] > b[l2])
                          l1--,ctr++;
                          else
                          l1--,l2--;
              }
              
              
              printf("Case #%d: %d %d\n",cases++,ans,ctr);
    }
}
