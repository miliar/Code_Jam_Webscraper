// b@ver
#include<cstdio>
#include<iostream>
#include<algorithm>
#include <cmath>
#include <vector>
#include<cstring>
#include<cstdlib>
using namespace std;
int main()
{
  // freopen("B-small-attempt1.in","r",stdin);
   int t,tc;
   scanf("%d",&t);
   tc=t;
   while(t--)
   {
       int a,b,k,mm,sum,oth,i,j,res;
       long long int ct=0;
      scanf("%d%d%d",&a,&b,&k);
      sum=a+b;
      mm=min(a,b);
      oth=sum-mm;
      for(i=0;i<mm;i++)
      {
         for(j=0;j<oth;j++)
         {
            res=i&j;
            if(res<k)
               ct++;
         }
      }
      cout<<"Case #"<<tc-t<<": "<<ct<<endl;
   }
   return 0;

}
