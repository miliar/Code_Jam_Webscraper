#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<math.h>

int main() {

	freopen("input.txt", "r", stdin);
	freopen("output2.txt", "w", stdout);

	int t; scanf("%d", &t);
	for (int k = 0; k < t; k++) {
		int d; scanf("%d",&d);
		int a[1005], max = 0, sum = 0;
		for (int i = 0; i < d; i++) {
			scanf("%d", &a[i]);
			sum += a[i]; 
			if (max < a[i]) max = a[i];
		}

		int ans = max;

		for (int i = 1; i <max; i++) {
			//i�� special minute�� ���� ��. ans-i-1�� �ȿ� �������� ans ���� ����
			//d+i���� ���ð� ����
			for (int j = ans - i - 1;j>=1; j--) {
				// d+i���� ���ÿ� max�� ans-i-1�� �ǵ��� ���� �� �ִ°�?
				int temp = 0;
				for (int l = 0; l < d; l++) {
					temp += (int)ceil((double)a[l] /j);
				}
				if (temp <= d + i) ans = j + i;
				else break;
			}

		}
		printf("Case #%d: %d\n", k + 1, ans);
	}

	return 0;
}