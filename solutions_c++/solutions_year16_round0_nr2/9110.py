#include <iostream>
#include <cstdio>
#include <string>
using namespace std;
int d[200];
int buf[200];

int main()
{
    freopen("B-large.in", "rt", stdin);
    freopen("output.txt", "wt", stdout);
    int t;
    cin >> t;
    for (int i = 0; i < t; i++)
    {
        int ans = 0;
        string s;
        cin >> s;
        for (int j = 0; j < s.length(); j++)
        {
            if (s[j] == '-')
            {
                d[j] = 1;
            }
            else
            {
                d[j] = 2;
            }
        }
        for (int j = s.length() - 1; j >= 0; j--)
        {
            if (d[j] == 1)
            {
                for (int k = 0; k <= j; k++)
                {
                    int g = d[k];
                    d[k] = d[j - k];
                    d[j - k] = g;
                }
                for (int k = 0;k <= j; k++)
                {
                    if (d[k] == 1)
                    {
                        d[k] = 2;
                    }
                    else
                    {
                        d[k] = 1;
                    }
                }

                ans++;
            }
        }
        cout << "Case #" << i + 1 << ": " << ans << endl;
    }
    return 0;
}
