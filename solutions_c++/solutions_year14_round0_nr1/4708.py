#include <cstdio>
#include <string>
#include <iostream>
using namespace std;
int T, x1, x2, a[6], a1[6], a2[6];
int main() {
	scanf("%d", &T);
	for (int t = 1; t <= T; ++t) {
		scanf("%d\n", &x1);
		for (int  i = 1; i < 5; ++i) 
			for (int j = 0; j < 4; ++j)
				if (i == x1) scanf("%d", a1 + j);
				else scanf("%d", a + j);
		scanf("%d", &x2);
		for (int  i = 1; i < 5; ++i) 
			for (int j = 0; j < 4; ++j)
				if (i == x2) scanf("%d", a2 + j);
				else scanf("%d", a + j);
		int ans(0), res;
		for (int i = 0; i < 4; ++i)
			for (int j = 0; j < 4; ++j)
				if (a1[i] == a2[j]) {
					ans++;
					res = a1[i];
				}
		printf("Case #%d: ", t);
		if (ans == 1) printf("%d\n", res);
		if (ans == 0) printf("Volunteer cheated!\n");
		if (ans > 1) printf("Bad magician!\n");
	}
	return 0;
}

