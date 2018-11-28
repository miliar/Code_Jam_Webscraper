#include <iostream>
#include <stdio.h>

using namespace std;

int n, ans;
string str;

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    cin >> n;
    for (int i = 1; i <= n; i++) {
        cin >> str;
        ans = 0;
        for (int j = 0; j < str.size(); j++)
            if (j + 1 < str.size() && str[j] != str[j + 1])
                ++ans;
        if (str[str.size() - 1] == '-')
            ++ans;
        printf("Case #%d: %d\n", i, ans);
    }
    return 0;
}
