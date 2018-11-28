#include <cstdio>
#include <algorithm>
using namespace std;

const int maxn = 1000;

double a[maxn];
double b[maxn];

void task(int t)
{
	int n;
	scanf("%i", &n);
	for (int i = 0; i < n; i++) scanf("%lf", &a[i]);
	for (int i = 0; i < n; i++) scanf("%lf", &b[i]);
	sort(a, a + n);
	sort(b, b + n);
	int xi = 0, xj = 0;
	for (; xj < n; xj++) {
		for (; xi < n; xi++) {
			if (a[xi] > b[xj]) break;
		}
		if (xi == n) break;
		xi++;
	}
	int yi = 0, yj = 0;
	for (; yi < n; yi++) {
		for (; yj < n; yj++) {
			if (a[yi] < b[yj]) break;
		}
		if (yj == n) break;
		yj++;
	}
	printf("Case #%i: %i %i\n", t +1, xj, n - yi);
}

int main()
{
	int t;
	scanf("%i", &t);
	for (int i = 0; i < t; i++) {
		task(i);
	}
	return 0;
}

