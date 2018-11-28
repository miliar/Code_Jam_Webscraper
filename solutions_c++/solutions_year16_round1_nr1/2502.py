#include <bits/stdc++.h>

using namespace std;

int main()
{
    //freopen("A-large.in", "r", stdin);
    //freopen("A-large.out", "w", stdout);
    int tc;
    scanf("%d", &tc);
    for (int nc = 1; nc <= tc; nc++)
    {
        string s;
        cin >> s;
        printf("Case #%d: ", nc);
        vector<char> res;
        res.push_back(s[0]);
        for (int i = 1; i < s.size(); i++)
        {
            if (s[i] >= res[0])
            {
                res.insert(res.begin(), s[i]);
            }
            else
            {
                res.push_back(s[i]);
            }
        }
        for (auto it = res.begin(); it != res.end(); it++)
            printf("%c", *it);
        printf("\n");
    }
}
