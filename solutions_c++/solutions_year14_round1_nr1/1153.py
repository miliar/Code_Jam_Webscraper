#include <set>
#include <map>
#include <ctime>
#include <cstdio>
#include <vector>
#include <string>
#include <climits>
#include <cstdlib>
#include <cstddef>
#include <sstream>
#include <string.h>
#include <iostream>
#include <algorithm>

using namespace std;

#define LL long long

template <typename T> T sqr(T x) { return x * x; }
template <typename T> T abs(T x) { return x < 0 ? -x : x; }

string f[200], flow[200], d[200];
int main()
{
//*
    freopen("in", "r", stdin);
    freopen("out2", "w", stdout);
//*/
    int TESTS;
    scanf("%d\n", &TESTS);
    for (int tests = 1; tests <= TESTS; tests++)
    {
        int n, l;
        cin >> n >> l;
        for (int i = 0; i < n; i++)
            cin >> flow[i];
        for (int i = 0; i < n; i++)
            cin >> d[i];
        sort(d, d + n);
        int Min = (int) 1e9;
        bool nice = false;
        for (int j = 0; j < n; j++)
        {
            for (int i = 0; i < n; i++)
                f[i] = flow[i];
            int cnt = 0;
            for (int i = 0; i < l; i++)
                if (f[j][i] != d[0][i])
                {
                    cnt += 1;
                    for (int k = 0; k < n; k++)
                        if (f[k][i] == '0')
                            f[k][i] = '1';
                        else
                            f[k][i] = '0';
                }
            sort(f, f + n);
            bool good = true;
            for (int i = 0; i < n; i++)
                if (d[i] != f[i])
                {
                    good = false;
                    break;
                }
            if (good)
                Min = min(Min, cnt);
            nice |= good;
        }
        printf("Case #%d: ", tests);
        if (nice)
            cout << Min << endl;
        else
            puts("NOT POSSIBLE");
    }
    return 0;
}
