#include <bits/stdc++.h>

typedef long long int64;
#define sz(A) (int((A).size()))

using namespace std;

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);

    int T;
    cin >> T;

    vector <vector <string> > A(200, vector <string>(200));
    A['1']['1'] = "1";
    A['1']['i'] = "i";
    A['1']['j'] = "j";
    A['1']['k'] = "k";
    A['i']['1'] = "i";
    A['i']['i'] = "-1";
    A['i']['j'] = "k";
    A['i']['k'] = "-j";
    A['j']['1'] = "j";
    A['j']['i'] = "-k";
    A['j']['j'] = "-1";
    A['j']['k'] = "i";
    A['k']['1'] = "k";
    A['k']['i'] = "j";
    A['k']['j'] = "-i";
    A['k']['k'] = "-1";

    for (int tst = 0; tst < T; tst++)
    {
        int n;
        int64 x;
        string s;
        cin >> n >> x >> s;
        char now = '1';
        int sign = 1, pos1 = -1, pos2 = -1;

        for (int i = 0; i < min(n * x, n * 5LL); i++)
        {
            string st = A[now][s[i % n]];

            if (st[0] == '-')
            {
                sign = -sign;
                now = st[1];
            }
            else
                now = st[0];

            if (now == 'i' && sign == 1)
            {
                pos1 = i;
                break;
            }
        }
        now = '1', sign = 1;

        for (int i = 0; i < min(n * x, n * 5LL); i++)
        {
            string st = A[s[n - i % n - 1]][now];

            if (st[0] == '-')
            {
                sign = -sign;
                now = st[1];
            }
            else
                now = st[0];

            if (now == 'k' && sign == 1)
            {
                pos2 = i;
                break;
            }
        }
        
        if (pos1 != -1 && pos2 != -1 && pos1 + pos2 <= n * x - 2)
        {
            now = '1', sign = 1;

            for (int i = 0; i < n; i++)
            {
                string st = A[now][s[i]];

                if (st[0] == '-')
                {
                    sign = -sign;
                    now = st[1];
                }
                else
                    now = st[0];
            }
            char all = '1';
            int allsign = 1;

            for (int i = 0; i < x % 4; i++)
            {
                string st = A[all][now];

                if (st[0] == '-')
                {
                    allsign = -allsign;
                    all = st[1];
                }
                else
                    all = st[0];
                allsign *= sign;
            }

            if (all == '1' && allsign == -1)
                cout << "Case #" << tst + 1 << ": YES\n";
            else
                cout << "Case #" << tst + 1 << ": NO\n";
        }
        else
            cout << "Case #" << tst + 1 << ": NO\n";
    }

    return 0;
}
