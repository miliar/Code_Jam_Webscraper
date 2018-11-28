#include<iostream>
#include<vector>
#include<string>
#include<algorithm>
#include<map>
#include<stdio.h>
using namespace std;

int actOnIt(vector<int>sizes,int sum,int i,int n);

int main()
{
   int i,j,t,n,c,curr;
   vector<int>sizes(101);
   
   cin>>t;
   
   for(j=1;j<=t;j++)
   {       
      scanf("%d%d",&c,&n);
      
      for(i=0;i<n;i++)
      {
         scanf("%d",&sizes[i]);
      }
      
      sizes[n] = c;
      
      sort(sizes.begin(),sizes.begin()+n+1);
      int sum=0;
       
      i=0; 
      for(i=0;sizes[i]!=c;i++)
      {
         sum+=sizes[i];
      }
      
      sum+=sizes[i];
   
      if(i!=n)
         cout<<"Case #"<<j<<": "<<actOnIt(sizes,sum,i+1,n)<<"\n";
      else 
         cout<<"Case #"<<j<<": 0\n";
   }
}

int actOnIt(vector<int>sizes,int sum,int i,int n)
{
   if(i==n)
   {
      if(sizes[n]<sum)
      return 0;
      
      else return 1;
   }
   
   if(sizes[i]<sum)
   {
      sum+=sizes[i];
      return actOnIt(sizes,sum,i+1,n);
   }
   
   int fc,sc;
   
   fc = 1 + actOnIt(sizes,sum,i+1,n);

   long count = 0;
   
   if(sum!=1)
   {
      while(sizes[i]>=sum)
      {
         sum+=sum-1;
         count++;
      }
   }
   else count = 9999999;
   
   sc = count + actOnIt(sizes,sum+sizes[i], i+1,n);
   
   return min(fc,sc);
}
