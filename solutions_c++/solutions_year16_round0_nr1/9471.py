#include <bits/stdc++.h>

using namespace std;

bool doneded[10];

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("output.out", "w", stdout);

	int t;
	scanf("%d", &t);
	for (int tc=1; tc<=t; tc++) {
		printf("Case #%d: ", tc);
		int cnt = 0, n;
		scanf("%d", &n);
		if (n==0) {
			printf("INSOMNIA\n");
			continue;
		}
		int temp = n;
		memset(doneded, false, sizeof(doneded));
		cnt = 0;
		while (cnt != 10 && temp<=(int)1e9 * 2) {
			int temp2 = temp;
			while (temp2>0) {
				if (!doneded[temp2%10]) {
					doneded[temp2%10] = true;
					cnt++;
				}
				temp2/=10;
			}
			temp+=n;			
		}		
		printf("%d\n", temp-n);
	}
	return 0;
}