#include<iostream>
#include<math.h>
#include<string.h>
#include<algorithm>
using namespace std;
int main()
{
 freopen("de.txt","r",stdin);
 freopen("dea.txt","w",stdout);
 int t;
 cin>>t;
 for(int q=1;q<=t;++q)
 {
  int n,dwans=0,wans=0;
  cin>>n;
  double na[n],ke[n],na1[n],ke1[n];
  for(int i=0;i<n;++i)
  {cin>>na[i];na1[i]=na[i];}
  for(int i=0;i<n;++i)
  {cin>>ke[i];ke1[i]=ke[i];}
  sort(na,na+n);sort(ke,ke+n);sort(na1,na1+n);sort(ke1,ke1+n);
  //for dewar
  for(int i=0;i<n;++i)
  {
   int f=0;
   for(int j=0;j<n;++j)
   {
    if(na[j]!=-1.0)
    {
     if(na[j]>ke[i])
     {
      f=1;
      dwans++;
      na[j]=-1.0;
      ke[i]=-1.0;
      break;               
     }             
    }        
   }        
   if(f==0)
   {
    ke[i]=-1.0;
    for(int j=0;j<n;++j)
    {
     if(na[j]!=-1.0)
     {
      na[j]=-1.0;
      break;               
     }        
    }        
   }
  }
  //for war
  for(int i=0;i<n;++i)
  {
   int f=0;
   for(int j=0;j<n;++j)
   {
    if(ke1[j]!=-1.0)
    {
      if(ke1[j]>na1[i])
      {
       f=1;
       ke1[j]=-1.0;
       na1[i]=-1.0;
       break;                 
      }         
    }        
   }        
   if(f==0)
   {
    wans++;
    na1[i]=-1.0;
    for(int j=0;j<n;++j)
    {
     if(ke1[j]!=-1.0)
     {
      ke1[j]=-1.0;
      break;                
     }        
    }        
   }
  }
  printf("Case #%d: %d %d\n",q,dwans,wans);        
 }    
}
