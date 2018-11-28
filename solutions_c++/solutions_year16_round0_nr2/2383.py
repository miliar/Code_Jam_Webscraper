#include <set>
#include <map>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <iostream>
#include <algorithm>

#define MaxN 110

using namespace std;

int T;

char str[MaxN];

int main() {
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    int T0 = 0;
    scanf("%d", &T);
    for ( ; T; --T) {
        scanf("%s", &str);
        int startsig = 0, num = 0, l = strlen(str);
        startsig = str[0] == '-' ? 1 : 0;
        for (int i = 1; i < l; ++i)
            if (str[i] != str[i - 1])
                ++num;
        printf("Case #%d: %d\n", ++T0, num + ((num & 1) ^ startsig));
    }
    return 0;
}
