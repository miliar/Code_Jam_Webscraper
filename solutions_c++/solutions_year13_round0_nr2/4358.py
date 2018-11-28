#include <iostream>
#include <string>
#include <cstdlib>
#include <cstring>

using namespace std;

int n, m;

int dst[101][101];
int now[101][101];
int tmp[101][101];
bool done[101][101];

bool check_done() {
    for (int i=0; i<n; ++i) {
        for (int j=0; j<m; ++j) {
            if (!done[i][j]) return false;
        }
    }
    return true;
}

bool check_yes() {
    for (int i=0; i<n; ++i) {
        for (int j=0; j<m; ++j) {
            if (now[i][j] != dst[i][j]) return false;
        }
    }
    return true;
}

bool check_no() {
    for (int i=0; i<n; ++i) {
        for (int j=0; j<m; ++j) {
            if (now[i][j] < dst[i][j]) return true;
        }
    }
    return false;
}

int find_max(int &x, int &y) {
    int max = -1;
    for (int i=0; i<n; ++i) {
        for (int j=0; j<m; ++j) {
            if (!done[i][j] && dst[i][j] > max) {
                max = dst[i][j];
                x = i;
                y = j;
            }
        }
    }
    return max;
}

void cut_row(int no, int h)
{
    {
        int i = no;
        for (int j=0; j<m; ++j) {
            if (now[i][j] > h) {
                now[i][j] = h;
            }
        }
    }
}

void cut_col(int no, int h)
{
    for (int i=0; i<n; ++i) {
        {
            int j = no;
            if (now[i][j] > h) {
                now[i][j] = h;
            }
        }
    }
}

bool can_cut_row(int no, int h)
{
    memcpy(tmp, now, sizeof(now));
    cut_row(no, h);
    bool ret = !check_no();
    memcpy(now, tmp, sizeof(now));
    return ret;
}

bool can_cut_col(int no, int h)
{
    memcpy(tmp, now, sizeof(now));
    cut_col(no, h);
    bool ret = !check_no();
    memcpy(now, tmp, sizeof(now));
    return ret;
}

int main()
{
    int t;
    cin >> t;
    cin.ignore();
    for (int c=0; c<t; ++c) {
        cin >> n >> m;
        for (int i=0; i<n; ++i) {
            for (int j=0; j<m; ++j) {
                cin >> dst[i][j];
                now[i][j] = 100;
                done[i][j] = false;
            }
        }
        bool ret = false;
        while (!check_done()) {
            int x, y;
            int max = find_max(x, y);
            if (can_cut_row(x, max)) {
                cut_row(x, max);
            } else if (can_cut_col(y, max)) {
                cut_col(y, max);
            } else {
                ret = false;
                break;
            }
            done[x][y] = true;
            if (check_yes()) {
                ret = true;
                break;
            }
            if (check_no()) {
                ret = false;
                break;
            }
        }

        if (check_yes()) ret = true;
        if (check_no()) ret = false;
        cout << "Case #" << c + 1 << ": " << (ret ? "YES" : "NO") << endl;
    }
    return 0;
}
