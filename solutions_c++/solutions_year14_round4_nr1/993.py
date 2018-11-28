#include<cstdio>
#include<iostream>
#include<algorithm>
#include<cmath>
#include<vector>
#include<set>
#include<map>
#include<cstring>
#include<string>
#include<cstdlib>
#include<ctime>
#include<cassert>

using namespace std;

#define FNAME "1"
#define FILE 1

#define pb push_back
#define mp make_pair
#define LL long long
#define ULL unsigned long long
#define LD long double

#ifdef WIN32
	#define I64 "%I64d"
#else
	#define I64 "%lld"
#endif

int T, n, x, a[100005], ans, it1, it2;

int main()
{
	#if (FILE == 1)
	freopen(FNAME".in", "r", stdin);
	freopen(FNAME".out", "w", stdout);
	#endif
	scanf("%d", &T);
	for (int g = 0; g < T; g++)
	{
		scanf("%d%d", &n, &x);
		for (int i = 0; i < n; i++)
			scanf("%d", &a[i]);
		sort(a, a + n);
		ans = 0;
		it1 = 0;
		it2 = n - 1;
		while(it2 > it1)
		{
			if (a[it1] + a[it2] <= x)
			{
				ans++;
				it1++;
            	it2--;
				continue;
			}
			it2--;
			ans++;
		}
		if (it1 == it2)
			ans++;
		printf("Case #%d: %d\n", g + 1, ans);
	}
	return 0;
}