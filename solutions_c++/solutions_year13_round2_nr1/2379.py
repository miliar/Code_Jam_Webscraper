#include <iostream>
#include <cstdio>
#include <climits>
#include <algorithm>
#include <queue>
#include <cstring>
#include <cmath>
#include <vector>
#include <stack>
#include <set>
#include <map>
#include <deque>
#include <string>
#define SET(p) memset(p,-1,sizeof(p))
#define CLR(p) memset(p,0,sizeof(p))
#define LL long long int
#define ULL unsigned long long int
#define S(n)					scanf("%d",&n)
#define Sl(n)					scanf("%lld",&n)
#define Sf(n) 					scanf("%lf",&n)
#define Ss(n) 					scanf("%s",n)
using namespace std;
int arr[1000010];
bool is_ok(int n,int init)
{
	int i,j,k;
	for(i=0;i<n;i++)
	{
		if(init<=arr[i])
		return false;
		init+=arr[i];
	
	}
	return true;
}
int maxadd(LL &a,LL v)
{
	//int ans=0;
	LL k=1;
	int ans=1;
	if(a==1)
	return INT_MAX;
	//LL init=a;
	while(a+(a-1)<=v)
	{
		a+=a-1;
		ans++;
	}
	a+=a-1+v;
	return ans;
}
int main()
{
	int i,j,k,l,m,n,t;
	#ifndef ONLINE_JUDGE
	freopen("test1.in","r",stdin);
	freopen("op1.txt","w",stdout);
	#endif
	k=1;
	S(t);
	while(t--)
	{
		printf("Case #%d: ",k++);
		LL armin;
		Sl(armin),S(n);
		for(i=0;i<n;i++)
		S(arr[i]);
		sort(arr,arr+n);
		LL init=armin;
		i=0;
		while(armin>arr[i]&&i<n)
		armin+=arr[i++];
		if(i==n)
		{
			printf("0\n");
			continue;
		}
		int st=i;
		
		int ans=0;
		for(i=st;i<n;i++)
		{
			if(armin>arr[i])
			{
				armin+=arr[i];
				continue;
			}
			
			//cout<<i<<" "<<armin<<endl;
			int a=n-i;
			int v=maxadd(armin,arr[i]);
			//cout<<i<<" "<<armin<<endl;
			if(a<=v)
			{
				ans+=a;
				break;
			}
			else
			{
				//armin+=(1<<(v-1))*(armin-1);
				ans+=v;
			}
			
		}
		printf("%d\n",ans);
		
		
		
		
		
	}
	return 0;
}
