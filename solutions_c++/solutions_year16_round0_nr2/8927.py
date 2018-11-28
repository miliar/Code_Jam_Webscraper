#include <iostream>
#include <cstdio>
#include <string>
#include <cstring>
#include <vector>
using namespace std;
string s;
int a[100];
int main()
{
    freopen("B-large.in", "rt", stdin);
    freopen("output.txt", "wt", stdout);
    int t;
    cin >> t;
    for(int i = 0; i < t;i++)
    {
        int ans = 0;
        cin >> s;
        for(int j = 0;j < s.length();j++)
            if (s[j] == '-')
                a[j] = 2;
            else
                a[j] = 1;
        while(true)
        {
            int b = -1;
            for(int j = s.length() - 1;j >= 0;j--)
            {
                if (a[j] == 2)
                {
                    b = j;
                    break;
                }
            }
            if (b == -1) break;
            ans++;
            if (b == 0)
                break;
            for(int j = 0;j <= b;j++)
            {
                int l = a[b - j];
                a[b - j] = a[j];
                a[j] = l;
            }
            for(int j = 0;j <= b;j++)
            {
                if (a[j] == 2)
                    a[j] = 1;
                else
                    a[j] = 2;
            }
        }
        cout << "Case #" << i + 1 << ": " << ans << endl;
    }
    return 0;
}
