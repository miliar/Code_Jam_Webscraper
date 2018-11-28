#include <iostream>
using namespace std;

int main()
{
    int maxtime, time;
    cin >> maxtime;
    const int maxn = 110;
    int n, m, h[maxn][maxn], m1[maxn], m2[maxn], i, j;

    for (time = 1; time <= maxtime; time++)
    {
        cin >> n >> m;
        for (i = 0; i < n; i++) {
            for (j = 0; j < m; j++) {
                cin >> h[i][j];
            }
        }

        for (i = 0; i < n; i++) {
            m1[i] = 0;
            for (j = 0; j < m; j++) {
                if (m1[i] < h[i][j])
                    m1[i] = h[i][j];
            }
        }
        for (j = 0; j < m; j++) {
            m2[j] = 0;
            for (i = 0; i < n; i++) {
                if (m2[j] < h[i][j])
                    m2[j] = h[i][j];
            }
        }

        bool able = true;
        for (i = 0; i < n; i++) {
            for (j = 0; j < m; j++) {
                if (h[i][j] != min (m1[i], m2[j]))
                    able = false;
            }
        }

        cout << "Case #" << time << ": ";
        if (able)
            cout << "YES" << endl;
        else
            cout << "NO" << endl;
    }
    return 0;
}

