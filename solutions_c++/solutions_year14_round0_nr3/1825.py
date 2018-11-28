#include <iostream>
#include <cstdlib>
#include <fstream>
#include <utility>
#include <vector>

using namespace std;

ifstream lire("input.in", ios::in);
ofstream ecrire("output.txt", ios::out);

int mat[50][50];
bool continu;
int nb, obj;
int R, C, M;

void test(int x, int y)
{
    if (!continu or nb > obj)
        return;
    if (nb == obj)
    {
        continu = false;
        for (int i = 0; i < R; i++)
        {
            for (int j = 0; j < C; j++)
                if (mat[i][j] == 1)
                    ecrire << 'c';
                else if (mat[i][j] == 2)
                    ecrire << '.';
                else
                    ecrire << '*';
            ecrire << endl;
        }
        return;
    }
    vector< pair<int,int> > l;
    for (int i = -1; i <= 1; i++)
        for (int j = -1; j <= 1; j++)
            if (x + i >= 0 and x + i < R and y + j >= 0 and y + j < C and mat[x + i][y + j] == 0)
            {
                nb++;
                mat[x + i][y + j] = 2;
                l.push_back(make_pair(x + i, y + j));
            }
    for (int i = 0; i < l.size(); i++)
        test(l[i].first, l[i].second);
    for (int i = 0; i < l.size(); i++)
    {
        nb--;
        mat[l[i].first][l[i].second] = 0;
    }
    return;
}

int main()
{
    int T;
    int m[50][50];
    lire >> T;
    for (int k = 1; k <= T; k++)
    {
        lire >> R >> C >> M;
        ecrire << "Case #" << k << ":" << endl;
        if (M == 0)
        {
            for (int i = 0; i < R; i++)
            {
                for (int j = 0; j < C; j++)
                    if (i == 0 and j == 0)
                        ecrire << 'c';
                    else
                        ecrire << '.';
                ecrire << endl;
            }
        }
        else if (R == 1)
        {
            ecrire << 'c';
            for (int j = 1; j < C - M; j++)
                ecrire << '.';
            for (int j = C - M; j < C; j++)
                ecrire << '*';
            ecrire << endl;
        }
        else if (C == 1)
        {
            ecrire << 'c' << endl;
            for (int j = 1; j < R - M; j++)
                ecrire << '.' << endl;
            for (int j = R - M; j < R; j++)
                ecrire << '*' << endl;
        }
        else
        {
            int maxi = max(R, C);
            int mini = min(R, C);
            int c = maxi - M / mini;
            int m = M % mini;
            int p = m % c;
            int r = mini - m / c;
            if (r >= 2 and c >= 2 and p < c - 1 and p < r - 1)
            {
                for (int i = 0; i < R; i++)
                {
                    for (int j = 0; j < C; j++)
                        if (i == 0 and j == 0)
                            ecrire << 'c';
                        else if (j < c)
                        {
                            if ((j < c - 1 and i < r) or i < r - p)
                                ecrire << '.';
                            else
                                ecrire << '*';
                        }
                        else
                            ecrire << '*';
                    ecrire << endl;
                }
            }
            else
            {
                obj = R * C - M;
                continu = true;
                for (int t = 0; t < C / 2 + 1; t++)
                    for (int v = 0; v < R / 2 + 1; v++)
                    {
                        for (int i = 0; i < R; i++)
                            for (int j = 0; j < C; j++)
                                mat[i][j] = 0;
                        mat[v][t] = 1;
                        nb = 1;
                        test(v, t);
                    }
                if (continu)
                    ecrire << "Impossible" << endl;
            }
        }
    }
    return 0;
}
