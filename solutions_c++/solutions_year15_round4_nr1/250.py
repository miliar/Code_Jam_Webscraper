#include <cstdio>
#include <iostream>
using namespace std;
char street[101][101];
int main()
{
    int t;
    scanf("%d", &t);
    int cs=0;
    while (t--)
    {
        int r, c;
        scanf("%d%d", &r, &c);
        for (int i=0; i<r; i++)
        {
            scanf("%s", street[i]);
        }
        int ans=0;
        bool fail=false;
        for (int i=0; i<r; i++)
        {
            for (int j=0; j<c; j++)
            {
                if ('.'==street[i][j]) continue;
                bool legal=false;
                if ('>'==street[i][j])
                {
                    for (int k=j+1; k<c; k++) if ('.'!=street[i][k]) legal=true;
                }
                if ('<'==street[i][j])
                {
                    for (int k=0; k<j; k++) if ('.'!=street[i][k]) legal=true;
                }
                if ('^'==street[i][j])
                {
                    for (int k=0; k<i; k++) if ('.'!=street[k][j]) legal=true;
                }
                if ('v'==street[i][j])
                {
                    for (int k=i+1; k<r; k++) if ('.'!=street[k][j]) legal=true;
                }
                if (legal) continue;
                legal=false;
                for (int k=j+1; k<c; k++) if ('.'!=street[i][k]) legal=true;
                for (int k=0; k<j; k++) if ('.'!=street[i][k]) legal=true;
                for (int k=0; k<i; k++) if ('.'!=street[k][j]) legal=true;
                for (int k=i+1; k<r; k++) if ('.'!=street[k][j]) legal=true;
                if (legal)
                {
                    ans++;
                    continue;
                }
                fail=true;
            }
        }
        printf("Case #%d: ", ++cs);
        if (fail) printf("IMPOSSIBLE\n");
        else printf("%d\n", ans);
    }
    return 0;
}
