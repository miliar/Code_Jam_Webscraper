#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <utility>

using namespace std;

#define MAXN 1000002

int ReverseInt(int input)
{
    int ret_val=0;
    while (input != 0)
    {
        ret_val = (ret_val*10) + (input%10);
        input /= 10;
    }
    return ret_val;
}

int main()
{
    freopen ("A-small-attempt0.in","r",stdin);
    freopen ("A-small-attempt0.out","w",stdout);

    int cas, input, dp[MAXN];

    memset(dp, 0, sizeof(dp));

    scanf("%d", &cas);

    dp[1] = 1;

    for (int i = 2; i < MAXN; ++i)
    {
        int last = ReverseInt(i);
        //printf("%d %d\n", i, last);
		if (last >= i || i % 10 == 0)
		{
			dp[i] = dp[i-1] + 1;
		}
		else
		{
			dp[i] = min(dp[i-1], dp[last]) + 1;
		}
		//printf("dp[i]: %d\n", dp[i]);
    }

    for (int c = 1; c <= cas; ++c)
    {
        scanf("%d", &input);

        printf("Case #%d: %d\n", c, dp[input]);
    }

    return 0;
}
