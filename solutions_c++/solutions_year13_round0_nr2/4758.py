#include <vector>
#include <string>
#include <algorithm>
#include <list>
#include <set>
#include <queue>
#include <stack>
#include <sstream>
#include <numeric>
#include <functional>
#include <utility>
#include <bitset>
#include <iostream>
#include <cmath>
#include <map>
#include <cstring>
#include <cstdio>
#include <cassert>
#include <stdint.h>
#include <cstdarg>
#include <cstdio>
#include <fcntl.h>

using namespace std;

int a[110][110];

bool fr[130], fc[130];

int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    int _;
    scanf("%d\n", & _);
    for (int __ = 1; __ <= _; ++ __)
    {
        int n, m;
        scanf("%d%d\n", &n, &m);
        for (int i = 0; i < n; ++ i)
            for (int j = 0; j < m; ++ j)
                scanf("%d", a[i] + j);
        bool flag = 1;
        for (int k = 0; k <= 100; ++ k)
        {
            memset(fr, 0, sizeof(fr));
            memset(fc, 0, sizeof(fc));
            for (int i = 0; i < n; ++ i)
                for (int j = 0; j < m; ++ j)
                    if (a[i][j] > k)
                         fr[i] = 1, fc[j] = 1;
            for (int i = 0; i < n; ++ i)
                for (int j = 0; j < m; ++ j)
                    if (a[i][j] <= k)
                        if (fr[i] && fc[j])
                            flag = 0;
       }
       if (flag)
           printf("Case #%d: YES\n", __);
       else
           printf("Case #%d: NO\n", __);
       
    }
    fclose(stdout);
}



