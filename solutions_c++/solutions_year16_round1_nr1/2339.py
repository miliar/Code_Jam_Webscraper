#include <iostream>
#include <vector>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    int t;
    cin >> t;
    for (int testCase = 0; testCase < t; ++testCase) {
        string s;
        cin >> s;
        string ans;
        for (char c: s) {
            if (ans.empty()) {
                ans = c;
            } else {
                if (c > ans[0]) {
                    ans = c + ans;
                } else if (c < ans[0]) {
                    ans = ans + c;
                } else {
                    bool f = false;
                    for (char t: ans) {
                        if (c < t) {
                            f = false;
                            break;
                        } else if (c > t) {
                            f = true;
                            break;
                        }
                    }
                    if (f) {
                        ans = c + ans;
                    } else {
                        ans = ans + c;
                    }
                }
            }
        }
        cout << "Case #" << testCase + 1 << ": " << ans;
        cout << endl;
    }
    return 0;
}
