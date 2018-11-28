#include <iostream>
#include <algorithm>
#include <cassert>
using namespace std;
int n, m;
char ma[110][110];


void process(int case_id)
{
    cin >> n >> m;
    for (int i = 0 ; i < n ; ++i)
        cin >> ma[i];

    int ans = 0;
    
    for (int i = 0 ; i < n ; ++i)
        for (int j = 0 ; j < m ; ++j)
        {
            if (ma[i][j] != '.')
            {
                bool flag = false;
                int d;
                char directions[] = { '^' , 'v',  '<' , '>' };
                int delta[][2] = { {-1 , 0} , {1 , 0} , {0 , -1} , {0 , 1} };
                for (int k = 0 ; k < 4 ; ++k)
                    if (ma[i][j] == directions[k])
                    {
                        d = k;
                        break;
                    }
                int x = i + delta[d][0];
                int y = j + delta[d][1];
                while (x >= 0 && x < n && y >= 0 && y < m)
                {
                    if (ma[x][y] != '.')
                    {
                        flag = true;
                        break;
                    }
                    x += delta[d][0];
                    y += delta[d][1];
                }
                if (!flag)
                {
                    ++ans;
                    for (int k = 0 ; k < 4 ; ++k)
                    {
                        int x = i + delta[k][0];
                        int y = j + delta[k][1];
                        while (x >= 0 && x < n && y >= 0 && y < m)
                        {
                            if (ma[x][y] != '.')
                            {
                                flag = true;
                                break;
                            }
                            x += delta[k][0];
                            y += delta[k][1];
                        }
                    }
                    if (!flag)
                    {
                        cout << "Case #" << case_id << ": " << "IMPOSSIBLE" << endl;
                        return ;
                    }
                }
            }
        }

    cout << "Case #" << case_id << ": " << ans << endl;
}
int main()
{
    int t;
    cin >> t;
    for (int i = 1 ; i <= t ; ++i)
        process(i);
    return 0;
}