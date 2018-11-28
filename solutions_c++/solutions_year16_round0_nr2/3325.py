#include "bits/stdc++.h"
using namespace std;
char input[101];
int main() {
	freopen("B-small-attempt0.in", "r", stdin);
	int Case;
	//Case = 1000000;
	cin >> Case;
	FILE *fp = fopen("output.text","w");
	for (int tc = 1; tc <= Case; tc++) {
		scanf("%s", input);
		int len = strlen(input);
		int reverse = 1;
		int ans = 0;
		for (int i = len - 1; i >= 0; i--) {
			if (reverse == 1) {
				if (input[i] == '+')
					continue;
				reverse *= -1;
				ans++;
			}
			else {
				if (input[i] == '-')
					continue;
				reverse *= -1;
				ans++;
			}
		}
		fprintf(fp,"Case #%d: %d\n", tc,ans);
	}
	return 0;
}