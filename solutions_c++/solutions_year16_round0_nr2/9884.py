/// This code is a pure govnocode
#include <bits/stdc++.h>
#define DEBUG(x) cout << #x << " = " << x << endl;
using namespace std;
const int MAXN = 10;
const int MAXS = (1 << MAXN) + 1;

int Q[MAXS], dist[MAXS];
int mask[MAXN + 1];

int Reverse(int x, int N)
{
    int y = 0;
    for (int i = 0; i < N; i++)
    {
        y = (2 * y) + (x % 2);
        x /= 2;
    }
    return y;
}

int main()
{
    freopen("input.in", "r", stdin);
    freopen("output.out", "w", stdout);

    int T;
    cin >> T;

    mask[1] = 1;
    for (int i = 2; i <= MAXN; i++)
    {
        mask[i] = 2 * mask[i - 1] + 1;
    }

    string s;
    getline(cin, s);
    for (int _t = 0; _t < T; _t++)
    {
        getline(cin, s);
        int N = s.size();

        int exp = 1;
        int state = 0;
        for (int i = 0; i < N; i++)
        {
            if (s[i] == '-')
            {
                state ^= exp;
            }
            exp *= 2;
        }

        for (int i = 0; i < (1 << N); i++)
        {
            dist[i] = -1;
        }

        Q[1] = state;
        dist[state] = 0;
        int l = 1, r = 1;

        while(Q[l] != 0)
        {
            //DEBUG(state);
            int state = Q[l];
            for (int i = 1; i <= N; i++)
            {
                int top = state & mask[i];
                top = Reverse(top, i);
                top ^= mask[i];
                int newState = (state & (mask[N] - mask[i])) ^ top;
                //DEBUG(newState);

                if (dist[newState] == -1)
                {
                    r++;
                    Q[r] = newState;
                    dist[newState] = dist[state] + 1;
                }
            }
            l++;
        }

        cout << "Case #" << _t + 1 << ": " << dist[0] << endl;
    }

    return 0;
}
