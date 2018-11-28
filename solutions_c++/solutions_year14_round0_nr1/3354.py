#include <cstdio>
#include <unordered_set>
using namespace std;
//int a[4][4];
int ra;
//int b[4][4];
int rb;
int main(int argc, const char *argv[])
{
	int T;
	scanf("%d", &T);
	unordered_set<int> s;
	int tmp, val;
	for (int i = 1; i <= T; i++) {
		s.clear();
		scanf("%d", &ra);
		for (int j = 0; j < 4; j++) {
			for (int k = 0; k < 4; k++) {
				//scanf("%d", &a[j][k]);
				scanf("%d", &tmp);
				if (j == ra - 1) {
					s.insert(tmp);
				}
			}
		}
		scanf("%d", &rb);
		int cnt = 0;
		for (int j = 0; j < 4; j++) {
			for (int k = 0; k < 4; k++) {
				scanf("%d", &tmp);
				if (j == rb - 1 && s.count(tmp) == 1) {
					cnt++;
					if (cnt == 1) {
						val = tmp;//remember the first
					}
				}
			}
		}
		if (cnt == 0) {
			printf("Case #%d: Volunteer cheated!\n", i);
		} else if (cnt == 1) {
			printf("Case #%d: %d\n", i, val);
		} else {
			printf("Case #%d: Bad magician!\n", i);
		}
	}
	return 0;
}
