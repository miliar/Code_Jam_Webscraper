#include <stdio.h>
#include <set>

using namespace std;

int main() {
	int T;
	scanf("%d", &T);
	for (int ca = 1; ca <= T; ca++) {
		set<int> all;
		for (int i = 1; i <= 16; i++)
			all.insert(i);

		for (int z = 0; z < 2; z++) {
			int a;
			scanf("%d", &a);
			for (int i = 0; i < 4; i++) {
				for (int j = 0; j < 4; j++) {
					int x;
					scanf("%d", &x);
					if (i + 1 != a) {
						all.erase(x);
					}
				}
			}
		}

		printf("Case #%d: ", ca);
		if (all.size() == 0) {
			printf("Volunteer cheated!\n");
		}
		else if (all.size() == 1) {
			printf("%d\n", *all.begin());
		}
		else {
			printf("Bad magician!\n");
		}
	}
	return 0;
}