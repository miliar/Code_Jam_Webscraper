#include <bits/stdc++.h>

using namespace std;

int main()
{
    freopen("inp.in", "r", stdin);
    freopen("outp.out", "w", stdout);
    int tc;
    scanf("%d", &tc);
    for(int kras=1; kras<=tc; kras++)
    {
        printf("Case #%d: ", kras);
        //printf("\n");
        string s;
        cin >> s;
        string ans="";
        ans += s[0];
        for(int i=1; i<s.size(); i++)
        {
            if(s[i] >= ans[0])
            {
                reverse(ans.begin(), ans.end());
                ans += s[i];
                reverse(ans.begin(), ans.end());
            }
            else
            {
                ans += s[i];
            }
        }
        cout << ans << endl;
    }
    return 0;
}
