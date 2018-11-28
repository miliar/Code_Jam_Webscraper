#include <iostream>
#include <cstdio>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int t;
    cin >> t;
    for (int j = 0; j < t; j++)
    {
        int n;
        cin >> n;
        string s;
        cin >> s;
        int result = 0;
        int prev = 0;
        for (int i = 0; i <= n; i++)
        {
            int p = s[i] - '0';
            if (p == 0) continue;
            if (prev < i)
            {
                result += i - prev;
                prev = i;
            }
            prev += p;
        }

        cout << "Case #" << j + 1 << ": " << result << "\n";
    }
    return 0;
}
