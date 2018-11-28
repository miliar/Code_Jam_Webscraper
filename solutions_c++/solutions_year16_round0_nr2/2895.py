#include <stdint.h>
#include <iostream>
#include <sstream>
#include <vector>
#include <stack>
#include <queue>
#include <map>
#include <set>
#include <unordered_map>
#include <unordered_set>
#include <algorithm>

using namespace std;

int main()
{
    int T;
    string S;
    cin >> T;
    for (int i = 1; i <= T; ++i) {
        cin >> S; int l, r = S.length() - 1;
        int count = 0;
        
        while (true) {
            // remove tailing +
            while (r >= 0 && S[r] == '+') --r;
            // flip heading +
            bool flip = false;
            l = 0;
            while (r >= l && S[l] == '+') {
                S[l++] = '-'; flip = true;
            }
            if (flip) ++count;

            int l2 = 0, r2 = r; flip = false;
            while (l2 <= r2) {
                char c = S[l2];
                S[l2] = S[r2] == '+' ? '-' : '+';
                S[r2] = c == '+' ? '-' : '+';
                ++l2; --r2;
                flip = true;
            }
            if (flip) ++count;

            if (r < 0) break;
        }

        cout << "Case #" << i << ": " << count << endl;
    }
    return 0;
}