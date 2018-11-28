#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <cctype>
#include <climits>
#include <iostream>
#include <vector>
#include <queue>
#include <string>
#include <stack>
#include <map>
#include <set>
#include <unordered_map>
#include <unordered_set>
#include <algorithm>
#include <sstream>
#include <initializer_list>

using namespace std;

int main(int argc, char *argv[])
{
    int T = 0;
    int mx = 0;

    if (argc > 1) {
        freopen(argv[1], "r", stdin);
    }
    
    cin >> T;
    for (int cas = 1; cas <= T; cas++) {
        string s;
        cin >> mx;
        cin >> s;

        long long res = 0, acc = 0;
        for (int i = 0; i < s.size(); i++) {
            if (acc < i) {
                long long add = i - acc;
                res += add;
                acc += add;
            }

            acc += s[i] - '0';
        }

        cout << "Case #" << cas << ": " << res << endl;
    }

    return 0;
}
