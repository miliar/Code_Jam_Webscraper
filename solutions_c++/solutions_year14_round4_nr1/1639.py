#include <iostream>
#include <fstream>
#include <cstdio>
#include <iomanip>
#include <cassert>
#include <climits>
#include <cmath>
#include <ctime>
#include <vector>
#include <string>
#include <cstring>
#include <queue>
#include <deque>
#include <time.h>
#include <stack>
#include <map>
#include <set>
#include <functional>
#include <algorithm>
#include <bitset>

//#pragma comment(linker, "/STACK:256000000")

using namespace std;


int main() {
#ifdef MYLOCAL
    freopen("//home//maks//code//input.txt", "rt", stdin);
    freopen("//home//maks//code//output.txt", "wt", stdout);
    clock_t beginTime = clock();
#endif

    int test = 0;
    cin >> test;

    for (int tes = 0; tes < test; ++tes) {
        int n, s, ans = 0;
        vector<int> azaza;
        cin >> n >> s;
        azaza.resize(n);
        for (int i = 0; i < n; ++i) {
            cin >> azaza[i];
        }
        sort(azaza.begin(), azaza.end());
        while (!azaza.empty()) {
            if (azaza.size() == 1) {
                ans++;
                break;
            }
            else {
                int val = azaza[azaza.size() - 1];
                azaza.pop_back();
                auto it = upper_bound(azaza.begin(), azaza.end(), s - val);
                if (it == azaza.begin()) {
                    ans++;
                }
                else {
                    ans++;
                    azaza.erase(--it);
                }
            }
        }
        cout << "Case #" << tes + 1 << ": " << ans << '\n';
    }

#ifdef MYLOCAL
    cout << endl << "time: " << double(clock() - beginTime) / CLOCKS_PER_SEC << '\n';
#endif

    return 0;
}
