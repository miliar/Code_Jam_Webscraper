#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
#define int64 long long
#define Sort sort

using namespace std;

const int Maxn = 11000;

//int f[Maxn][Maxn];
int a[Maxn];
int N,X;

int main()
{
	freopen("input2.in","r",stdin);
	freopen("output2.txt","w",stdout);
	
	int T;
	scanf("%d",&T);
	for (int ii=0;ii<T;++ii)
	{
		printf("Case #%d: ",ii+1);
		scanf("%d%d",&N,&X);
		for (int i=1;i<=N;++i)
			scanf("%d",&a[i]);
		Sort(a+1,a+N+1);
		int res = 0;
		for (int i=1,j=N;i<=j;)
		{
			for (;a[i]+a[j] > X && i < j;--j) ++res;
			++res;
			if (i == j) break;
			++i;--j;
		}
		printf("%d\n",res);
	}
		
	return 0;
}