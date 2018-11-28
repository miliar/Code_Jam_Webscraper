#include <iostream>
#include <cstdio>
#include <string>
#include <map>
#include <vector>

using namespace std;

const int MAXN = 1111;

string s[MAXN];
int a[MAXN][MAXN];
bool f[MAXN][MAXN];
int n, m;
int res;

void checkTop(char c = '^') {
    for (int j = 0; j < m; j++) {
        for (int i = 0; i < n; i++)
            if (s[i][j] != '.') {
                a[i][j]--;
                if (s[i][j] == c)
                    res++;
                break;
        }
    }
}

void checkBottom(char c = 'v') {
    for (int j = 0; j < m; j++) {
        for (int i = n - 1; i >= 0; i--)
            if (s[i][j] != '.') {
                a[i][j]--;
                if (s[i][j] == c)
                    res++;
                break;
        }
    }
}

void checkLeft(char c = '<') {
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++)
            if (s[i][j] != '.') {
                a[i][j]--;
                if (s[i][j] == c)
                    res++;
                break;
        }
    }
}

void checkRight(char c = '>') {
    for (int i = 0; i < n; i++) {
        for (int j = m - 1; j >= 0; j--)
            if (s[i][j] != '.') {
                a[i][j]--;
                if (s[i][j] == c)
                    res++;
                break;
        }
    }
}

int main() {
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);

    int o;
    cin >> o;

    int t = 0;
    while (t < o) {
        t++;
        cout << "Case #" << t << ": ";
        cin >> n >> m;
        res = 0;
        for (int i = 0; i < n; i++)
            cin >> s[i];
        for (int i = 0; i < n; i++)
            for (int j = 0; j < m; j++) {
                a[i][j] = 4;
                f[i][j] = false;
            }

        checkTop();
        checkBottom();
        checkLeft();
        checkRight();

        for (int i = 0; i < n; i++)
            for (int j = 0; j < m; j++)
                if (res >= 0 && a[i][j] == 0) {
                    cout << "IMPOSSIBLE" << endl;
                    res  = -1;
                }

        if (res >= 0)
            cout << res << endl;

    }

    return 0;
}
