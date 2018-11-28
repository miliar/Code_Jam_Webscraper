#include <stdio.h>
#include <algorithm>
#include <memory.h>
using namespace std;

struct data {
	long long s, e, n;
	int si, ei;

	inline bool operator < (const data &rhs) const { return s < rhs.s; }
};
int n, m;
data d[1010];

int xcnt, x[2010];
long long cnt[2010];

long long solve (long long *cnt, int s, int e)
{
	if (s>=e) return 0;

	long long m=cnt[s];
	for (int i=s; i<e; i++) {
		if (m > cnt[i])
			m = cnt[i];
	}

	for (int i=s; i<e; i++)
		cnt[i] -= m;

	long long res = m * (x[e]-x[s])*(x[e]-x[s]-1)/2;
	int last=s;
	for (int i=s; i<e; i++) {
		if (cnt[i]==0) {
			res += solve(cnt, last, i);
			last = i+1;
		}
	}

	return res + solve(cnt, last, e);
}

int bsearch (int* x, int low, int high, int v)
{
	int mid;
	while (low<=high) {
		mid=(low+high) /2;
		if (x[mid]==v) return mid;
		if (x[mid]< v) low=mid+1;
		else high=mid-1;
	}

	return -1;
}


int main()
{
	freopen ("a.in", "r", stdin);
	freopen ("a.out", "w", stdout);

	int t, tt=0;
	scanf ("%d", &t);
	while (t--) {
		scanf ("%d%d", &n, &m);
		xcnt=0;

		long long c1=0, c2=0;
		for (int i=0; i<m; i++) {
			scanf ("%lld%lld%lld", &d[i].s, &d[i].e, &d[i].n);
			x[xcnt++] = d[i].s;
			x[xcnt++] = d[i].e;

			c1 -= d[i].n * (d[i].e - d[i].s) * (d[i].e - d[i].s - 1) / 2;
		}

		sort(x, x+xcnt);
		
		memset(cnt, 0, sizeof(cnt));

		for (int i=0; i<m; i++) {
			d[i].si = bsearch (x, 0, xcnt, d[i].s);
			d[i].ei = bsearch (x, 0, xcnt, d[i].e);

			cnt[d[i].si] += d[i].n;
			cnt[d[i].ei] -= d[i].n;
		}

		for (int i=0; i<xcnt; i++) {
			if(i)
				cnt[i] += cnt[i-1];
		}

		c1 += solve (cnt, 0, xcnt-1);


		printf ("Case #%d: %lld\n", ++tt, c1);
	}

	return 0;
}
