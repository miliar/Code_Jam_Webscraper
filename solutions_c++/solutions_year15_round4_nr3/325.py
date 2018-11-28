#include <iostream>
#include <sstream>
#include <cstdio>
#include <cstring>
#include <string>
#include <cstdlib>
#include <vector>
#include <algorithm>
#include <map>
#include <cmath>
#include <set>
using namespace std;

int n;
char buf[10000];
vector<int> a[300];
int o[3000];
int f[300];
int ans;
int o2[3000];

void dfs(int d, int sum) {
    if (d == n) {
        if (sum < ans) {
            ans = sum;
        }
        return;
    }
    if (sum >= ans)
        return;
    int o2[3000];
    memcpy(o2, o, sizeof(o));
    int sum0 = sum;
    int i = d;
    if (d != 1) {
            for (int j = 0; j < a[i].size(); j++) {
                if (o[a[i][j]] != 3) {
                    o[a[i][j]] |= 1;

                    if (o[a[i][j]] == 3) {
                        sum0++;
                    }
                }
            }
        dfs(d + 1, sum0);
    }
    memcpy(o, o2, sizeof(o));
    sum0 = sum;
    if (d != 0) {
    for (int j = 0; j < a[i].size(); j++) {
                if (o[a[i][j]] != 3) {
                    o[a[i][j]] |= 2;
                    if (o[a[i][j]] == 3) {
                        sum0++;
                    }
                }
            }
    dfs(d + 1, sum0);
    }
}

void solve() {
    scanf("%d", &n);
    getchar();
    map<string, int> tocode;
    for (int i = 0; i < n; i++) {
        a[i].clear();
        gets(buf);
        istringstream strin(buf);
        string s;
        while (strin >> s) {
            if (tocode.find(s) == tocode.end()) {
                tocode[s] = tocode.size();
            }
            a[i].push_back(tocode[s]);
        }
    }
    ans = 10000000;
    dfs(0, 0);
    printf("%d\n", ans);
}

int main() {
    freopen("E:/1.in", "r", stdin);
    freopen("E:/1.out", "w", stdout);

	int T;
	scanf("%d", &T);
	for (int i = 1; i <= T; i++) {
        printf("Case #%d: ", i);
		solve();
		cerr << i << endl;
	}
	return 0;
}
