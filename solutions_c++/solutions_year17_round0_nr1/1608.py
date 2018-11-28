//#pragma warning (disable: 4786)
//#pragma comment (linker, "/STACK:16777216")
//HEAD
//include <bits/stdc++.h>
#include <cstdio>
#include <ctime>
#include <cstdlib>
#include <cstring>
#include <queue>
#include <string>
#include <set>
#include <stack>
#include <map>
#include <cmath>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

typedef long long LL;
typedef unsigned long long ULL;

const int maxn = 10010;

char str[maxn];
int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int T;
    int ncase = 1;
    int n, k;
    scanf("%d", &T);
    while (T--) {
        scanf("%s %d", str, &k);
        n = strlen(str);
        int cnt = 0;
        for (int i = 0; i < n - k + 1; i++) {
            if (str[i] == '-')
            {
                for (int j = i; j < i + k; j++) {
                    if (str[j] == '-') str[j] = '+';
                    else if (str[j] == '+') str[j] = '-';
                }
                cnt++;
            }
        }
        int flag = 1;
        for (int i = n - k + 1; i < n; i++) {
            if (str[i] == '-') {
                flag = 0;
            }
        }
        if (flag) {
            printf("Case #%d: %d\n", ncase++, cnt);
        } else {
            printf("Case #%d: IMPOSSIBLE\n", ncase++);
        }
    }
    return 0;
}


