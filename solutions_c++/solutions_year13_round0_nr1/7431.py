#include <iostream>
#include <cstring>

using namespace std;

int map[5][5];
int T;
bool bo=false;

int check() {
    int tmp = 0;
    for (int i = 1; i <= 4; i++)
        tmp += map[i][i];
    if (tmp == 0 || tmp == 4 || tmp == 100 || tmp == 103)
        return tmp;

    tmp = 0;
    for (int i = 1; i <= 4; i++)
        tmp += map[i][5-i];
    if (tmp == 0 || tmp == 4 || tmp == 100 || tmp == 103)
        return tmp;

    for (int i = 1; i <= 4; i++) {
        tmp = 0;
        for (int j = 1; j <= 4; j++)
            tmp += map[i][j];
        if (tmp == 0 || tmp == 4 || tmp == 100 || tmp == 103)
            return tmp;

        tmp = 0;
        for (int j = 1; j <= 4; j++)
            tmp += map[j][i];
        if (tmp == 0 || tmp == 4 || tmp == 100 || tmp == 103)
            return tmp;
    }
    return -1;
}

int output(int ti, int res) {
    if (res == 0 || res == 100) {
        cout << "Case #" << ti << ": X won" << endl;
        return 0;
    }
    if (res == 4 || res == 103) {
        cout << "Case #" << ti << ": O won" << endl;
        return 0;
    }
    if (res == -1 && !bo) {
        cout << "Case #" << ti << ": Draw" << endl;
        return 0;
    }
    cout << "Case #" << ti << ": Game has not completed" << endl;
    return 0;
}

int main() {
    char ch;
    cin >> T;
    for (int ti = 1; ti <= T; ti++) {
        bo = false;
        for (int i = 1; i <= 4; i++)
            for (int j = 1; j <= 4; j++) {
                cin >> ch;
                if (ch == 'X')
                    map[i][j] = 0;
                else if (ch == 'O')
                    map[i][j] = 1;
                else if (ch == 'T')
                    map[i][j] = 100;
                else if (ch == '.') {
                    map[i][j] = 1000;
                    bo = true;
                }
            }
        output(ti, check());
    }
    return 0;
}

