#include <cstdio>
#include <cstdlib>
#include <iostream>
using namespace std;

int main()
{
    freopen("a.in", "r",stdin);
    int t;
    cin >> t;
    for (unsigned int idx = 0; idx < t; idx++)
    {
        int n;
        string ch;
        int total = 0;
        int ans = 0;
        cin >> n >> ch;
        for (int i = 0; i < n + 1; i++)
        {
            int k = (int)ch[i] - '0';
            if (i > total)
            {
                int add = i - total;
                ans += add;
                total += add;
            }
            total += k;
        }
        cout << "Case #" << idx + 1 << ": " << ans << endl;
    }
    return 0;
}
