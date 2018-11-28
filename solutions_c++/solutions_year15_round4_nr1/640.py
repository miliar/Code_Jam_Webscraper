#include <iostream>
#include <string>
#include <map>
#include <vector>
#include <set>
#include <fstream>
#include <algorithm>
#include <cctype>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <functional>

using namespace std;

int main(int argc, char ** argv)
{

    int T;
    while (cin >> T)
    {
        for (int t = 1; t <= T; t++)
        {
            int n, m;
            cin >> n >> m;
            vector<vector<int> > a(n + 2, vector<int>(m + 2, 0));
            for (int i = 1; i <= n ; i++)
            {
                string str;
                cin >> str;
                for (int j = 1; j<=m; j++)
                    a[i][j] = (str[j - 1] == '^') * 1 +
                        (str[j - 1] == '>') * 2 +
                        (str[j - 1] == 'v') * 3 +
                        (str[j - 1] == '<') * 4;
            }
            for (int i = 1; i<= n; i++, clog << endl)
                for (int j = 1; j<=m; j++)
                    clog << a[i][j] << " ";
            vector<vector<int> > l(a), r(a), d(a), u(a);


            for (int i = 1; i <= n; i++)
                for (int j = 1; j<=m; j++)
                {
                    l[i][j] = l[i][j - 1] || a[i][j - 1];
                    u[i][j] = u[i - 1][j] || a[i - 1][j];
                }

            for (int i = n; i>= 1; i--)
                for (int j = m; j>= 1; j--)
                {
                    r[i][j] = r[i][j + 1] || a[i][j + 1];
                    d[i][j] = d[i + 1][j] || a[i + 1][j];
                }
            for (int i = 1; i <= n; i++, clog << endl)
                for (int j = 1; j<=m ; j++)
                    clog << u[i][j] << r[i][j] << d[i][j] << l[i][j] << ", " << endl;

            int ans = 0, re = 0;
            for (int i = 1; i<= n; i++)
                for (int j = 1; j<= m; j++)
                    if (a[i][j])
                    {
                        if (
                                (a[i][j] == 1 && u[i][j] == 0) || 
                                (a[i][j] == 2 && r[i][j] == 0) ||
                                (a[i][j] == 3 && d[i][j] == 0) ||
                                (a[i][j] == 4 && l[i][j] == 0))
                        {
                            ans += u[i][j] || r[i][j] || d[i][j] || l[i][j];
                            re += !(u[i][j] || r[i][j] || d[i][j] || l[i][j]);
                        }
                    }
            if (re)
                printf("Case #%d: IMPOSSIBLE\n", t);
            else
                printf("Case #%d: %d\n", t, ans);
        }
    }
    return 0;
}
