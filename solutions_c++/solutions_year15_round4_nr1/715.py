#include <iostream>
#include <string>

std::string s[100];
int r, c;

bool leave(int ii, int jj, int di, int dj)
{
    ii += di;
    jj += dj;
    while (ii >= 0 && ii < r && jj >= 0 && jj < c
        && s[ii][jj] == '.')
    {
        ii += di;
        jj += dj;
    }
    return !(ii >= 0 && ii < r && jj >= 0 && jj < c);
}

int main()
{
    int T;
    std::cin >> T;
    for (int t = 1 ; t <= T ; ++t)
    {
        std::cin >> r >> c;
        std::getline(std::cin, s[0]);
        for (int i = 0 ; i < r ; ++i)
            std::getline(std::cin, s[i]);
        int res = 0;
        for (int i = 0 ; res >= 0 && i < r ; ++i)
            for (int j = 0 ; res >= 0 && j < c ; ++j)
                if (s[i][j] != '.')
                {
                    int dj = s[i][j] == '<' ? -1 : s[i][j] == '>' ? 1 : 0;
                    int di = s[i][j] == '^' ? -1 : s[i][j] == 'v' ? 1 : 0;
                    if (leave(i, j, di, dj))
                    {
                        int di[4] = {1, -1, 0, 0};
                        int dj[4] = {0, 0, -1, 1};
                        bool ok = false;
                        for (int d = 0 ; d < 4 ; ++d)
                            if (!leave(i, j, di[d], dj[d]))
                                ok = true;
                        if (ok)
                            ++res;
                        else
                            res = -1;
                    }
                }
        std::cout << "Case #" << t << ": ";
        if (res == -1)
            std::cout << "IMPOSSIBLE";
        else
            std::cout << res;
        std::cout << "\n";
    }
    return 0;
}

