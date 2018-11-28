#include <cstdio>
#include <algorithm>
using namespace std;
const int Len = 1000;
int n;
double A[Len+5], B[Len+5];
int ans0, ans1;
void solve()
{
	sort(A, A+n);
	sort(B, B+n);
	int id0 = 0, id1 = 0;
	ans1 = 0;
	while (id0 < n && id1 < n)
	{
		if (A[id0] < B[id1])
		{
			++ans1;
			++id0;
			++id1;
		}
		else ++id1;
	}
	ans1 = n-ans1;
	ans0 = ans1;
	for (int i = 0; i < n; ++i)
		if (i == 0 || A[i-1] < B[n-i])
		{
			id0 = i, id1 = 0;
			int tmpans = 0;
			while (id0 < n && id1 < n-i)
			{
				if (A[id0] < B[id1]) ++tmpans;
				++id0;
				++id1;
			}
			ans0 = max(ans0, n-(tmpans+i));
		}
	printf("%d %d\n", ans0, ans1);
}
int main()
{
	//freopen("E:\\My Code\\GCJ\\QR\\D-large.in", "r", stdin);
	//freopen("E:\\My Code\\GCJ\\QR\\D-large.out", "w", stdout);
	int T;
	int Case = 1;
	scanf("%d", &T);
	while (T--)
	{
		scanf("%d", &n);
		for (int i = 0; i < n; ++i)
			scanf("%lf", &A[i]);
		for (int i = 0; i < n; ++i)
			scanf("%lf", &B[i]);
		printf("Case #%d: ", Case++);
		solve();
	}
}