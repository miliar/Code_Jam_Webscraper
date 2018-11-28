#include <iostream>
#include <string>
#include <cstdlib>
#include <cstdio>

using namespace std;

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int t;
    scanf("%d", &t);
    for(int i = 1; i <= t; ++i)
    {
        int s_max;
        char s[1005];
        scanf("%d%s", &s_max, s);
        int sum = s[0] - '0';
        int max_diff = 0;
        for(int j = 1; j <= s_max; ++j)
        {
            if(j - sum > max_diff) max_diff = j - sum;
            sum += s[j] - '0';
        }
        printf("Case #%d: %d\n", i, max_diff);
    }
    return 0;
}
