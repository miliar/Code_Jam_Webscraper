#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cfloat>
#include <climits>
#include <cstring>
#include <string>
#include <vector>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
#define ARBLIMIT 1000
using namespace std;

int main()
{
    int k, c, s, T;
    scanf("%d", &T);
    for(int t=1; t <= T; ++t)
    {
        scanf("%d%d%d", &k, &c, &s);
        printf("Case #%d:", t);
        if(k - c >= s)
            printf(" IMPOSSIBLE");
        else
            for(int i=1; i <= s; ++i)
                printf(" %d", i);
        printf("\n");
    }

    return 0;
}
