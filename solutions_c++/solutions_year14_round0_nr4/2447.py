//soting google code jam o(n)

#include<iostream>
#include<cstdio>
#include<stdlib.h>
#include<iomanip>
#include<math.h>
#include<limits.h>
#include<string.h>
#include<algorithm>
#include<vector>
#include<stack>
#include<queue>
#include<map>
#define mod 1000000007
#define MAX 100000000

using namespace std;

#define PB(x) push_back(x)
#define SORT(a) sort(a.begin(),a.end())
#define INF 1000000000
#define V vector
#define S string
typedef long long LL;
typedef long double LD;
typedef long L;
typedef pair<int, int> p;
const double pi=acos(-1.0);
int main()
{
	int t;
	freopen("in.in","r",stdin);
    freopen("output.out","w",stdout);
	int c=1;
	scanf("%d",&t);
	while(t--)
	{
     int n;
     scanf("%d",&n);
     vector<double>v,v1;
     for(int i=0;i<n;i++)
     {
     	 double j;
     	 scanf("%lf",&j);
     	 v.PB(j);
     }
     for(int i=0;i<n;i++)
     {
     	 double j;
     	 scanf("%lf",&j);
     	 v1.PB(j);
     }
     sort(v.begin(),v.end());
     sort(v1.begin(),v1.end());
     int ans1=0;
     int a=0,b=0;
     while(1)
     {
     	  if(v[a]<v1[b])
     	  {
     	     ans1++;
     	     a++;
     	     b++;
     	  }
     	  else
     	     b++;
     	  
     	  if(a==n || b==n)
     	     break;
     }
     
     int ans2=0;
     a=0,b=0;
     
     while(1)
     {
     	  if(v1[b]<v[a])
     	  {
     	     ans2++;
     	     a++;
     	     b++;
     	  }
     	  else 
     	  	   a++;
     	  if(a==n || b==n)
     	     break;
     }
     printf("Case #%d: ",c++);
	 printf("%d %d\n",ans2,n-ans1);
	 }
     return 0;
 }

