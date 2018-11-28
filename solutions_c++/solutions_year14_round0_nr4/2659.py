#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>

using namespace std;

int main()
{
    freopen("in.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    int task;
    scanf("%d", &task);
    double a[1010], b[1010];
    int n;
    for (int t = 1; t <= task; ++t)
    {
	printf("Case #%d: ", t);
	scanf("%d", &n);
	for (int i = 1; i <= n; ++i)
	    scanf("%lf", &a[i]);
	for (int i = 1; i <= n; ++i)
	    scanf("%lf", &b[i]);
	sort(a + 1, a + n + 1);
	sort(b + 1, b + n + 1);
	int z;
	z = n;
	int r = n;
	for (int i = n; i >= 1; --i)
	{
	    for (; r && b[r] > a[i]; --r);
	    if (r) {--z, --r;}
	}
	printf("%d ", n - z);
	
	z = n;
	r = n;
	for (int i = n; i >= 1; --i)
	{
	    for (; r && a[r] > b[i]; --r);
	    if (r) {--z, --r;}
	}
	printf("%d\n", z);
    }
    return 0;
}
