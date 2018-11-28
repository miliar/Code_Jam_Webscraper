#include <stdio.h>
#include <string.h>
#include <string>
#include <iostream>

using namespace std;

char s[1010];
int main()
{
    int test;
    freopen("test.in", "r", stdin);
    freopen("test.out", "w", stdout);
    scanf("%d", &test);
    for (int t = 1; t <= test; t++)
    {
        scanf("%s", s);
        int len = strlen(s);
        //ans[0] = s[0];
        string ans(1, s[0]);
        for (int i = 1; i < len; i++)
        {
            if (s[i] >= ans[0])
                ans.insert(ans.begin(), s[i]);
            else
                ans.push_back(s[i]);
        }
        printf("Case #%d: ", t);
        cout << ans << endl;
    }

    return 0;
}
