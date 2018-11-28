#include <cstdio>
#include <vector>
FILE* inputFile;
FILE* outputFile;
int t;
int res[2], row[4];
std::vector<int> pos, ans;
bool in(int a) {
	for (int i = 0; i < pos.size(); i++) {
		if (pos[i] == a) {
			return true;
		}
	}
	return false;
}
int main() {
	freopen("magic.in", "r", stdin);
	freopen("magic.out", "w", stdout);
	scanf("%d ", &t);
	for (int i = 1; i <= t; i++) {
		printf("Case #%d: ", i);
		scanf("%d ", &res[0]);
		for (int j = 1; j <= 4; j++) {
			for (int k = 0; k < 4; k++) {
				scanf("%d ", &row[k]);
			}
			if (j == res[0]) {
				for (int k = 0; k < 4; k++) {
					pos.push_back(row[k]);
				}
			}
		}
		scanf("%d ", &res[1]);
		for (int j = 1; j <= 4; j++) {
			for (int k = 0; k < 4; k++) {
				scanf("%d ", &row[k]);
			}
			if (j == res[1]) {
				for (int k = 0; k < 4; k++) {
					if (in(row[k])) {
						ans.push_back(row[k]);
					}
				}
			}
		}
		if (ans.size() == 0) {
			printf("Volunteer cheated!\n");
		} else if (ans.size() > 1) {
			printf("Bad magician!\n");
		} else {
			printf("%d\n", ans[0]);
		}
		pos.clear();
		ans.clear();
	}
	return 0;
}
