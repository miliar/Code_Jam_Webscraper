#include <bits/stdc++.h>
using namespace std;

bool p[200];
char s[200];

int main()
{
    int T;
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    cin >> T;
    for (int K = 1; K <= T; K++)
    {
        cout << "Case #" << K << ": ";

        cin >> s;
        int l = strlen(s);
        for (int i = 0; i < l; i++)
            p[i] = s[i] == '+';

        int ans = 0;
        for (int i = l - 1; i >= 0; i--)
        {
            if (p[i] == 0)
            {
                ans++;
                for (int j = 0; j <= i; j++)
                    p[j] = !p[j];
            }
        }
        cout << ans << endl;
    }
    return 0;
}
