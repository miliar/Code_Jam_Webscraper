#include <fstream>
#include <sstream>
#include <iostream>
#include <string>
#include <set>
#include <cstdlib>
#include <deque>

using namespace std;

int main()
{
    freopen("input.in", "r", stdin);
    freopen("output.out", "w", stdout);

    int n;
    cin >> n;

    for (int i = 1; i <= n; ++i) {
        string s;
        deque<char> res;
        cin >> s;
        for (int j = 0; j < s.size(); ++j) {
            char ch = s[j];
            if (res.empty()) {
                res.push_back(ch);
            }
            else {
                if (ch >= res[0]) {
                    res.push_front(ch);
                }
                else {
                    res.push_back(ch);
                }
            }
        }
        string res_str(res.begin(), res.end());
        cout << "Case #" << i << ": " << res_str << endl;
    }

    return 0;
}
