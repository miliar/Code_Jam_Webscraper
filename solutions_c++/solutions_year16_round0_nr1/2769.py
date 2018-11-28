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
        int N, multiN, mod, ans = 0;
        int notSeen = (1 << 10) - 1;

        cin >> N;

        if (N == 0) {
            printf("Case #%d: INSOMNIA\n", t);
            continue;
        }

        while (notSeen) {
            multiN = ans + N;
            ans = multiN;

            while (multiN) {
                mod = multiN % 10;
                notSeen &= ~(1 << mod);
                multiN = multiN / 10;
            }
        }

        printf("Case #%d: %d\n", t, ans);
    }

    return 0;
}
