#include <bits/stdc++.h>
using namespace std;
#define MOD 1000000007


 
int main()
{
    
   long long int t,index=0,N;
   int a[10];
   scanf("%lld",&t);
   while(t--)
   {
       index++;
       int x=100000;
       long long int temp;
      scanf("%lld",&N);
      
      for(int i=0;i<10;i++)
      a[i]=0;
      long long int n=N;
      while(x--){
          temp=n;
      while(temp)
      {
          a[temp%10]=1;
          temp/=10;
      }
      for(int j=0;j<10;j++)
      {if(a[j]==0)
      goto there;}
      break;
      there:
      n=n+N;
      }
      for(int i=0;i<10;i++)
      {if(a[i]==0)
      goto wrong;}
      printf("Case #%lld: %lld\n",index,n);
      continue;
      wrong:
      printf("Case #%lld: INSOMNIA\n",index);
      
   }
    return 0;
}
 
