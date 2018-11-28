#include <iostream>
#include <cmath>
#include <vector>
#include <memory.h>
#include <map>
#include <set>
#include <cstdio>
#include <algorithm>
#include <cstdlib>
#include <ctime>
#include <string>

using namespace std;

const int DEBUG = 1;

int a[10005];
bool used[10005];
int n, x, t;

int main()
{
    if (DEBUG) {
        freopen("input.txt","r",stdin);
        freopen("output.txt","w",stdout);
    }
    cin >> t;
    int number = 0;
    while (t--) {
        cin >> n >> x;
        ++number;

        for (int i = 0; i < n; ++i) cin >> a[i];
        cout << "Case #" << number << ": ";
        sort(a, a + n);
        memset(used, false, sizeof(used));
        int j = n - 1;
        int ans = 0;
        for (int i = 0; i < n; ++i) {
            if (used[i]) continue;
            ++ans;
            used[i] = true;
            while (j >= 0 && (used[j] || a[j] > x - a[i])) --j;
            if (j > 0) {
                used[j] = true;
            }
        }
        cout << ans << endl;
    }
    return 0;
};

