#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <vector>
#include <map>
#include <set>
#include <algorithm>

using namespace std;
#define MAXS 102

int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);

    int T, cas, index, ans;
    char str[MAXS];
    bool firstFlip;
    scanf("%d", &T);

    for (cas = 1; cas <= T; ++cas)
    {
        memset(str, 0, sizeof(str));
        scanf("%s", str);
        index = 0;
        firstFlip = false;
        ans = 0;
        while (index < (int)strlen(str))
        {
            if (str[index] == '-')
            {
                while (index + 1 < (int)strlen(str))
                {
                    if (str[index+1] == '-')
                    {
                        ++index;
                    }
                    else
                    {
                        if (firstFlip == false)
                        {
                            ++ans;
                        }
                        else
                        {
                            ans += 2;
                        }
                        break;
                    }
                }
                if (index == (int)strlen(str)-1)
                {
                    if (firstFlip == false)
                    {
                        ++ans;
                    }
                    else
                    {
                        ans += 2;
                    }
                }
            }

            firstFlip = true;
            ++index;
        }
        printf("Case #%d: %d\n", cas, ans);
    }
    return 0;
}
