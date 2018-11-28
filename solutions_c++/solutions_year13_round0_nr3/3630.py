#include <iostream>
#include <cstdio>
#include <cmath>

using namespace std;

int main()
{
	int t;
	scanf("%d", &t);

	for (int w = 1; w <= t; w++) {
		int a;
		int b;
		scanf("%d%d", &a, &b);

		int c = 0;
		for (int i = a; i <= b; i++) {
			if (i == 1 || i == 4 || i == 9 || i == 121 || i == 484) {
				c++;
			}
			if (i > 484) {
				break;
			}
		}
		printf("Case #%d: %d\n", w, c);
	}

	return 0;
}
