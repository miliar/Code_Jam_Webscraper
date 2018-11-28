#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <deque>
#include <algorithm>

using namespace std;

int main()
{
    int n, t, a, b, K, res, tmp;

    scanf("%d", &t);

    for(int k = 1; k <= t; ++k)
    {

        scanf("%d%d%d", &a, &b, &K);

        res = 0;
        for(int i=0; i < a; ++i)
        {
            for(int j=0; j < b; ++j)
            {
                tmp = i & j;
                if(0 <= tmp && tmp < K )
                    res++;
            }
        }

        printf("Case #%d: %d\n", k, res);
    }

    return 0;    
}
