#include <bits/stdc++.h>

using namespace std;

int S[40], cnt = 0;

void Print (void) {
	++cnt;
	for (int k = 1; k <= 32; k++) printf("%d", S[k]);
	printf(" 3 2 5 2 7 2 3 2 11\n");
}

int main (int argc, char const *argv[]) {
	//freopen("input.txt", "r", stdin);
	freopen("C-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);

	S[1] = S[32] = 1;

	printf("Case #1:\n");
	Print();
	
	for (int i = 2; i <= 31; i += 2)
		for (int j = 3; j <= 31; j += 2) {
			if (cnt == 500) break;
			S[i] = S[j] = 1;
			Print();
			S[i] = S[j] = 0;
		}

	for (int i = 2; i <= 31; i += 4)
		for (int j = 3; j <= 31; j += 4)
			for (int s = 4; s <= 31; s += 4)
				for (int t = 5; t <= 31; t += 4) {
					if (cnt == 500) break;
					S[i] = S[j] = S[s] = S[t] = 1;
					Print();
					S[i] = S[j] = S[s] = S[t] = 0;
				}
	return 0;
}

