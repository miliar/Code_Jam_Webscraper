#include <bits/stdc++.h>
using namespace std;

int T;
int n, p, r, s;

int a[100000];

void polish(int l, int r)
{
    if (l == r)
        return;
    int mid = (l + r) / 2;
    polish(l, mid);
    polish(mid + 1, r);
    bool work = false;
    for (int i = 0; i <= mid - l; i++)
        if (a[l + i] > a[mid + 1 + i])
        {
            work = true;
            break;
        }
    if (work)
    {
        for (int i = 0; i <= mid - l; i++)
            swap(a[l + i], a[mid + 1 + i]);
    }
}

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);

    cin >> T;
    for (int K = 1; K <= T; K++)
    {
        cin >> n >> r >> p >> s;
        cout << "Case #" << K << ": ";
        int k = 1;
        for (int i = 1; i <= n; i++)
            k = k * 2;
        k = k - 1;
        bool found = false;
        for (int i = 1; i <= 3; i++)
        {
            a[1] = i;
            for (int l = 1; l <= k; l++)
            {
                if (a[l] == 1)
                {
                    a[l * 2] = 1;
                    a[l * 2 + 1] = 2;
                }
                else if (a[l] == 2)
                {
                    if (l * 2 + 1 <= k)
                    {
                        a[l * 2] = 3;
                        a[l * 2 + 1] = 2;
                    }
                    else
                    {
                        a[l * 2] = 2;
                        a[l * 2 + 1] = 3;
                    }
                }
                else if (a[l] == 3)
                {
                    a[l * 2] = 1;
                    a[l * 2 + 1] = 3;
                }
            }
            int x = 0, y = 0, z = 0;
            for (int l = k + 1; l <= 2 * k + 1; l++)
            {
                if (a[l] == 1)
                    x++;
                else if (a[l] == 2)
                    y++;
                else
                    z++;
            }
            if (x == p && y == r && z == s)
            {
                found = true;
                break;
            }
        }
        if (found)
        {
            polish(k + 1, 2 * k + 1);
            for (int l = k + 1; l <= 2 * k + 1; l++)
                if (a[l] == 1)
                    cout << "P";
                else if (a[l] == 2)
                    cout << "R";
                else
                    cout << "S";
            cout << endl;
        }
        else
            cout << "IMPOSSIBLE" << endl;
    }
    return 0;
}
