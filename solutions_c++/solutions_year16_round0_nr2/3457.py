#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <cassert>

using namespace std;

int main()
{
//    freopen("input.txt", "r", stdin);
//    freopen("B-small-attempt0.in", "r", stdin);
    freopen("B-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);

    ios_base::sync_with_stdio(false);

    int T;
    cin >> T;
    for(int t = 1; t <= T; ++t)
    {
        string s;
        cin >> s;

        int ans = 0;
//        cout << s << endl;
        for(int i = s.length()-1; i >= 0; --i) {
            if(s[i] == '-') {
                ++ans;
                for(int j = 0; j <= i; ++j) {
                    if(s[j] == '+') {
                        s[j] = '-';
                    } else {
                        s[j] = '+';
                    }
                }
//                cout << s << endl;
            }
        }

        cout << "Case #" << t << ": ";
        cout << ans;
        cout << endl;
    }

    return 0;
}
