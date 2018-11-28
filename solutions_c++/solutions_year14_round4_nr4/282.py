#include <iostream>
#include <string>
#include <map>
#include <math.h>
#include <vector>
#include <algorithm>
#include <cstdio>
#include <set>
#include <queue>
#include <sstream>
#include <deque>
#include <memory.h>
#include <cassert>
#include <ctime>


using namespace std;

#define ll long long
#define y1 _dfdfdfd


const int maxn = 1 << 18;
const int inf = 1000000007;
const int mod = 1000000007;

int n, m;
int ans, cans;
int a[10];
string s[10];

void rec(int x) {
    if (x == n) {
        vector<vector<string> > v(m);
        for (int i = 0; i < n; i++) v[a[i]].push_back(s[i]);
        
        int cur = 0;
        for (int i = 0; i < m; i++) {
            sort(v[i].begin(), v[i].end());
            for (int j = 0; j < v[i].size(); j++) {
                cur += v[i][j].size() + 1;
                if (j) {
                    int k = 0;
                    while (k < v[i][j].size() && k < v[i][j - 1].size() && v[i][j][k] == v[i][j - 1][k]) k++;
                    cur -= k + 1;
                }
            }
        }
        if (ans < cur) ans = cur, cans = 0;
        if (ans == cur) cans++;
        return;
    }
    for (int i = 0; i < m; i++) {
        a[x] = i;
        rec(x + 1);
    }
}
 
int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

    int tests;
    cin >> tests;
    for (int test = 1; test <= tests; test++) {
        cout << "Case #" << test << ": ";

        cin >> n >> m;
        for (int i = 0; i < n; i++) cin >> s[i];
        ans = -1;
        rec(0);
        cout << ans << " " << cans << endl;
    }

	return 0;
}
