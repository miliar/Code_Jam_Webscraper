#include <iostream>
#include <cstdio>
#include <string>
#include <cstring>
#include <vector>
#include <map>
#include <queue>
#include <algorithm>
#include <cmath>
#include <ctime>
using namespace std;

typedef long long LL;
typedef pair<int,int> pii;
typedef vector<int>::iterator vit;
typedef map<int,int>::iterator mit;

int n,p;

int worst(int x)
{
	int ret = 0;
	for (int i = 0;i < n;++i)
	{
		if (!x) break;
		ret += (1 << (n - i - 1));
		x--;
		x >>= 1;
	}
	return ret;
}

int best(int x)
{
	return (1 << n) - 1 - worst((1 << n) - 1 - x);
}

void work(int no)
{
	printf("Case #%d: ",no);
	scanf("%d%d",&n,&p);
	int l = 0,r = (1 << n);
	while (l + 1 < r)
	{
		int mid = (l + r) >> 1;
		if (worst(mid) < p)
			l = mid;
		else r = mid;
	}
	printf("%d ",l);
	l = 0,r = (1 << n);
	while (l + 1 < r)
	{
		int mid = (l + r) >> 1;
		if (best(mid) < p)
			l = mid;
		else r = mid;
	}
	printf("%d\n",l);
}

int main()
{
	int times;
	scanf("%d",&times);
	for (int i = 1;i <= times;++i)
		work(i);
	return 0;
}
