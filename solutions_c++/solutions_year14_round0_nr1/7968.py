#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <set>
#include <map>
#include <vector>
#include <string>
#include <iostream>
#include <algorithm>

using namespace std;

#pragma comment(linker, "/STACK:268435456")

typedef pair<int, int> pii;
typedef long long ll;

void solve() {
	set <int> S;
	S.clear();

	int k;
	scanf("%d", &k);
	--k;

	for (int i = 0; i < 4; ++i) {
		for (int j = 0; j < 4; ++j) {
			int a;
			scanf("%d", &a);
			if (i == k) {
				S.insert(a);
			}
		}
	}

	scanf("%d", &k);
	--k;
	bool bad = false;

	int ans = -1;
	for (int i = 0; i < 4; ++i) {
		for (int j = 0; j < 4; ++j) {
			int a;
			scanf("%d", &a);
			if (i == k) {
				if (S.find(a) != S.end()) {
					if (ans != -1) {
						bad = true;
					} else {
						ans = a;
					}
				}
			}
		}
	}

	if (bad) {
		printf("Bad magician!\n");
	} else
	if (ans == -1) {
		printf("Volunteer cheated!\n");
	} else {
		printf("%d\n", ans);
	}
}

int main() {
    freopen("input.txt", "r", stdin);
    freopen("outut.txt", "w", stdout);

    int T;
    scanf("%d", &T);

    for (int i = 1; i <= T; ++i) {
    	printf("Case #%d: ", i);
		solve();
    }

	return 0;
}
