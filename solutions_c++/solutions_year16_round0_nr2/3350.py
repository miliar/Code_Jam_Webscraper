#include <bits/stdc++.h>
using namespace std;
char s[107];
void go(int len)
{
    for (int i = 1; i <= len; i++)
    {
        if (s[i] == '-')
        {
            s[i] = '+';
        }
        else
        {
            s[i] = '-';
        }
    }
    reverse(s + 1, s + 1 + len);
}
int main()
{
    freopen("b.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    int t;
    scanf("%d", &t);
    for (int tt = 1; tt <= t; tt++)
    {
        scanf("%s", s);
        int n = strlen(s);
        for (int i = n; i >= 1; i--)
        {
            s[i] = s[i - 1];
        }
        int ans = 0;
        while(1)
        {
            int r = n;
            while (r > 0 && s[r] == '+') r--;
            if (r == 0) break;
            if (s[1] == '+')
            {
                int l = 1;
                while (l <= n && s[l] == '+') l++;
                go(l - 1);
                ans++;
            }
            else
            {
                go(r);
                ans++;
            }
        }
        printf("Case #%d: %d\n", tt, ans);
        cerr << tt << endl;
    }
}
