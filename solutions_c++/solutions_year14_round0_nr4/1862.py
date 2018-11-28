#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <climits>
#include <algorithm>
#include <vector>
#include <map>
#include <stack>
#include <queue>
#include <deque>
#include <set>
#include <cstdlib>
#include <string>
#include <sstream>
using namespace std;

#define sqr(x) ((x)*(x))
#define lowbit(x) ((x)&(-x))

#define MAXN 1005
double a[MAXN], b[MAXN];
int n;

int main()
{
	int T, cases = 0;
	scanf("%d", &T);
	while (T--)
	{
		scanf("%d", &n);
		for (int i = 0; i < n; ++i)
			scanf("%lf", &a[i]);
		for (int i = 0; i < n; ++i)
			scanf("%lf", &b[i]);
		sort(a, a + n);
		sort(b, b + n);
		printf("Case #%d: ", ++cases);
/*		for (int i = 0; i < n; ++i)
			printf("%lf ", a[i]);
		printf("\n");
		for (int i = 0; i < n; ++i)
			printf("%lf ", b[i]);
		printf("\n");
		*/
		int j = 0, s1 = 0, s2 = 0;
		for (int i = 0; i < n; ++i)
			if (a[i] > b[j])
			{
				s1++;
				j++;
			}
		j = 0;
		for (int i = 0; i < n; ++i)
		{
			while (j < n && a[i] > b[j]) ++j;
			if (j >= n) 
			{
				s2 = n - i;
				break;
			}
			++j;
		}
		printf("%d %d\n", s1, s2);
	}
	return 0;
}
