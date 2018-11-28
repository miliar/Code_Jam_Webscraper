#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstdlib>
#include <cstring>
#include <string.h>
#include <string>
#include <map>
#include <queue>
#include <deque>
#include <cmath>
#include <math.h>
#include <vector>
#include <ctime>
#include <cctype>
#include <stack>
#include <set>
#include <bitset>
#include <functional>
#include <numeric>
#include <stdexcept>
#include <utility> 
using namespace std;
#define ll long long 
#define m0(a) memset(a, 0, sizeof(a))
#define m1(a) memset(a, -1, sizeof(a))
#define C1(x)  cout<<x<<endl;
#define C2(x,y)  cout<<x<<" "<<y<<endl;
#define C3(x,y,z)  cout<<x<<" "<<y<<" "<<z<<endl;
struct stu
{
	int x,y,z;
	bool operator < (const stu &b) const
	{
		return x<b.x;	
	}
};
const int inf = 0x3f3f3f3f; 
const double eps = 1e-15;
const double pi = acos((double)-1) ;
const int maxn = 100100;
const ll M = 1e9+7;
ll i,j,k,l,m,n,x,y,z,ans;
int a[maxn]={0};
int num[11]={0};
int dx[4]={0,0,1,-1};
int dy[4]={1,-1,0,0};

ll dis(ll x)
{
	for(ll i=2;i<=sqrt(x);i++)
		if(x%i==0) return i;
		return -1;
}
int main () 
{
	#ifdef ONLINE_JUDGE
	
	#else
	
	    //freopen("in.in","r",stdin);
	    freopen("in.out","w",stdout);
	
	#endif
	int cas;
	scanf("%d",&cas);
	for (int casi=1;casi<=cas;casi++)
	{
		cin>>x>>y;ans=0;
		printf("Case #%d:\n",casi);
		if (x==1)
		{
			printf("1 1 1 1 1 1 1 1 1 1\n");
			continue;
		}
		if (x==2)
		{
			printf("\n");
			continue;
		}
		for (ll i=0;i<=((ll)1<<(x-2))-1;i++)
		{
			ll o=i;
			a[0]=1;a[x-1]=1;
			for (int j=1;j<=x-2;j++)
			{
				a[j]=o%2;
				o>>=1;
			}
			
			for (int j=2;j<=10;j++)
			{
				ll p=1;
				ll o=0;
				for (int k=x-1;k>=0;k--)
				{
					o+=a[k]*p;
					p=p*j;
				}
				num[j]=dis(o);
				if (num[j]==-1) break;
				
				if (j==10)
				{
					//cout<<ans<<":";
					cout<<o;
					for (int k=2;k<=10;k++) cout<<" "<<num[k];
					cout<<endl;
					ans++;
				}
				if (ans>=y) break;
				
			}
			/*
			for (int j=0;j<x;j++)
			{
				printf("%d ",a[j]);
			}
			cout<<endl;
			*/
		}
	}
	return 0;
}
