#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <stack>
#include <queue>
#include <map>
#include <set>
#define PB push_back
#define MP make_pair
#define X first
#define Y second
#define lc (k<<1)
#define rc ((k<<1)|1)
using namespace std;
typedef long long ll;
typedef unsigned long long ull;

int a[1003];

int main()
{
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);

	int cas; scanf("%d",&cas);
	for(int t=1;t<=cas;t++)
	{
		int n,mx=0; scanf("%d",&n);
		for(int i=0;i<=n;i++)
		{
			char ch=' ';
			while(ch<'0'||ch>'9')
				ch=getchar();
			a[i]=ch-'0';
			if(a[i]) mx=max(mx,i);
		}
		int now=0,add=0;
		for(int i=0;i<=mx;i++)
		{
			if(now<i)
			{
				add+=i-now;
				now=i;
			}
			now+=a[i];
		}
		printf("Case #%d: %d\n",t,add);
	}
	return 0;
}