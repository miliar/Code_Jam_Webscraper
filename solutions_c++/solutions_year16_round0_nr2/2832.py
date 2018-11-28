#include <iostream>
#include <vector>
#include <map>
#include <string>
#include <utility>
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>

using namespace std;

int main(int argc, char const *argv[])
{
    int t, T;

    cin >> T;

    for (t = 1; t <= T; ++t) {
        int ans = 0;
        bool lastMinus = false;
        string pancake;
        char c, lastC;

        cin >> pancake;

        int n = pancake.size();

        for (int i = 0; i < n; ++i) {
            c = pancake[i];

            if (i == 0 || lastC != c) {
                ans++;
                lastC = c;
            }
        }

        if (pancake[n - 1] == '+') {
            ans--;
        }


        printf("Case #%d: %d\n", t, ans);
    }

    return 0;
}
