#include <iostream>

using namespace std;

int bit_num(int num) {
    int c = 0;
    for (; num; ++c)
        num &= num - 1;
    return c;
}

bool good(int x, int y, int n, int m) {
    return (x >= 0) && (x < n) && (y >= 0) && (y < m);
}

int a[5][5], b[5][5], d[5][5];
void dive(int x, int y, int n, int m) {
    d[x][y] = 1;
    if (a[x][y] != 1 && b[x][y] == 0) {
        for (int sx = -1; sx <= 1; ++sx)
            for (int sy = -1; sy <= 1; ++sy) {
                int tmpx = x + sx;
                int tmpy = y + sy;
                if (good(tmpx, tmpy, n, m) && d[tmpx][tmpy] == 0)
                    dive(tmpx, tmpy, n, m);
            }
    }
}

int main()
{
    int t;
    cin >> t;
    for (int case_num = 1; case_num <= t; ++case_num) {
        cout << "Case #" << case_num << ":\n";

        int r, c, m;
        cin >> r >> c >> m;

        bool ok = false;

        for (int pos = 0; !ok && (pos < (1 <<  (r * c))); ++pos)
            if (bit_num(pos) == m) {
                for (int i = 0; i < r; ++i)
                    for (int j = 0; j < c; ++j)
                        a[i][j] = (pos & (1 << (i * c + j))) > 0;

                for (int i = 0; i < r; ++i)
                    for (int j = 0; j < c; ++j) {
                        b[i][j] = 0;
                        for (int sx = -1; sx <= 1; ++sx)
                            for (int sy = -1; sy <= 1; ++sy)
                                if (good(i + sx, j + sy, r, c))
                                    b[i][j] += a[i + sx][j + sy];
                    }

                for (int i = 0; i < r; ++i)
                    for (int j = 0; j < c; ++j) {
                        d[i][j] = 0;
                        if (a[i][j])
                            continue;
                        for (int sx = -1; sx <= 1; ++sx)
                            for (int sy = -1; sy <= 1; ++sy)
                                if ((sx || sy) && good(i + sx, j + sy, r, c) && b[i + sx][j + sy] == 0)
                                    d[i][j] = 1;
                    }


                int x = -1, y = -1;
                if (m == r * c - 1) {
                    for (int i = 0; i < r; ++i)
                        for (int j = 0; j < c; ++j)
                            if (a[i][j] == 0) {
                                a[i][j] = 2;
                                x = i;
                                y = j;
                            }

                } else {
                    bool now_ok = false;
                    for (int i = 0; !now_ok && i < r; ++i)
                        for (int j = 0; !now_ok && j < c; ++j)
                            if (a[i][j] == 0 && b[i][j] == 0) {
                                a[i][j] = 2;
                                x = i;
                                y = j;
                                now_ok = true;
                            }
                }
                for (int i = 0; i < r; ++i)
                    for (int j = 0; j < c; ++j)
                        d[i][j] = 0;
                dive(x, y, r, c);

                bool now_ok = true;
                for (int i = 0; i < r; ++i)
                    for (int j = 0; j < c; ++j)
                        if (a[i][j] == 0 && d[i][j] != 1) {
                            now_ok = false;
                        }
                if (now_ok) {
                    ok = true;
                    for (int i = 0; i < r; ++i) {
                        for (int j = 0; j < c; ++j)
                            if (a[i][j] == 0)
                                cout << ".";
                            else if (a[i][j] == 1)
                                cout << "*";
                            else
                                cout << "c";
                        cout << "\n";
                    }
                }
            }
            if (!ok)
                cout << "Impossible\n";

    }
    return 0;
}
