#include<stdio.h>
#include<map>
#include<vector>
#include<iostream>
#include<math.h>
#include<algorithm>

using namespace std;

#define mod 1000000007

int checkp(long long int i)
{
    int n;
    char s[20];
    n=sprintf(s,"%lld",i);
    
    int j;
    for(j=0;j<n;j++)
      { 
         if(s[j]==s[n-1-j])
         {}
         else
         {return 0;}
      }
    return 1;
    
}



int main()
{
    
  freopen("input.txt","r",stdin);
  freopen("output.txt","w",stdout);

    int t,cnt=1;
    cin>>t;
    while(t--)
    {
     long long int i,j,a,b,res,a1,b1;
      cin>>a>>b;
      
      double n,m;
      n=(double)a;
      m=(double)b;      
 
 res=sqrt(n);
 a1=res;
 res=sqrt(m);
 b1=res+1;
 
 int count=0;
      for(i=a1;i<=b1;i++)
         {
            if(checkp(i))
              {
                 res=i*i;
                 if(res>=a&&res<=b)
                  { if(checkp(res))
                      {count++;}
                  } 
                  
              }    
             
         }



cout<<"Case #"<<cnt<<": "<<count<<"\n"; cnt++;  

}
//cin>>i;
return 0;    
}
