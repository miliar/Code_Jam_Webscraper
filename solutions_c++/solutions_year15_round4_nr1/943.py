#include <iostream>
#include <algorithm>
#include <vector>
#include <fstream>
#include <string>

using namespace std;

int main()
{
    freopen("input.txt", "r",stdin);
    freopen("output.txt", "w",stdout);
    int T;
    cin >> T;
    for (int z = 0; z < T; ++z)
    {
        int R, C;
        cin >> R >> C;
        int ans = 0;
        int A[R + 2][C + 2];
        vector <vector <int> > B(R + 2);
        vector <vector <int> > D(C + 2);
        for (int i = 1; i <= R; ++i)
        {
            for (int j = 1; j <= C; ++j)
            {
                char c;
                cin >> c;
                A[i][j] = 0;
                if (c != '.')
                {
                    if (c == '^')
                    {
                        A[i][j] = 1;
                    }
                    if (c == '>')
                    {
                        A[i][j] = 2;
                    }
                    if (c == 'v')
                    {
                        A[i][j] = 3;
                    }
                    if (c == '<')
                    {
                        A[i][j] = 4;
                    }
                    B[i].push_back(j);
                    D[j].push_back(i);
                }
            }
        }
        int q = 0;
        int p = 0;
        for (int i = 1; i <= R; ++i)
        {
            if (B[i].size() == 1)
            {
                q = B[i][0];
                if (D[q].size() == 1)
                {
                    p = 1;
                }
            }
            stable_sort(B[i].begin(), B[i].end());
        }
        for (int j = 1; j <= C; ++j)
        {
            stable_sort(D[j].begin(), D[j].end());
        }
        if (p == 1)
        {
            cout << "Case #" << z + 1 << ": " << "IMPOSSIBLE" << endl;
        }
        else
        {
            for (int i = 1; i <= R; ++i)
            {
                for (int j = 0; j < B[i].size(); ++j)
                {
                    int a = B[i][j];

                    int q = 0;
                    if (A[i][a] == 1)
                    {


                        for (int k = 0; k < D[a].size(); ++k)
                        {

                            if (D[a][k] == i)
                            {
                                q = k;
                                break;
                            }
                        }
                        if (q == 0)
                        {
                            ++ans;
                        }
                    }
                    if (A[i][a] == 2)
                    {
                        if (j == B[i].size() - 1)
                        {
                            ++ans;
                        }
                    }
                    if (A[i][a] == 3)
                    {
                        for (int k = 0; k < D[a].size(); ++k)
                        {
                            if (D[a][k] == i)
                            {
                                q = k;
                                break;
                            }

                        }
                        if (q == D[a].size() - 1)
                        {
                            ++ans;
                        }
                    }
                    if (A[i][a] == 4)
                    {
                        if (j == 0)
                        {
                            ++ans;
                        }
                    }






                }
            }
            cout << "Case #" << z + 1 << ": " << ans << endl;
        }
    }
    return 0;
}
