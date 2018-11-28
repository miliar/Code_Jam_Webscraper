#include<iostream>
#include<cstdio>
#include<cmath>
#include<algorithm>

using namespace std;

const int N = 100;
int us[N];

int main()
{
    freopen("a.in", "r", stdin);
    freopen("a.out", "w", stdout);
    int t;
    int n = 4;
    int a;
    cin >> t;
    for (int k = 1; k <= t; k++)
{
    for (int i = 0; i <= 16; i++)
        us[i] = false;
    int x1, x2;
    cin >> x1;
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            cin >> a;
            if (x1 == i + 1)
                us[a] = true;
        }
    }
    cin >> x2;
    int ans = -1;
    int fl = 0;
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++)
        {
            cin >> a;
            if (fl == 1)
                continue;
            if (i + 1 == x2)
                if (us[a])
                    if (ans == -1)
                      ans = a;
                    else
                    {
                        fl = 1;
                    }
        }
    cout << "Case #" << k << ": ";
    if (fl == 1)
    {
        cout << "Bad magician!" << endl;
        continue;
    }
    if (ans == -1)
    {
        cout << "Volunteer cheated!" << endl;
    }
    else
    {
        cout << ans << endl;
    }
}
}
