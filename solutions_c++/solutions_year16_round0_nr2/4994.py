#include <stdio.h>

int t, ans;
char s[110];
bool st;

int main()
{
    freopen("/Users/IohcEjnim/Downloads/B-large.in.txt", "r", stdin);
    freopen("/Users/IohcEjnim/Downloads/result.txt", "w", stdout);
    int tn, i;
    scanf("%d", &t);
    for (tn = 1; tn <= t; tn++)
    {
        scanf("%s", s);
        ans = 0;
        st = (s[0] == '+');
        for (i = 0; s[i]; i++)
        {
            if (st != (s[i] == '+'))
            {
                ans++;
                st = (s[i] == '+');
            }
        }
        if (not st) ans++;
        printf("Case #%d: %d\n", tn, ans);
    }
}