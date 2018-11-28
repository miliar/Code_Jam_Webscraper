#include <iostream>
#include <vector>
#include <map>
#include <string>
#include <utility>
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cstring>

using namespace std;

int main(int argc, char const *argv[])
{
    int t, T;

    cin >> T;

    for (t = 0; t < T; ++t) {
        int s_max, ans = 0, up = 0;
        cin >> s_max;

        char s[s_max + 2];
        scanf("%s", s);

        for (int i = 0; i < s_max + 1; ++i) {
            if (up < i) {
                ans += i - up;
                up = i;
            }

            up += s[i] - '0';
        }

        printf("Case #%d: %d\n", t + 1, ans);
    }

    return 0;
}
