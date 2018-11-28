#include <iostream>
#include <cstdio>

using namespace std;

int main()
{
    freopen("in", "r", stdin);
    freopen("out", "w", stdout);
    int tt;
    scanf("%d", &tt);
    for (int qq = 1; qq <= tt; qq++)
    {
        printf("Case #%d: ", qq);
        int n;
        scanf("%d", &n);
        char s[1024];
        scanf("%s", &s);
        
        int ret = 0;
        int ctr = 0;
        for (int i = 0; i < n+1; i++)
        {
            if (s[i] - '0' > 0 && ctr < i)
            {
                ret += (i - ctr);
                ctr += (i-ctr);
            }
            ctr += (s[i] - '0');
        }
        printf("%d\n", ret);

    }
    return 0;
}
