#include<iostream>
#include<stdio.h>
using namespace std;
int main()
{
 int g,t,i,n,ans=0,j,ans2=0,x;
 float one[10000],two[10000],tem,he[10000];
 cin>>t;
 for(g=0;g<t;g++)
 {
  cin>>n;
  for(i=0;i<n;i++)
  { cin>>one[i];  he[i]=one[i];  }
  for(i=0;i<n;i++)
  cin>>two[i];

  for(i=0;i<n;i++)
  { for(j=0;j<n;j++)
    {  if(one[j]>one[i])
       { tem=one[i];
         one[i]=one[j];
         one[j]=tem;
       }
    }
  }

  for(i=0;i<n;i++)
  { for(j=0;j<n;j++)
    {  if(two[j]>two[i])
       { tem=two[i];
         two[i]=two[j];
         two[j]=tem;
       }
    }
  }

  for(i=0;i<n;i++)
  {
   for(j=0;j<n;j++) 
   if(two[i]<one[j]) { ans++;  one[j]=0;   break; }
  }

  x=n; 
 
  for(i=0;i<n;i++)
  { for(j=0;j<n;j++)
     {  if(two[j]>he[i]) {  x--;  two[j]=0;   break; } 
     }
  }


  cout<<"Case #"<<g+1<<": "<<ans<<" "<<x<<endl;

  
  ans=0;
  }

 return 0;
}
     
 

