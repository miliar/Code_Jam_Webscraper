#include <iostream>
#include <vector>

#include <assert.h>
#include <stdio.h>

using namespace std;

enum class cell
{
    empty,
    up,
    down,
    left,
    right
};

int
calc_updates (const vector< vector<cell> > & cells, int D1, int D2, cell dir1, cell dir2)
{
    int answer = 0;

    return answer;
}

int main()
{
    freopen ("input.txt", "rb", stdin);
    freopen ("output.txt", "wb", stdout);

    int T;
    cin >> T;
    for(int i = 0; i < T; i++)
    {
        cout << "Case #" << (i + 1) << ": ";

        int R, C;
        cin >> R >> C;

        vector< vector<cell> > cells;
        vector<int> count_by_row (R);
        vector<int> count_by_column (C);

        // cout << endl;
        for (int i = 0; i < R; i++)
        {
            std::string s;
            cin >> s;
            // cout << s << endl;
            cells.push_back(vector<cell> (C, cell::empty));

            for (int j = 0; j < C; j++)
            {
                switch (s[j])
                {
                case '^':
                    cells[i][j] = cell::up;
                    break;
                case 'v':
                    cells[i][j] = cell::down;
                    break;
                case '<':
                    cells[i][j] = cell::left;
                    break;
                case '>':
                    cells[i][j] = cell::right;
                    break;
                }

                if (cells[i][j] != cell::empty)
                {
                    count_by_row[i]++;
                    count_by_column[j]++;
                }
            }
        }

        int answer = 0;

        for (int i = 0; i < R && answer != -1; i++)
        {
            for (int j = 0; j < C; j++)
            {
                if (cells[i][j] != cell::empty)
                {
                    if (count_by_row[i] == 1
                        && count_by_column[j] == 1)
                    {
                        answer = -1;
                        break;
                    }
                }
            }
        }

        if (answer == -1)
        {
            cout << "IMPOSSIBLE" << std::endl;

            /* to the next test case */
            continue;
        }

        assert (answer == 0);

        for (int i = 0; i < R; i++)
        {
            int j1;
            for (j1 = 0; j1 < C; j1++)
            {
                if (cells[i][j1] != cell::empty)
                {
                    if (cells[i][j1] == cell::left)
                    {
                        answer++;
                    }
                    else
                    {
                        j1--;
                    }

                    break;
                }
            }

            int j2;
            for (j2 = C - 1; j2 > j1; j2--)
            {
                if (cells[i][j2] != cell::empty)
                {
                    if (cells[i][j2] == cell::right)
                    {
                        answer++;
                    }

                    break;
                }
            }
        }
        for (int i = 0; i < C; i++)
        {
            int j1;
            for (j1 = 0; j1 < R; j1++)
            {
                if (cells[j1][i] != cell::empty)
                {
                    if (cells[j1][i] == cell::up)
                    {
                        answer++;
                    }
                    else
                    {
                        j1--;
                    }

                    break;
                }
            }

            int j2;
            for (j2 = R - 1; j2 > j1; j2--)
            {
                if (cells[j2][i] != cell::empty)
                {
                    if (cells[j2][i] == cell::down)
                    {
                        answer++;
                    }

                    break;
                }
            }
        }

        cout << answer << endl;
    }

    fclose (stdin);
    fclose (stdout);

    return 0;
}
