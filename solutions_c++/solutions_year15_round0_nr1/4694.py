#include <iostream>
#include <string.h>
#include <stdio.h>
using namespace std;

int main()
{
    freopen("stuff.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    int t, n, p = 0, ans = 0, aud[1000] = {0}, c;
    bool g;
    char x;
    cin >> t;
    c = t;
    while(t--)
    {
        cin >> n;
        p = 0;
        ans = 0;
        fill(aud, aud + 1000, 0);
        for(int i = 0; i <= n; i++)
        {
            cin >> x;
            aud[i] += x - '0';
        }
        while(true)
        {
            g = true;
            for(int i = 0; i <= n; i++)
            {
                if(p >= i)
                {
                    p += aud[i];
                    aud[i] = 0;
                }
                if(aud[i] != 0)
                    g = false;
            }
            if(g)
                break;
            else
            {
                aud[0]++;
                ans++;
            }
        }
        cout << "Case #" << (c - t) << ": " << ans << endl;
    }
    return 0;
}
