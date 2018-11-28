#include<cstdio>
#include<cstdlib>
#include<iostream>
#include<map>
#include<algorithm>
#include<vector>
#include<iomanip>
using namespace std;
int main()
{
   long long int i,j,k,l,m,n,t,T;
   double c,f,x,ans,totalTime,freq,M;
   freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
   cin>>T;
   M = (double)1000000;
   for(t=1;t<=T;t++)
   {
      totalTime = (double)0;
      freq = (double)2;
      cin>>c>>f>>x;
      while(1)
      {
         double lhs = (x*M)/freq;
         double rhs = (x*M)/(freq + f) +  (c*M)/freq;
         if(lhs < rhs)
         {
            totalTime = totalTime + (lhs);
            break;
         }
         else
         {
            totalTime = totalTime + ((c*M)/freq);
            freq = freq + f;
         }
      }
      cout<<"Case #"<<t<<": ";
      printf("%.7f\n",totalTime/M);
   }
   return 0;
}
