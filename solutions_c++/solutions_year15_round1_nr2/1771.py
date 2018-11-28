#include<iostream>
#include<stdio.h>
#include<map>
#include<algorithm>
#include<stack>
#include<queue>
#include<string.h>
#include<string>
#include<stdlib.h>
#include<math.h>
#include<fstream>
#include<set>

using namespace std;
typedef long long int ll;
typedef unsigned long long ull;
int xx[]={1,1,1,0,-1,-1,-1,0}; // 8 direction
int yy[]={-1,0,1,1,1,0,-1,-1}; // 8 direction
int rx[] = {1,-1,0,0}; // 4 direction
int ry[] = {0,0,1,-1}; // 4 direction
ll gcd(ll a,ll b)
{ return ((a%b==0)?b:gcd(b,a%b)) ;}

int main()
{
   freopen("0in.txt", "r", stdin);
   freopen("0out.txt", "w", stdout);
   ll tcase,t,i,b,n,pos,bar[1000+5],p,v,c,len,tm,j,f;
   scanf("%lld",&tcase);
   for(t=1;t<=tcase;t++)
   {
   	vector<int>ve;
   	tm=50;
   	   scanf("%lld %lld",&b,&n);
   	  
   	   for(i=1;i<=b;i++)
   	   {
   	       scanf("%lld",&bar[i]);
			  if(bar[i]<tm)
			  tm=bar[i]; 	
	       ve.push_back(i);
	       
	   }
	   len = b;
	   while(1)
	   {
	   	f=0;
	   	for(j=1;j<=b;j++)
	   	{
	   		if(tm%bar[j]==0)
	   		{
			   ve.push_back(j);
	   		len++;
	   		f++;
	   	}
		   }
	   	if(f==b)
	   	break;
	   	tm++;
	   	
	   }
	   len=len-b;
	   n=n%len;
	   //for(j=0;j<len;j++)
	   //printf("%lld\n",ve[j]);
	   if(n-1<0)
	   printf("Case #%lld: %lld\n",t,ve[len-1]);
	   else
	   printf("Case #%lld: %lld\n",t,ve[n-1]);
	  
   }
   
 return 0;
}

