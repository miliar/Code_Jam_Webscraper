#include <bits/stdc++.h>

using namespace std;

#define xx first
#define yy second
#define pb push_back

int tc;
char s[111];

int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("AAA.out", "w", stdout);
    cin >> tc;
    int tt = 0;
    while(tc--)
    {
        scanf("%s", s);
        if(strlen(s) == 1)
        {
            if(s[0] == '+')
            {
                printf("Case #%d: 0\n", ++tt);
            }
            else
            {
                printf("Case #%d: 1\n", ++tt);
            }
            continue;
        }
        int ans = 0;
        for(int i = 1; s[i]; i++)
        {
            if(s[i] != s[i - 1])
            {
                ans++;
            }
        }
        if(s[strlen(s) - 1] == '-')
        {
            ans++;
        }
        printf("Case #%d: %d\n", ++tt, ans);
    }
    return 0;
}
