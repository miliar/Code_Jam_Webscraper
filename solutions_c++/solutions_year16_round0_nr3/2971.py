#include <bits/stdc++.h>

using namespace std;

long long t, n, j, jc = 0, i1, i2, i3, i4, f, num, power, last, cur, a1[100], ans[11];

int main()
{
	freopen("b.in", "r", stdin);
 	freopen("b.ans", "w", stdout);
	
	scanf("%d", &t);
	for (i1 = 0; i1 < t; i1++) {
		scanf("%d%d", &n, &j);
		printf("Case #%d:\n", i1 + 1);
		
		power = 1;
		for (i2 = 0; i2 < n; i2++)
			power *= 2;
		for (i2 = (power / 2 + 1); i2 < power; i2 += 2) {
			if (jc >= j)
				break;
			cur = i2;
			last = n;
			while (cur > 0) {
				a1[--last] = cur % 2;
				cur /= 2;
			}
			
			for (i3 = 2; i3 <= 10; i3++) {
				num = 0;
				for (i4 = 0; i4 < n; i4++)
					num = num * i3 + a1[i4];
// 				printf("%lld_%lld = %lld: ", i2, i3, num);
				f = 0;
// 				if (ferma(num))
// 					break;
				for (i4 = 2; i4 <= sqrt(num); i4++)
					if (num % i4 == 0) {
						ans[i3] = i4;
// 						printf("%lld ", i4);
						f = 1;
						break;
					}
// 				printf("\n");
				if (!f)
					break;
			}
			if (f) {
				jc++;
				for (i3 = 0; i3 < n; i3++)
					printf("%d", a1[i3]);
				for (i3 = 2; i3 <= 10; i3++)
					printf(" %lld", ans[i3]);
				printf("\n");
			}
		}
	}
	return 0;
}