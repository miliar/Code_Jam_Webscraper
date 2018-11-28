#include<iostream>
#include<cstring>
#include<string>
#include<cstdio>
using namespace std;

int T, len, kase = 0;
char s[1005], ans[3005];

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    cin >> T;
    while (T--)
    {
        scanf("%s", s);
        len = strlen(s);
        int i, t = 1500;
        ans[t] = s[0];
        for (i = 1; i < len; i++)
            if (s[i] < ans[t]) ans[t + i] = s[i];
            else
            {
                t--;
                ans[t] = s[i];
            }
        ans[t + len] = '\0';
        printf("Case #%d: %s\n", ++kase, ans + t);
    }
    fclose(stdin);
    fclose(stdout);
    return 0;
}
