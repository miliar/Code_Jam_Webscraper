#include <iostream>
#include <string>

using namespace std;

int main() {
        int T;
        cin >> T;
        for (int casenum = 1; casenum <= T; ++casenum) {
                int smax;
                string str;
                cin >> smax >> str;
                int ans = 0, cur = 0;
                for (int i = 0; i <= smax; ++i) {
                        if (cur < i) {
                                ans += (i - cur);
                                cur = i;
                        }
                        cur += (str[i] - '0');
                }
                cout << "Case #" << casenum << ": " << ans << endl;
        }
        return 0;
}
