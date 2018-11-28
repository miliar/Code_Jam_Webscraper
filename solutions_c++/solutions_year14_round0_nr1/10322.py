// Copyright (c) 2014 FreeLancer Company.
// Author: Guojun Liu (liuguojun.pku@gmail.com)

#include <iostream>
using namespace std;
int main() {
    int T;
    cin >> T;
    for (int ccase = 1; ccase <= T; ++ccase) {
        int a1, b1, a[5][5], b[5][5];
        cin >> a1;
        for (int i = 1; i <=4; ++i)
            for (int j = 1; j <=4; ++j)
                cin >> a[i][j];
        cin >> b1;
        for (int i = 1; i <=4; ++i)
            for (int j = 1; j <=4; ++j)
                cin >> b[i][j];
        int found = 0;
        int result = 0;
        for (int j = 1; j <= 4; ++j)
            for (int i = 1; i <= 4; ++i)
                if (a[a1][i] == b[b1][j]) {
                    found++;
                    result = b[b1][j];
                }
        cout << "Case #" << ccase << ": ";
        if (found == 0)
            cout << "Volunteer cheated!";
        else if (found == 1)
            cout << result;
        else
            cout << "Bad magician!";
        cout << endl;
    }
    return 0;
}

