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
    int T, n;
    int frequencies[2501];
    scanf("%d", &T);
    for(int t=1; t <= T; ++t)
    {
        int tmp;
        scanf("%d", &n);
        memset(frequencies, 0, sizeof(int) * 2501);
        for(int i=(n << 1); i > 1; --i)
        {
            for(int j=0; j < n; ++j)
            {
                scanf("%d", &tmp);
                frequencies[tmp]++;
            }
        }

        printf("Case #%d:", t);
        for(int i=1; i <= 2500; ++i)
        {
            if(frequencies[i] % 2)
                printf(" %d", i);
        }
        printf("\n");
    }

    return 0;
}
