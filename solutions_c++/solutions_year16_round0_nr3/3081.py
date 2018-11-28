#include <bits/stdc++.h>

using namespace std;

unsigned long long int get_num(int num, int N, int dig[]) {
	unsigned long long int ans = 0, n = 1;
	for (int i = 0; i < N; i++) {
		ans += dig[i] * n;
		n *= num;
	}
	
	return ans;
}

int main() {
	int T;
	scanf("%d", &T);
	for (int e = 1; e <= T; e++) {
		int N, J;
		scanf("%d %d", &N, &J);
		
		int num[N];
		for (int i = 0; i < N; i++) num[i] = 0;
		
		num[1] = 1;
		num[N - 1] = 1;
		int answer = 0;
		printf("Case #%d:\n", e);
		while (answer < J) {
			int div[10] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
			
			int i = 1;
			while (num[i] == 1) {
				num[i] = 0;
				i++;
			}
			num[i] = 1;
			num[N - 1] = 1;
			num[0] = 1;
			
			for (i = 2; i <= 10; i++) {
				if (div[i - 1] != 0) continue;
				unsigned long long int t_num = get_num(i, N, num);
				unsigned long long int l, last = sqrt(t_num);//t_num / 2;
				for (l = 2; l <= last; l++) {
					if (t_num % l == 0) {
						div[i - 1] = l;
						//cout << t_num << " " << l << endl;
						break;
					}
				}
				if (l > last) break;
			}
			if (i < 11) continue;
			
			for (int i = N - 1; i >= 0; i--) printf("%d", num[i]);
			printf(" ");
			for (int i = 1; i < 10; i++) printf("%d ", div[i]);
			printf("\n");
			answer++;
		}
	}
	
	
	return 0;
} 