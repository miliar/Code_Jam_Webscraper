#include <cstdio>
#include <ctime>
#include <cassert>
#include <cstdlib>
#include <cstring>
#include <vector>
#include <numeric>
#include <set>
#include <algorithm>
#include <iostream>
#include <queue>
using namespace std;

#define REP(i,n) for(int i=0;i<(n);i++)

typedef long long ll;

int arr[1001];
int b[1001];

//int brute(int cur, int inc)
//{
//	if(cur==1) return 1+inc;
//	int res=cur+inc;
//	if(arr[cur]==0)
//		res=min(res,brute(cur-1,inc));
//	else
//		for(int i=1;i<=cur-i;i++)
//		{
//			arr[i]+=arr[cur];
//			arr[cur-i]+=arr[cur];
//			res=min(res,brute(cur-1,inc+arr[cur]));
//			arr[i]-=arr[cur];
//			arr[cur-i]=arr[cur];
//		}
//	return res;
//}

int solve()
{
	int n;
	scanf("%d",&n);
	memset(arr,0,sizeof(arr));
	REP(i,n)
	{
		int t;
		scanf("%d",&t);
		arr[t]++;
	}
	int res=1000;
	for(int border=1;border<=res;border++)
	{
		int cnt=0;
		memset(b,0,sizeof(b));
		for(int i=border+1;i<=1000;i++)
		{
			cnt+=((i-1)/border)*arr[i];
		}
		res=min(res,border+cnt);
	}
//	int inc=0;
//	for(int i=1000;i>=1;i--)
//	{
//		if(inc>=res) break;
//		res=min(res,i+inc);
//		inc+=arr[i];
//		arr[i/2]+=arr[i];
//		arr[i-i/2]+=arr[i];
//	}
	return res;
}

int main()
{
	int T;
	scanf("%d",&T);
	for(int test=1;test<=T;test++)
	{
		printf("Case #%d: %d\n",test, solve());
	}
	return 0;
}
