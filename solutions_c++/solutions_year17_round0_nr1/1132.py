#include <iostream>
#include <cstdio>

using namespace std;

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);

    int T;
    cin >> T;

    for(int ct = 1; ct <= T; ct++)
    {
        string s;
        int k;
        cin >> s >> k;

        int ans = 0, n = s.size();
        for(int i = 0; i <= n-k; i++)
            if(s[i] == '-')
            {
                ans++;
                for(int j = 0; j < k; j++)
                    s[i+j] = (s[i+j] == '-')?'+':'-';
            }

        bool imp = false;
        for(int i = 0; i < n; i++)
            if(s[i] != '+')
                imp = true;

        if(imp)
            printf("Case #%d: IMPOSSIBLE\n", ct);
        else
            printf("Case #%d: %d\n", ct, ans);
    }

    return 0;
}
