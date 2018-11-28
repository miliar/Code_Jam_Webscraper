#include<stdio.h>
#include<iostream>
#include<algorithm>
#define rep(i,a,b) for(i=a;i<=b;i++)

using namespace std;
int main()
{
    
    freopen("in.in","r",stdin);
    freopen("out.txt","w",stdout);
    int t,n,i,j,ans,ans1,m;
    scanf("%d",&t);
   rep(m,1,t)
    {
              scanf("%d",&n);
              
              double a[n],b[n];
              
              rep(i,0,n-1)
              scanf("%lf",&a[i]);
              
              rep(i,0,n-1)
              scanf("%lf",&b[i]);
              
              
              sort(a,a+n);
              sort(b,b+n);
              
              //decieved war
              i=n-1;
              j=n-1;
              ans1 = 0;
              while(i>=0)
              {
                          if(a[i] > b[j])
                          i--,ans1++;
                          else
                          i--,j--;
              }
              
              //war
              i = 0;
              j = 0;
              ans = 0;
              while(i!=n)
              {
                          if(a[i] > b[j])
                          i++,j++,ans++;
                          else
                          i++;
              }
              
              
              printf("Case #%d: %d %d\n",m,ans,ans1);
    }
    
    return 0;
}
