#include <cstdio>
#include <set>
using namespace std;

int r, c;
int map[111][111];
bool rowsame[111], colsame[111];

void reconstruct() {
	for (int i = 0; i < r; ++i) {
		rowsame[i] = true;
		for (int j = 1; j < c; ++j) {
			if (map[i][j] != map[i][0]) {
				rowsame[i] = false;
				break;
			}
		}
	}
	for (int j = 0; j < c; ++j) {
		colsame[j] = true;
		for (int i = 1; i < r; ++i) {
			if (map[i][j] != map[0][j]) {
				colsame[j] = false;
				break;
			}
		}
	}
}

int main() {
	int t;
	scanf("%d", &t);
	for (int tt = 1; tt <= t; ++tt) {
		set<int> values;
		scanf("%d %d", &r, &c);
		for (int i = 0; i < r; ++i)
			for (int j = 0; j < c; ++j) {
				scanf("%d", &map[i][j]);
				values.insert(map[i][j]);
			}

		set<int>::iterator it = values.begin();
		int next = *it;
		++it;
		while (it != values.end()) {
			int v = next;
			next = *it;
			++it;
			
			reconstruct();
			for (int i = 0; i < r; ++i) {
				for (int j = 0; j < c; ++j) {
					if (map[i][j] == v) {
						if (!rowsame[i] && !colsame[j]) {
							printf("Case #%d: NO\n", tt);
							goto end;
						}
					}
				}
			}
			for (int i = 0; i < r; ++i) {
				for (int j = 0; j < c; ++j) {
					if (map[i][j] == v) {
						map[i][j] = next;
					}
				}
			}
		}
		
		printf("Case #%d: YES\n", tt);
		end: ;
	}
}
