#include <iostream>
#include <vector>
#include <string>
using namespace std;

typedef vector<int> Row;
typedef vector<Row> Matrix;

int main()
{
    string s1 = "Bad magician!";
    string s2 = "Volunteer cheated!";
    int T;
    cin >> T;
    for (int x = 1;x <= T; ++x) {
        int a1,a2;
        Matrix m1(4,Row(4)), m2(4,Row(4));
        cin >> a1;
        for (int i = 0; i < 4; ++i) {
            for (int j = 0; j < 4; ++j) cin >> m1[i][j];
        }
        cin >> a2;
        for (int i = 0; i < 4; ++i) {
            for (int j = 0; j < 4; ++j) cin >> m2[i][j];
        }
        cout << "Case #" << x << ": ";
        int sol = 0;
        string y;
        bool finded = false;
        for (int i = 0;i < 4;++i) {
            for (int j = 0;j < 4;++j) {
                if (m1[a1-1][i] == m2[a2-1][j]) {
                    if (not finded) {
                        finded = true;
                        sol = m1[a1-1][i];
                    }
                    else  {
                        sol = 0;
                        y = s1;
                    }
                }
            }
        }
        if (not finded) y = s2;
        if (sol != 0) cout << sol;
        else cout << y;
        cout << endl;
    }
}
