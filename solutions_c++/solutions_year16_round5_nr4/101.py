#include <bits/stdc++.h>
using namespace std;

int t;

int n, l;

string dob[107];
string zle;

int main()
{
    cin >> t;
    for (int tt=1; tt<=t; tt++)
    {
        printf("Case #%d: ", tt);
        cin >> n >> l;
        for (int i=1; i<=n; i++)
        {
            cin >> dob[i];
        }
        cin >> zle;
        int czy=0;
        for (int i=1; i<=n; i++)
        {
            if (dob[i]==zle)
            {
                czy=1;
            }
        }
        if (czy)
        {
            printf("IMPOSSIBLE\n");
            continue;
        }
        if (l==1)
        {
            printf("0? 00\n");
            continue;
        }

        for (int i=1; i<=min(l, 30); i++)
        printf("01");
        printf("0?");
        for (int i=1; i<=min(l, 30); i++)
        printf("01");

        printf(" ");

        for (int i=1; i<l; i++)
        printf("?");
        printf("\n");
    }
    return 0;
}
