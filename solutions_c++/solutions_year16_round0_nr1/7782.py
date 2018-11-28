#include<iostream>
#include<algorithm>
#include<vector>
#include<map>
#include<cstdio>
#include<cstring>
using namespace std;
 
 
int main()
{
  long long i,n,t,k,sum,c[100],count,no;
  char a[100];
  cin>>t;
  for(k=1;k<=t;k++)
  {
      cin>>n;
      if(n==0)
      {
          cout<<"Case #"<<k<<": INSOMNIA"<<endl;
          continue;
      }
      for(i=0;i<100;i++)
        c[i]=0;
      snprintf(a,10,"%lld",n);
      count=0;
      no=n;
      while(count!=10)
      {
          snprintf(a,10,"%lld",n);
          for(i=0;a[i]!='\0';i++)
          {
              if(c[a[i]]==0)
              {
                  count++;
                  c[a[i]]++;
              }
          }
          n+=no;
      }
        cout<<"Case #"<<k<<": "<<n-no<<endl;
  }
  
} 