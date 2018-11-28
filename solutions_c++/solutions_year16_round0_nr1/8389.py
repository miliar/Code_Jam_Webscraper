#include <iostream>
#include <cmath>
#include <vector>
#include <stdlib.h>
#include <cstdio>
#include <ctime>
#include <map>

using namespace std;

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("A_large_ans.txt", "w", stdout);

    int T;
    scanf("%d", &T);
    for (int test = 1; test <= T; test++) {
        int val;
        scanf("%d", &val);
        if (val == 0) {
            printf("Case #%d: INSOMNIA\n", test);
            continue;
        }
        int cnt = 0;
        bool used[10];
        for (int i = 0; i < 10; i++) used[i] = false;

        long long m = val;
        while (true) {
            long long mcp = m;
            while (mcp > 0) {
                if (used[mcp%10] == false) {
                    used[mcp%10] = true;
                    cnt++;
                }
                mcp /= 10;
            }

            if (cnt == 10) {
                printf("Case #%d: %I64d\n", test, m);
                break;
            }

            m += val;
        }
    }


    return 0;
}

