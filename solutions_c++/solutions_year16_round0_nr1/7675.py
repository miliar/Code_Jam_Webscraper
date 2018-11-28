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
        int n;
        cin >> n;
        cout << "Case #" << i + 1 << ": ";
        if (n == 0) {
            cout << "INSOMNIA" << endl;
            continue;
        }
        vector<int> m(10, 0);
        int k = 0;
        long long s = 0;
        while (k < 10) {
            s += n;
            long long t = s;
            while (t > 0) {
                if (m[t % 10] == 0) {
                    m[t % 10] = 1;
                    k++;
                }
                t /= 10;
            }
        }
        cout << s << endl;
    }

    return 0;

}
