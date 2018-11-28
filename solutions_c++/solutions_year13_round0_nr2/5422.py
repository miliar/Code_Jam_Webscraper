#include <string>
#include <algorithm>
#include <iostream>
#include <cstdio>
#include <sstream>

using namespace std;

string tostring(int i) {
    stringstream ss;
    ss << i;
    return ss.str();
}

class Lawn {
    private:
    int n, m, field[101][101], maxRows[101], maxCols[101];

    void computeMaxRows() {
        for (int i = 0; i < n; i++) {
            int maxRow = -1;
            for (int j = 0; j < m; j++)
                maxRow = max(maxRow, field[i][j]);
            maxRows[i] = maxRow;
        }

//        for (int i = 0; i < n; i++)
//            cout << maxRows[i] << ' ';
//        cout << endl;
    }

    void computeMaxCols() {
        for (int i = 0; i < m; i++) {
            int maxCol = -1;
            for (int j = 0; j < n; j++)
                maxCol = max(maxCol, field[j][i]);
            maxCols[i] = maxCol;
        }

//        for (int i = 0; i < m; i++)
//            cout << maxCols[i] << ' ';
//        cout << endl;
    }

    public:

    Lawn() {
        cin >> n >> m;
        for (int i = 0; i < n; i++)
            for (int j = 0; j < m; j++)
                cin >> field[i][j];
        computeMaxCols();
        computeMaxRows();
    }

    bool checkField() {
        for (int i = 0; i < n; i++)
            for (int j = 0; j < m; j++)
                if (field[i][j] != maxRows[i] and field[i][j] != maxCols[j])
                    return false;
        return true;
    }
};

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    int T;

    cin >> T;
    for (int i = 0; i < T; i++) {
        Lawn temp;
        string ans = "Case #" + tostring(i + 1) + ": ";
        ans += (temp.checkField()) ? "YES" : "NO";
        cout << ans << endl;
    }

    return 0;
}
