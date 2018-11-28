#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <algorithm>

using namespace std;

int T;
int n, x;

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    cin >> T;
    for (int t = 1; t <= T; ++t) {
        cin >> n;
        string ans = "";

        if (n == 2) {
            int a, b;
            cin >> a >> b;
            while (a != b) {
                if (a > b) {
                    ans += " A", --a;
                } else {
                    ans += " B", --b;
                }
            }
            while (a) {
                ans += " AB", --a;
            }
        } else {
            set <pair <int, int> > cnt;
            for (int i = 0; i < n; ++i) {
                cin >> x;
                cnt.insert(make_pair(-x, i));
            }

            while (cnt.size() && (cnt.begin()->first != -1 || (cnt.begin()->first == -1 && cnt.size() > 2))) {
                pair<int, int> a = *cnt.begin();
                ans.push_back(' ');
                ans.push_back((char) ('A' + a.second));

                cnt.erase(cnt.begin());
                if (a.first != -1) {
                    cnt.insert(make_pair(a.first + 1, a.second));
                }
            }

            pair<int, int> a = *cnt.begin();
            cnt.erase(cnt.begin());
            pair<int, int> b = *cnt.begin();
            cnt.erase(cnt.begin());

            ans.push_back(' ');
            ans.push_back(char('A' + a.second));
            ans.push_back(char('A' + b.second));
        }
        cout << "Case #" << t << ":" << ans << endl;
    }

    return 0;
}