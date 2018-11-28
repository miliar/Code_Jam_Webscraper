#include <iostream>
#include <vector>
#include <queue>
#include <string>
#include <cstring>
#include <cstdio>
#include <iomanip>
#include <algorithm>
#include <cstdlib>
#include <fstream>
#include <cmath>
#include <set>
#include <map>
#include <stack>
using namespace std;


char grid[100][100];

void gfill(int c, int r, int cnt, char ch) {
    for (int i = 1; i <= c && cnt > 0; ++i)
    for (int j = 1; j <= r && cnt > 0; ++j) {
        grid[i][j] = ch;
        cnt --;
    }
}

void gfillv(int c, int r, int cnt, char ch) {
    for (int j = 1; j <= r && cnt > 0; ++j)
        for (int i = 1; i <= c && cnt > 0; ++i) {
            grid[i][j] = ch;
            cnt --;
        }
}

void check(int n) {
    if (n == 4)
        grid[1][1] = grid[1][2] = grid[2][1] = grid[2][2] = '.';
    else if (n == 9) {
        grid[1][1] = grid[1][2] = grid[2][1] = grid[2][2] = '.';
        grid[1][3] = grid[2][3] = grid[3][3] = grid[3][2] = grid[3][1] = '.';
    } else if (n == 13) {
        grid[1][1] = grid[1][2] = grid[2][1] = grid[2][2] = '.';
        grid[1][3] = grid[2][3] = grid[3][3] = grid[3][2] = grid[3][1] = '.';
        grid[1][4] = grid[2][4] = grid[4][1] = grid[4][2] = '.';
    }

}

void check(int n , int m) {
    for (int i = 1; i <= n; ++i)
        for (int j = 1; j <=m; ++j)
        grid[i][j] = '.';
}

int main() {
    int T;
    bool trans, imp;

    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);

    cin>>T;
    for (int t=1;t<=T;++t) {
        cout<<"Case #"<<t<<":" << endl;
        int c, r, m;
        cin >> c >> r >> m;
        m = c*r - m;

        trans = false;
        imp = false;
        if (c > r) {
            swap(c, r);
            trans = true;
        }
        gfill(c, r, c*r, '*');
        if (m == 1) {
            grid[1][1] = 'c';
        } else {
            if (c == 1) {
                gfill(c, r, m, '.');
            } else if (c == 2) {
                if (m > 3 && (m % 2 == 0)) {
                    gfillv(c, r, m, '.');
                } else imp = true;
            } else if (c == 3 && r == 3) {
                if (m < 4 || m == 5 || m == 7)
                    imp = true;
                else if (m == 4) {
                    check(m);
                } else {
                    gfill(c, r, m, '.');
                }
            } else if (c == 4 && r == 4) {
                if (m == 4 || m == 9 || m == 13)
                    check(m);
                else if (m == 6) {
                    check(2,3);
                }
                else if (m < 8)
                    imp = true;
                else gfill(c, r, m, '.');
            } else if (c == 5 && r == 5) {
                if (m < 4 || m == 5 || m == 7)
                    imp = true;
                else if (m == 4)
                    check(4);
                else if (m == 9)
                    check(9);
                else if (m == 8)
                    check(2, 4);
                else if (m == 6)
                    check(2,3);
                else if (m == 16)
                    check(4,4);
                else if (m == 11) {
                    check(3,4);
                    grid[3][4] = '*';
                } else if (m == 21) {
                    check(3, 5);
                    check(5, 3);
                } else
                    gfill(c, r, m, '.');
            } else if (c == 3 && r == 4) {
                if (m < 4 || m == 5 || m == 7)
                    imp = true;
                else if (m == 4 || m == 9)
                    check(m);
                else if (m == 6)
                    check(2, 3);
                else if (m == 10)
                    gfill(c, r, m, '.');
                else gfillv(c, r, m, '.');
            } else if (c == 4 && r == 5) {
                if (m < 4 || m == 5 || m == 7)
                    imp = true;
                else if (m == 4 || m ==9)
                    check(m);
                else if (m == 6 || m == 8)
                    check(2, m/2);
                else if (m == 13 || m == 17) {
                    gfill(c,r,m, '.');
                } else
                    gfillv(c, r, m, '.');
            } else if (c == 3 && r == 5) {
                if (m == 2 || m == 3 || m ==5 || m ==7)
                    imp = true;
                else if (m == 4 || m == 9)
                    check(m);
                else if (m == 8 || m == 6)
                    check(2, m/2);
                else if (m == 11)
                    gfillv(c, r, m, '.');
                else gfill(c,r,m, '.');

            }
            grid[1][1] = 'c';
        }

        if (imp)
            cout << "Impossible" << endl;
        else {
            if (trans) {
                for (int j = 1; j <= r; ++j) {
                    for (int i = 1; i <= c; ++i)
                        cout << grid[i][j];
                    cout << endl;
                }
            } else {
                for (int i = 1; i <= c; ++i) {
                    for (int j = 1; j <= r; ++j)
                        cout << grid[i][j];
                    cout << endl;
                }
            }
        }
    }
    return 0;
}
