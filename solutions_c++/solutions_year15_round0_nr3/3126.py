#include <stdio.h>
#include <iostream>
#include <string>

using namespace std;

int table[4][4] = {{0, 1, 2 , 3},
				   {1, 0, 3, 2}, 
				   {2, 3, 0, 1}, 
				   {3, 2, 1, 0}};
int semn[4][4] = {{0, 0, 0 , 0},
				   {0, 1, 0, 1}, 
				   {0, 1, 1, 0}, 
				   {0, 0, 1, 1}};

int D[4][10005];
int codif[300];

int main() {

	freopen("c.in", "r", stdin);
	freopen("c.out", "w", stdout);

	codif['1'] = 0, codif['i'] = 1, codif['j'] = 2, codif['k'] = 3;

	int tests, t = 0;
	scanf("%d", &tests);
	while (tests--) {

		int len, rep; string init_s, s = " ";
		cin >> len >> rep >> init_s;
		for (int i = 0; i < rep; ++i) {
			s += init_s;
		}
		// cout << s << "\n";

		memset(D, 0, sizeof(D));
		D[0][0] = 1;
		for (int i = 1; i < 4; ++i) {

			for (int j = 1; j < s.size(); ++j) {
				int crt = 0, crt_semn = 0;
				for (int k = j; k >= 1; --k) {
					int prev_crt = crt;
					crt = table[codif[s[k]]][prev_crt];
					crt_semn ^= semn[codif[s[k]]][prev_crt];
					// cout << "CRT = " << crt << " at " << i << " " << j << " " << k << "\n";;
					if (crt == i && crt_semn == 0 && D[i-1][k-1]) {
						D[i][j] = 1;
						// cout << i << " " << j << "\n";
					}
				}
			}
		}

		++t;
		printf("Case #%d: ", t);
		if (D[3][s.size()-1]) {
			printf("YES\n");
		} else {
			printf("NO\n");
		}

		fprintf(stderr, "%d\n", tests);
	}

	return 0;
}