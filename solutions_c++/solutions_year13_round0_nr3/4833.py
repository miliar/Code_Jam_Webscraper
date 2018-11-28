#include<iostream>
#include<cstdio>
using namespace std;

int main()
{
      int no[]={1,4,9,121,484};
      
      int t,i,j,a,b;
      
      cin>>t;
      
      for(i=1;i<=t;i++)
      {
                 cin>>a>>b;
                 cout<<"Case #"<<i<<": ";
                int ans=0,x;
                 
                 x=1;
                 if(a<=x&&x<=b)
                 ans++;  
                 x=4;
                 if(a<=x&&x<=b)
                 ans++;  
                 x=9;
                 if(a<=x&&x<=b)
                 ans++;  
                 x=121;
                 if(a<=x&&x<=b)
                 ans++;  
                 x=484;
                 if(a<=x&&x<=b)
                 ans++;
                 
                 cout<<ans<<"\n";     
      }
          return 0;
}
