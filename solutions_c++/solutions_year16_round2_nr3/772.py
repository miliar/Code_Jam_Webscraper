#include <iostream>
#include <sstream>
#include <cmath>
#include <algorithm>
#include <string>
#include <string.h>
#include <cstdio>
#include <vector>
#include <map>
#include <set>
#include <cstring>
#include <queue>
#include <bitset>
#include <queue>
#include <unordered_map>


using namespace std;


int n;
string a[1001], b[1001];
unordered_map<string, int> m, m1;
bool f[1001];
int ans = 0;


void get(int i) {
    if (i == n) {
        bool t = 1;
        int cnt = 0;
        for (int j = 0; j < n; j++) {
            if (!f[j]) {
                if (m[a[j]] >= 1 && m1[b[j]] >= 1) {
                    cnt++;
                } else {
                    t = 0;
                    break;
                }
            }
        }
        ans = max(ans, t * cnt);
        return;
    }
    m[a[i]]++;
    m1[b[i]]++;
    f[i] = 1;
    get(i + 1);
    f[i] = 0;
    m[a[i]]--;
    m1[b[i]]--;    
    get(i + 1);
}


int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int tt;
    cin >> tt;
    for (int ii = 0; ii < tt; ii++) {
        cin >> n;
        for (int i = 0; i < n; i++) {
            cin >> a[i] >> b[i];
        }
        ans = 0;
        get(0);
        cout << "Case #" << ii + 1 << ": " << ans << endl;
    }
    return 0;
}
