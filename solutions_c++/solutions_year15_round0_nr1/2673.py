// ================================================================================================
//  A - Standing Ovation.cpp
//  Written by Luis Garcia, 2015
// ================================================================================================

#include <cstdio>
#include <cstring>
#include <algorithm>
#include <set>
#include <map>
#include <vector>
#include <string>
#include <iterator>
#include <numeric>
#include <iostream>

using namespace std;

#if defined _OJ_PROJECT
_BEGIN_PROBLEM(_GCJ15_01A, "GCJ15 01A")
#endif // _OJ_PROJECT

#define infinite_loop for (;;)

int main() {
    int T, Smax;
    string S;
    cin >> T;

    for (int _T = 1; _T <= T; ++_T) {
        cin >> Smax >> S;

        int ans = 0, cur = 0;
        for (int i = 0; i <= Smax; ++i) {
            int t = S[i] - '0';
            if (t && cur < i) {
                ans += i - cur, cur += i - cur;
            }
            cur += t;
        }

        cout << "Case #" << _T << ": " << ans << endl;
    }

    return 0;
}

#if defined _OJ_PROJECT
_END_PROBLEM
#endif // _OJ_PROJECT

// ================================================================================================
//  End of file.
// ================================================================================================
