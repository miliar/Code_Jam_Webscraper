// ================================================================================================
//  GCJ053C.cpp
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
_BEGIN_PROBLEM(_GCJ15_03C, "GCJ15 03C")
#endif // _OJ_PROJECT

#define infinite_loop for (;;)

int main() {
    char A[20000];

    int T, N;
    sscanf(gets(A), "%d", &T);

    for (int _T = 1; _T <= T; ++_T) {
        sscanf(gets(A), "%d", &N);

        vector<int> cA, cB;
        int cD[3000], cDl = 0, cC[30][3000], cCl[30] = {};

        map<string, int> mp;
        auto f = [&mp](const string & a) {
            if (mp.find(a) == mp.end()) {
                int t = mp.size();
                mp[a] = t;
                return t;
            } else
                return mp[a];
        };

        auto sortAndUnique = [](vector<int> & t) {
            sort(t.begin(), t.end());
            t.erase(unique(t.begin(), t.end()), t.end());
        };
        
        auto sortAndUnique2 = [](int * t, int & s) {
            sort(t, t + s);
            s = unique(t, t + s) - t;
        };

        gets(A);
        for (char * psz = strtok(A, " "); psz; psz = strtok(NULL, " "))
            cA.push_back(f(psz));
        sortAndUnique(cA);

        gets(A);
        for (char * psz = strtok(A, " "); psz; psz = strtok(NULL, " "))
            cB.push_back(f(psz));
        sortAndUnique(cB);

        for (int i = 0; i < N - 2; ++i) {
            gets(A);
            for (char * psz = strtok(A, " "); psz; psz = strtok(NULL, " ")) {
                int k = f(psz);
                cD[cDl++] = k;
                cC[i][cCl[i]++] = k;
            }
            sortAndUnique2(cC[i], cCl[i]);
        }
        sortAndUnique2(cD, cDl);

        int w = mp.size();
        char cH[3000] = {};
        for (int i = 0; i < cA.size(); ++i) cH[cA[i]] |= 1;
        for (int i = 0; i < cB.size(); ++i) cH[cB[i]] |= 2;

        int ans = 100000000;
        for (int i = 0, _N = (1 << (N - 2)); i < _N; ++i) {
            char H[3000];
            memcpy(H, cH, sizeof H);

            for (int h = 0; h < N - 2; ++h)
                for (int j = 0; j < cDl; ++j)
                    if (binary_search(cC[h], cC[h] + cCl[h], cD[j]))
                        H[cD[j]] |= ((1 << h) & i) ? 2 : 1;
            ans = min(ans, count(H, H + w, 3));
        }

        printf("Case #%d: %d\n", _T, ans);
    }

    return 0;
}

#if defined _OJ_PROJECT
_END_PROBLEM
#endif // _OJ_PROJECT

// ================================================================================================
//  End of file.
// ================================================================================================
