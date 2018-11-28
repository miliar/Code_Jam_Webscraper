/// This code is a pure govnocode
#include <bits/stdc++.h>
#define DEBUG(x) cout << #x << " = " << x << endl;
using namespace std;
const int MAXN = 10005;

int ans[MAXN][3];

void generateWin(int W, int ansIdx, int tl, int tr)
{
    if (tl == tr)
    {
        ans[tl][ansIdx] = W;
    }
    else
    {
        int mid = (tl + tr) / 2;

        if (W == 0)
        {
            generateWin(0, ansIdx, tl, mid);
            generateWin(1, ansIdx, mid + 1, tr);
        }

        if (W == 1)
        {
            generateWin(1, ansIdx, tl, mid);
            generateWin(2, ansIdx, mid + 1, tr);
        }

        if (W == 2)
        {
            generateWin(0, ansIdx, tl, mid);
            generateWin(2, ansIdx, mid + 1, tr);
        }

        int pntL = tl;
        int pntR = mid + 1;
        while(ans[pntL][ansIdx] == ans[pntR][ansIdx])
        {
            pntL++;
            pntR++;
        }

        if (ans[pntR][ansIdx] < ans[pntL][ansIdx])
        {
            pntL = tl;
            pntR = mid + 1;
            while(pntL < mid + 1)
            {
                swap(ans[pntL][ansIdx], ans[pntR][ansIdx]);
                pntL++;
                pntR++;
            }
        }

    }
}

int main()
{
    freopen("inputA.in", "r", stdin);
    freopen("outputA.out", "w", stdout);

    int _T;
    cin >> _T;

    for (int _t = 1; _t <= _T; _t++)
    {
        int P, R, S;
        int N;
        cin >> N >> R >> P >> S;
        int M = (1 << N);

        generateWin(0, 0, 1, M);
        generateWin(1, 1, 1, M);
        generateWin(2, 2, 1, M);

        int x = -1;
        for (int idx = 0; idx < 3; idx++)
        {
            int RR = 0, PP = 0, SS = 00;
            for (int i = 1; i <= M; i++)
            {
                if (ans[i][idx] == 0) PP++;
                if (ans[i][idx] == 1) RR++;
                if (ans[i][idx] == 2) SS++;
            }

            if (RR == R && PP == P && SS == S)
            {
                x = idx;
            }
        }

        cout << "Case #" << _t << ": ";
        if (x == -1)
        {
            cout << "IMPOSSIBLE" << endl;
        }
        else
        {
            for (int i = 1; i <= M; i++)
            {
                if (ans[i][x] == 0) cout << 'P';
                if (ans[i][x] == 1) cout << 'R';
                if (ans[i][x] == 2) cout << 'S';
            }
            cout << endl;
        }
    }

    return 0;
}
