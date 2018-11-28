#include<bits/stdc++.h>

using namespace std;

int p[26];

int main() {
	int t;
	scanf("%d", &t);
	for (int T = 1; T <= t; T++) {
		int n;
		scanf("%d", &n);
		for (int i = 0; i < n; i++) scanf("%d", p + i);
		
		printf("Case #%d:", T);
		
		int sum = 0;
		for (int i = 0; i < n; i++) sum += p[i];
		while (sum > 0) {
			printf(" ");
			int mx = -1, sc = -1;
			for (int i = 0; i < n; i++) {
				if (mx == -1 || p[i] > p[mx]) {
					sc = mx;
					mx = i;
				}
				else if (sc == -1 || p[i] > p[sc]) {
					sc = i;
				}
			}
			
			if (p[mx] == p[sc] && sum == 2 * p[mx]) {
				printf("%c%c", 'A' + mx, 'A' + sc);
				
				p[mx]--;
				p[sc]--;
				sum -= 2;
			}
			else {
				printf("%c", 'A' + mx);
				
				p[mx]--;
				sum -= 1;
			}
		}
		
		printf("\n");
	}
	
	return 0;
}
