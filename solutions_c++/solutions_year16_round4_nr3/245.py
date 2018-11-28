/* Google Code Jam Round 2 2016
 * Problem C. The Gardener of Seville
 * Solution in C++
 * By Smithers
 */

#include <cstdio>
#include <string>
#include <vector>

int getCoords(int r, int c, int i, int & x, int & y)
{
    if (i < c)
    {
        x = 2 * i + 1;
        y = 0;
        return 0;
    }
    else if (i < r + c)
    {
        x = 2 * c;
        y = 2 * (i - c) + 1;
        return 1;
    }
    else if (i < r + 2 * c)
    {
        x = 2 * (r + 2 * c - i) - 1;
        y = 2 * r;
        return 2;
    }
    else
    {
        x = 0;
        y = 2 * (2 * r + 2 * c - i) - 1;
        return 3;
    }
}

int main()
{
    int t;
    
    std::scanf("%d ", &t);
    for (int x = 1; x <= t; x++)
    {
        int r, c;
        
        std::scanf("%d%d", &r, &c);
        std::vector<int> lover(2 * (r + c), 0);
        for (int i = 0; i < r + c; ++i)
        {
            int j, k;
            std::scanf("%d%d", &j, &k);
            lover[j-1] = k-1;
            lover[k-1] = j-1;
        }
        
        bool possible = true;
        std::vector<std::string> garden(r, std::string(c, ' '));
        for (int i = 0; i < 2 * (r + c); ++i)
        {
            if (lover[i] > i)
            {
                continue;
            }
            
            int curX, curY, tgtX, tgtY;
            int dir = getCoords(r, c, i, curX, curY);
            getCoords(r, c, lover[i], tgtX, tgtY);
            do
            {
                switch (dir)
                {
                case 0:
                    if (garden[curY / 2][curX / 2] == '\\')
                    {
                        ++curX;
                        ++curY;
                        dir = 3;
                    }
                    else
                    {
                        garden[curY / 2][curX / 2] = '/';
                        --curX;
                        ++curY;
                        dir = 1;
                    }
                    break;
                case 1:
                    if (garden[curY / 2][curX / 2 - 1] == '/')
                    {
                        --curX;
                        ++curY;
                        dir = 0;
                    }
                    else
                    {
                        garden[curY / 2][curX / 2 - 1] = '\\';
                        --curX;
                        --curY;
                        dir = 2;
                    }
                    break;
                case 2:
                    if (garden[curY / 2 - 1][curX / 2] == '\\')
                    {
                        --curX;
                        --curY;
                        dir = 1;
                    }
                    else
                    {
                        garden[curY / 2 - 1][curX / 2] = '/';
                        ++curX;
                        --curY;
                        dir = 3;
                    }
                    break;
                case 3:
                    if (garden[curY / 2][curX / 2] == '/')
                    {
                        ++curX;
                        --curY;
                        dir = 2;
                    }
                    else
                    {
                        garden[curY / 2][curX / 2] = '\\';
                        ++curX;
                        ++curY;
                        dir = 0;
                    }
                    break;
                }
            } while (curX != 0 && curX != 2 * c && curY != 0 && curY != 2 * r);
            if (curX != tgtX || curY != tgtY)
            {
                possible = false;
                break;
            }
        }
        
        std::printf("Case #%d:\n", x);
        if (possible)
        {
            for (int i = 0; i < r; ++i)
            {
                for (int j = 0; j < c; ++j)
                {
                    if (garden[i][j] == ' ')
                        garden[i][j] = '/';
                }
                std::printf("%s\n", garden[i].c_str());
            }
        }
        else
        {
            std::printf("IMPOSSIBLE\n");
        }
    }
    return 0;
}
