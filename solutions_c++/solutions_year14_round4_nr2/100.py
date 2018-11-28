#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
using namespace std;

const int N = 1010;

int ori[N];

int main ()
{
	freopen("B.in", "r", stdin);
	freopen("B.out", "w", stdout); 
	int T; scanf("%d", &T);
	for (int kase = 1; kase <= T; kase++)
	{
		int n; scanf("%d", &n);
		for (int i = 0; i < n; i++) scanf("%d", &ori[i]);
		int ll = 0, rr = n - 1;
		long long ans = 0;
		for (int i = 0; i < n; i++)
		{
			int s = ll;
			for (int j = ll; j <= rr; j++) if (ori[j] < ori[s]) s = j;
			if (s - ll < rr - s)
			{
				ans += s - ll;
				while (s > ll)
				{
					swap(ori[s], ori[s - 1]);
					--s;
				}
				++ll;
			}
			else
			{
				ans += rr - s;
				while (s < rr)
				{
					swap(ori[s], ori[s + 1]);
					++s;
				}
				--rr;
			}
		}
		printf("Case #%d: %lld\n", kase, ans);
	}
    return 0;
}
