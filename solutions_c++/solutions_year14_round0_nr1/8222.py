#include <cstring>
#include <iostream>
#include <cstdio>

using namespace std;

#define PROBLEM_NAME "A-small-attempt0"
#define INPUT_FILE_NAME "/home/moustafa/" PROBLEM_NAME ".in"
#define OUTPUT_FILE_NAME "/home/moustafa/" PROBLEM_NAME ".out"

int main() {

#ifndef ONLINE_JUDGE
	freopen(INPUT_FILE_NAME, "r", stdin);
	freopen(OUTPUT_FILE_NAME, "w", stdout);
#endif

	int tc;
	scanf("%d", &tc);
	int it = 0;

	while (++it <= tc) {
		printf("Case #%d: ", it);
		int fr, sr;
		scanf("%d", &fr);
		int v[17];
		memset(v, 0, 17*sizeof(int));
		int a, b, c, d;
		for (int ii = 0; ii < 4; ii++) {
			scanf("%d %d %d %d", &a, &b, &c, &d);
			if (ii == fr-1)
			{
				v[a]++;
				v[b]++;
				v[c]++;
				v[d]++;
			}
		}
		scanf("%d", &sr);
		for (int ii = 0; ii < 4; ii++) {
					scanf("%d %d %d %d", &a, &b, &c, &d);
					if (ii == sr-1)
					{
						v[a]++;
						v[b]++;
						v[c]++;
						v[d]++;
					}
		}

		int nsol = 0;
			int sol = 0;
			for (int ii = 1; ii < 17; ii++)
				if (v[ii] == 2)
				{
					nsol++;
					sol = ii;
				}
		if (nsol == 1) {
			printf("%d", sol);
		} else if (nsol  > 1) {
			printf("Bad magician!");
		} else {
			printf("Volunteer cheated!");
		}
		puts("");
	}



	return 0;
}
