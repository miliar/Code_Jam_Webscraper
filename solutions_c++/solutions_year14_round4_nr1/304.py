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


const int maxn = 1 << 15;
const int inf = 1000000007;
const int mod = 1000000007;

int n, x;
int a[maxn];
 
int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

    int tests;
    cin >> tests;
    for (int test = 1; test <= tests; test++) {
        cout << "Case #" << test << ": ";

        cin >> n >> x;
        for (int i = 0; i < n; i++) cin >> a[i];
        sort(a, a + n);
        vector<char> used(n);
        int ans = 0;
        for (int i = n - 1; i >= 0; i--) {
            if (used[i]) continue;
            int v = -1;
            for (int j = 0; a[j] + a[i] <= x && j < i; j++) {
                if (!used[j]) {
                    v = j;
                }
            }
            if (v != -1) used[v] = 1;
            ans++;
        }
        cout << ans << endl;
        cerr << test << endl;
    }

	return 0;
}
