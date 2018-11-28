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
bool comp(pair<ll,ll>a, pair <ll,ll>b)
{
    if(a.first == b.first)
    {
        return a.second>b.second;
    }
    return a.first < b.first;
}

int main()
{
     freopen("0in.txt", "r", stdin);
     freopen("0out.txt", "w", stdout);

    ll tcase,t,i,s;
    int a[2000],ans,stand;
   scanf("%d",&tcase);
   for(t=1;t<=tcase;t++)
   {
   	   scanf("%d",&s);
   	   for(i=0;i<=s;i++)
   	   {
   	       scanf("%1d",&a[i]); 	
	   }
	   
	   //cout<<endl;
	   ans = 0;
	   stand = 0;
	   for(i=0;i<=s;i++)
	   {
	   	   if(i==0)
	   	   {
		      stand += a[i]; 
		   }
		   else
		   {
		   	    if(stand>=i)
		   	    {
		   	       stand += a[i];	
				}
				else
				{
					 ans += i - stand;
					 stand += (i-stand) + a[i];
				}
		   }
	   }
	   
	   printf("Case #%d: %d\n",t,ans);
   }
     
 return 0;
}

