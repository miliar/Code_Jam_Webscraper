#include <bits/stdc++.h>
using namespace std;

int main()
{
    int test, shy;
    char str[10000];

//    freopen("A-large.in", "r", stdin);
//    freopen("output.txt", "w", stdout);

    scanf("%d", &test);
    for (int t=1 ; t<=test ; t++)
    {
        scanf("%d %s", &shy, str);

        int getmax=0, extra=0;
        for (int i=0 ; i<=shy ; i++)
        {
            if (str[i]!='0' && i > getmax)
            {
                extra += (i-getmax);
                getmax += (i-getmax);
            }
            getmax += (str[i] - '0');

        }
        printf("Case #%d: %d\n", t, extra);
    }
    return 0;
}
