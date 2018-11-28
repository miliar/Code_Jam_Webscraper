#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <iomanip>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <algorithm>

#define F first
#define S second
#define pb push_back
#define mp make_pair

using namespace std;

const int INF = 1000000009;
const int MOD = 1000000007;

int main() {

    ios_base::sync_with_stdio(0);

#ifdef DEBUG
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#else
    //freopen("vacation.in", "r", stdin);
    //freopen("vacation.out", "w", stdout);
#endif // DEBUG


    int t;
    cin >> t;

    for (int i = 0; i < t; ++i) {
        string s;
        cin >> s;
        s += "+";
        cout << "Case #" << i + 1 << ": ";
        int ans = 0;
        for (int j = 1; j < s.size(); ++j) {
            if (s[j] != s[j - 1])
                ans++;
        }
        cout << ans << endl;
    }

    return 0;

}
