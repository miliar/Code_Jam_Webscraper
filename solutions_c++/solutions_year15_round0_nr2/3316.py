#include <cstdio>
#include <algorithm>

using namespace std;

const int maxD = 10000;

int cake[maxD];

void testCase(int nr)
{
	int d;
	scanf("%d", &d);
	for (int i = 0; i < d; ++i)
		scanf("%d", &cake[i]);
	int mx = *max_element(cake, cake + d);
	int best = mx;
	for (int i = 1; i < mx; ++i) {
		int special = 0;
		for (int j = 0; j < d; ++j) {
			special += (cake[j] - 1) / i;
		}
		if (special + i < best)
			best = special + i;
	}
	printf("Case #%d: %d\n", nr, best);
}

int main()
{
	int t;
	scanf("%d", &t);
	for (int i = 1; i <= t; ++i)
		testCase(i);
}