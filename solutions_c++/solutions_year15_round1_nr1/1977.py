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
    int N;
    int m[10000];
    int ans1, ans2, diff_max, diff;

    cin >> T;

    for (t = 1; t <= T; ++t) {
        cin >> N;
        ans1 = 0;
        ans2 = 0;
        diff_max = 0;

        for (int i = 0; i < N; ++i) {
            cin >> m[i];

            if (i > 0) {
                diff = m[i - 1] - m[i];

                if (diff > 0) {
                    ans1 += diff;
                }

                if (diff > diff_max) {
                    diff_max = diff;
                }
            }
        }

        for (int i = 0; i < N - 1; ++i) {
            ans2 += min(m[i], diff_max);
        }

        printf("Case #%d: %d %d\n", t, ans1, ans2);
    }

    return 0;
}
