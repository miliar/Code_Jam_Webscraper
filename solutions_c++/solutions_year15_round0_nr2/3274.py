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

    if (argc > 1) {
        freopen(argv[1], "r", stdin);
    }
    
    cin >> T;
    for (int cas = 1; cas <= T; cas++) {
        int D = 0;
        int P[1024] = {0};

        cin >> D;
        for (int i = 0; i < D; i++) {
            cin >> P[i];
        }

        sort(P, P + D);
        reverse(P, P + D);
        
        int res = P[0];

        for (int maxNum = 1; maxNum <= P[0]; maxNum++) {
            int t = 0;
            int m = -1;
            for (int i = 0; i < D; i++) {
                m = std::max(m, P[i]);
                m = std::min(m, maxNum);

                if (P[i] > maxNum) {
                    t += (P[i] - maxNum + (maxNum - 1)) / maxNum;
                }
            }

            res = std::min(res, t + m);
        }

        cout << "Case #" << cas << ": " << res << endl;
    }
    return 0;
}
