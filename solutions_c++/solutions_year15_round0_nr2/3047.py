#include <cstdio>
#include <cstring>
#include <algorithm>
#define NN 1008

using namespace std;

int max_e(int a[], int n)
{
	int i, maxe = a[0];
	for (i=0; i<n; i++) {
		if (maxe < a[i]) maxe = a[i];
	}
	return maxe;
}

int main()
{
	int t;
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	scanf("%d", &t);
	for (int cas=1; cas<=t; cas++)
	{
		int d, p[NN], i;
		scanf("%d",&d);
		for (i=0; i<d; i++) scanf("%d", &p[i]);
		int last, maxe;
		maxe = max_e(p, d);
		int mint = maxe;
		for (last=1; last<=maxe; last++)
		{
			int time_s = last;
			for (i=0; i<d; i++) {
				if (p[i] <= last) continue;
				time_s += (p[i]-1)/last;
			}
			if (mint > time_s) mint = time_s;
		}
		printf("Case #%d: %d\n", cas, mint);
	}
	return 0;
}

