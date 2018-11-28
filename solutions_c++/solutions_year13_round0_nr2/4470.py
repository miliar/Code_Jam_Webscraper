#include <iostream>
#include <climits>
#include <cstdio>

using namespace std;

int T, n, m, v[200][200];

int main()
{
    cin >> T;

    for (int _ = 1; _ <= T; ++_) {
        cin >> n >> m;
        for (int i = 0; i < n; ++i)
            for (int j = 0; j < m; ++j)
                cin >> v[i][j];

        bool ok = true;
        while (n > 0 && m > 0) {
            int mi, mj, mm = INT_MAX;
            for (int i = 0; i < n; ++i)
                for (int j = 0; j < m; ++j)
                    if (v[i][j] < mm) {
                        mm = v[i][j];
                        mi = i;
                        mj = j;
                    }
            // if (_ == 45)
            //     printf("mi: %d mj: %d mm: %d\n", mi, mj, mm);
            bool finish = false;
            if (!finish) {
                bool flag = true;
                for (int i = 0; i < n; ++i)
                    if (v[i][mj] != mm)
                        flag = false;
                if (flag) {
                    finish = true;
                    for (int i = 0; i < n; ++i)
                        for (int j = mj; j < m-1; ++j)
                            v[i][j] = v[i][j+1];
                    --m;
                    // if (_ == 45) {
                    //     for (int i = 0; i < n; ++i) {
                    //         for (int j = 0; j < m; ++j)
                    //             printf("%4d ", v[i][j]);
                    //         puts("");
                    //     }
                    //     puts("");
                    // }
                }
            }
            if (!finish) {
                bool flag = true;
                for (int j = 0; j < m; ++j)
                    if (v[mi][j] != mm)
                        flag = false;
                if (flag) {
                    finish = true;
                    for (int i = mi; i < n-1; ++i)
                        for (int j = 0; j < m; ++j)
                            v[i][j] = v[i+1][j];
                    --n;
                    // if (_ == 45) {
                    //     for (int i = 0; i < n; ++i) {
                    //         for (int j = 0; j < m; ++j)
                    //             printf("%4d ", v[i][j]);
                    //         puts("");
                    //     }
                    //     puts("");
                    // }
                }
            }
            if (!finish) {
                ok = false;
                break;
            }
        }
        printf("Case #%d: %s\n", _, ok ? "YES" : "NO");
    }
}
