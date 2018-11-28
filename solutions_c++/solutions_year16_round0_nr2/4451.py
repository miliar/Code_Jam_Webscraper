#include <bits/stdc++.h>
using namespace std;
int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    int t;
    scanf("%d",&t);
    for(int cas = 1; cas <= t; cas++)
    {
        char s[110];
        scanf("%s",s);
        int len = strlen(s);
        int ans = 0;
        for(int i = 0; i < len - 1; i++)
        {
            if(s[i] != s[i + 1]) ans++;
        }
        if(s[len - 1] != '+') ans++;
        printf("Case #%d: %d\n",cas,ans);
    }
    return 0;
}
