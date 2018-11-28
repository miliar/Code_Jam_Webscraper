#include <iostream>
#include <vector>
#include <map>
#include <string>
#include <utility>
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cstring>

#define i 2
#define j 3
#define k 4

using namespace std;

int main(int argc, char const *argv[])
{
    int t, T;
    int L, X, LX, index, p, p_abs, m;
    char s[10001];
    vector<int> i_index, ij_index;
    bool possible;

    int prod[4][4] = {1, i, j, k,
                      i, -1, k, -j,
                      j, -k, -1, i,
                      k, j, -i, -1};

    cin >> T;

    for (t = 0; t < T; ++t) {
        possible = false;
        p = 1;
        i_index.clear();
        ij_index.clear();

        scanf("%d%d", &L, &X);
        scanf("%s", s);

        LX = L * X;

        for (m = 0; m < LX; ++m) {
            index = m % L;

            if (p > 0) {
                p = prod[p - 1][s[index] -'i' + i - 1];
            } else {
                p = -prod[-p - 1][s[index] -'i' + i - 1];
            }


            if (p == i) {
                i_index.push_back(m);
            } else if (p == k) {
                ij_index.push_back(m);
            }
        }

        if (p == -1) {
            if (!i_index.empty() && !ij_index.empty()) {
                if (i_index.front() < ij_index.back()) {
                    possible = true;
                }
            }
        }

        printf("Case #%d: %s\n", t + 1, possible ? "YES" : "NO");
    }

    return 0;
}
