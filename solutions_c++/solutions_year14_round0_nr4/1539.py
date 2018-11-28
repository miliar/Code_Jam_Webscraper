#include<iostream>
#include<algorithm>
using namespace std;
double a[1000+10];
double b[1000+10];
int n;
int get1()
{
   int s=0;
   int ans=0;
   while(b[s]>a[0])
      s++;
   while(a[n-s-1]<b[n-1])
      s++;
   for(int i=n-s-1;i>=0;i--)
   {
      if(a[i]>b[n-1])
      {
          ans++;  
          n--;
      }
   }
   return ans;
}
int get2()
{
    int j=0;
    int ans=0;
    for(int i=0;i<n;i++)
    {
      while(j<n&&a[j]>b[i])
         j++;
      if(j<n)
         ans++;
      j++;
    }  
    return n-ans;
}
int main()
{
    freopen("D-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    int t;
    cin>>t;
    int cas=1;
    while(t--)
    { 
       cin>>n;
       for(int i=0;i<n;i++)
         scanf("%lf",a+i);
       for(int i=0;i<n;i++)
         scanf("%lf",b+i);
       sort(a,a+n,greater<double>());
       sort(b,b+n,greater<double>());
       printf("Case #%d: ",cas++);
       printf("%d %d\n",get1(),get2());
    }
    return 0;
}
                 
           
