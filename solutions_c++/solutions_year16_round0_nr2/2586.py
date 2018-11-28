#include <stdio.h>
#include <string.h>
#include <algorithm>

using namespace std;

int main()
{
    int t, tt;
    scanf("%d", &t);

    for (tt = 1; tt <= t; ++ tt)
    {
        char moo[105];
        scanf("%s", moo);
        int l = strlen(moo);
        int ans = 0;
        moo[l] = '+';

        for (int i = l - 1; i >= 0; -- i)
        {
            if (moo[i] != moo[i + 1])
            {
                ++ ans;
/*                if (i) std::reverse(moo, moo + i - 1);
                for (int j = 0; j < i; ++ j)
                {
                    moo[j] = '+' + '-' - moo[j];
                }*/
            }
        }
        printf("Case #%d: %d\n", tt, ans);
    }

    return 0;
}
