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

const int Maxn = 1100;

int f[Maxn],g[Maxn];
int a[Maxn];
int N;

int main()
{
	freopen("input2.in","r",stdin);
	freopen("output2.txt","w",stdout);
	
	int T;
	scanf("%d",&T);
	for (int ii=0;ii<T;++ii)
	{
		printf("Case #%d: ",ii+1);
		scanf("%d",&N);
		for (int i=1;i<=N;++i)
			scanf("%d",&a[i]);
		int res = 0;
		for (int i=1;i<=N;++i)
		{
			int aa = 0,bb = 0;
			for (int j=1;j<i;++j)
				if (a[j] > a[i]) ++aa;
			for (int j=i+1;j<=N;++j)
				if (a[j] > a[i]) ++bb;
			res += min(aa,bb);
		}
		printf("%d\n",res);
	}
		
	return 0;
}