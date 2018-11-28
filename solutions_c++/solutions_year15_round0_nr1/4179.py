#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <vector>
#include <map>
#include <set>
#include <algorithm>

using namespace std;

#define MAXS 1003

int main()
{
    freopen ("A-large.in","r",stdin);
    freopen ("A-large.out","w",stdout);

    int cas, S, s_now, clap_num, ans;
    char str[MAXS], last;

    scanf("%d", &cas);
    for (int c = 1; c <= cas; ++c)
    {
        scanf("%d%s", &s_now, str);

        last = str[0];
        clap_num = str[0]-'0';
        ans = 0;

        for (int i = 1; i < strlen(str); ++i)
        {
            if (str[i] != '0' && clap_num < i)
            {
                ans += (i-clap_num);
                clap_num = i;
            }
            clap_num += (str[i]-'0');
        }

        printf("Case #%d: %d\n", c, ans);
    }

    return 0;
}
