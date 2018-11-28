#include <iostream>
#include <cstdio>
using namespace std;
int main()
{   int t;
    freopen("output.txt", "w", stdout);
    cin >> t;
    for (int kase = 1; kase <= t; kase++)
    {   int n;
        cin >> n;
        string s;
        cin >> s;
        int ans = 0, cur = 0;
        for (int i = 0; i <= n; i++)
        {    if (cur >= i)
                cur += s[i] - '0';
            else
            {   ans += i - cur;
                cur = i;
                cur += s[i] - '0';
            }
        }
        cout << "Case #" << kase << ": "<<ans << endl;
    }
    fclose(stdout);
    return 0;
}
