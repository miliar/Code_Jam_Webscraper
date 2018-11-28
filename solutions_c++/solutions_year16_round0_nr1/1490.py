#include <iostream>
#include <vector>

using namespace std;
const string NO = "INSOMNIA";
int T, N, rest;

bool check(vector<bool> &vis, int k) {
    while (k != 0) {
	int i = k % 10;
	k /= 10;
	if (!vis[i]) {
	    vis[i] = true;
	    --rest;
	    if (rest == 0) return true;
	}
    }
    return false;
}

int main() {
    scanf("%d", &T);
    for (int t = 1; t <= T; ++t) {
	scanf("%d", &N);
	if (N == 0) {
	    printf("Case #%d: INSOMNIA\n", t);
	    continue;
	}
	vector<bool> vis(10, false);
	rest = 10;
	for (int k = N; ; k += N) {
	    //	    printf("%d : %d\n", t, k);
	    if (check(vis, k)) {
		printf("Case #%d: %d\n", t, k);
		break;
	    }
	}
    }
    return 0;
}
