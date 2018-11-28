#include <iostream>
#include <string>
#include <vector>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <utility>
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <climits>
using namespace std;

int n;
double a1[1001], a2[1001];

int main ()
{
	freopen("data.in", "r", stdin);
	freopen("data.out", "w", stdout);
	int TC; scanf("%d", &TC);
	for (int tc = 1; tc <= TC; tc++)
	{
		scanf("%d", &n);
		for (int i = 0; i < n; i++) scanf("%lf", a1+i);
		for (int i = 0; i < n; i++) scanf("%lf", a2+i);
		sort(a1, a1+n);
		sort(a2, a2+n);

		int i = 0, j = 0;
		while (1)
		{
			 while (j < n && a2[j] < a1[i])	 j++;
			 if (j == n) break;
			 else 
			 {
				 i++, j++;
				 if (i == n) break;
			 }
			 
		}
		int ans1 = 0, ans2 = n - i;

		i = 0, j = 0;
		while(1)
		{
			if(a1[i] > a2[j])	ans1++, i++, j++;
			else i++;
			if (i == n)	break;
		}
		printf("Case #%d: ", tc);
		printf("%d %d\n", ans1, ans2);
	}

}