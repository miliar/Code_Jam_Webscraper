#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <algorithm>
#include <set>
#include <vector>
#include <cstring>
#include <string>
#include <map>
#include <iomanip>
using namespace std;

#define ALEXEY_HOME

int main() {
#ifdef ALEXEY_HOME
    freopen("input.txt", "rt", stdin);
    freopen("output.txt", "wt", stdout);
#endif

    ios_base::sync_with_stdio(false);

    int test; cin >> test;
    for (int t = 1; t <= test; t++) {
        int n; cin >> n;
        int x; cin >> x;
        vector<int> v;
        for (int i = 0; i < n; i++) {
            int num; cin >> num;
            v.push_back(num);
        }
        sort(v.begin(), v.end());
        int l = 0, r = v.size() - 1;
        int answer = 0;
        while (r >= l) {
            answer++;
            if (l == r) break;
            if (x >= v[l] + v[r]) {
                l++;
                r--;
            }
            else {
                r--;
            }
        }
        cout << "Case #" << t << ": " << answer << endl;
    }

    return 0;
}
