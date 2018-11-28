#define Fractiles

#ifdef Fractiles
#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <algorithm>
#include <vector>

using namespace std;

int main() {
	//freopen("in.txt","rt",stdin);
	freopen("D-small-attempt0.in", "rt", stdin);
	freopen("out.txt", "wt", stdout);

	int T;
	scanf("%d\n", &T);

	for (int i = 1; i <= T; i++) {
		int K, C, S;
		scanf("%d %d %d", &K, &C, &S);
		
		vector <unsigned long long> position;

		for (int j = 1; j <= S; j++) {
			position.push_back(j);
		}

		if (position.size() == 0)
			printf("Case #%d: IMPOSSIBLE\n", i);
		else {
			printf("Case #%d: %", i);
			for (int j = 1; j <= S; j++) {
				printf("%llu ",position[j-1]);
			}
			printf("\n");
		}
	}

	return 0;
}

#endif