#include <bits/stdc++.h>
using namespace std;


bool p[20];

int main()
{
    int T;
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    cin >> T;
    for (int K = 1; K <= T; K++)
    {
        cout << "Case #" << K << ": ";

        int a = 0, b, cnt = 0, t;
        cin >> b;
        if (b == 0)
        {
            cout << "INSOMNIA" << endl;
            continue;
        }
        for (int i = 0; i <= 9; i++)
            p[i] = 0;
        while (cnt < 10)
        {
            a += b;
            t = a;
            while (t > 0)
            {
                if (p[t % 10] == 0)
                {
                    p[t % 10] = 1;
                    cnt++;
                }
                t = t / 10;
            }
        }
        cout << a << endl;
    }
    return 0;
}
