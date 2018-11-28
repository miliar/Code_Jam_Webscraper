#include <iostream>
#include <string.h>

using namespace std;

const long long mod = 1000 * 1000 * 1000 + 7;

char s[1024][128];
int c[1024];

int n, m;
int nodes, ways;

void f(int i)
{
    if (i == m)
    {
        for (int j=0; j<n; j++)
        {
            for (i=0; i<m; i++)
                if (c[i] == j)
                    break;
            if (i == m)
                return;
        }

        int cur = n;

        for (i=0; i<m; i++)
        {
            int k = 0;

            for (int j=0; j<i; j++)
                if (c[i] == c[j])
                {
                    int t;
                    for (t=0; s[i] && s[i][t] == s[j][t]; t++);
                    k = max(t, k);
                }

            cur += strlen(s[i]) - k;
        }

//        cout << cur << " " << c[0] << " " << c[1] << " " << c[2] << " " << c[3] << endl;

        if (nodes < cur)
        {
            nodes = cur;
            ways = 0;
        }

        ways += nodes == cur;

        return;
    }

    for (c[i] = 0; c[i] < n; c[i]++)
        f(i+1);
}

int main()
{
    int t;
    cin >> t;
    for (int tt=1; tt<=t; tt++)
    {
        nodes = 0;
        ways = 0;
        cin >> m >> n;
        for (int i=0; i<m; i++)
            cin >> s[i];

        f(0);

        cout << "Case #" << tt << ": " << nodes << " " << ways << endl;
    }
    return 0;
}
