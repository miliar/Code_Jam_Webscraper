// ConsoleApplication1.cpp : 定義主控台應用程式的進入點。
//

#define _CRT_SECURE_NO_DEPRECATE
#include <cstdio>
#include <algorithm>

int main() {
	int FoodStack[2000];
	int T, D, sum;
	int A = 0, minA = 0, step = 0;

	freopen("1.in", "r", stdin);
	freopen("2.out", "w", stdout);

	scanf_s("%d", &T);
	while (T--)
	{
		scanf_s("%d", &D);
		for (int i = 0; i < D; i++) {
			scanf_s("%d", &FoodStack[i]);
			A = (A > FoodStack[i]) ? A : FoodStack[i];
		}
		minA = A;
		for (int i = 1; i <= A; i++) {
			sum = i;
			for (int j = 0; j < D; j++) {
				if (FoodStack[j] > i) {
					if (FoodStack[j] % i == 0)
						sum += (FoodStack[j] / i - 1);
					else
						sum += (FoodStack[j] / i);
				}
			}
			minA = (minA < sum) ? minA : sum;
		}
		printf_s("Case #%d: %d\n", ++step, minA);
	}
	return 0;
}

