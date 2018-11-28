#include <iostream>
#include <stdio.h>

using namespace std;

int a[102][102], first[102][102];

int main()
{
    //freopen("two.in", "r", stdin);
    //freopen("two.out", "w", stdout);
    int i, j, n, m, t, T;
    cin >> T;
    for(t = 1; t <= T; t++)
    {
        cin >> n >> m;
        for(i = 0; i < n; i++)
            for(j = 0; j < m; j++)
            {
                cin >> a[i][j];
                first[i][j] = 100;
            }


        for(i = 0; i < n; i++)
        {
            int max = -1;
            for(j = 0; j < m; j++)
            {
                if(a[i][j] > max)
                    max = a[i][j];
            }
            for(j = 0; j < m; j++)
                first[i][j] = max;
        }

        for(j = 0; j < m; j++)
        {
            int max = -1;
            for(i = 0; i < n; i++)
            {
                if(a[i][j] > max)
                    max = a[i][j];
            }
            for(i = 0; i < n; i++)
                if(first[i][j] > max)
                    first[i][j] = max;
        }

        bool flag = true;
        for(i = 0; i < n; i++)
        {
            for(j = 0; j < m; j++)
            {
                if(first[i][j] != a[i][j])
                {
                    flag = false;   break;
                }
            }
            if(!flag)   break;
        }
        if(!flag)
            cout << "Case #" << t << ": NO\n";
        if(flag)
            cout << "Case #" << t << ": YES\n";
    }
    return 0;
}
