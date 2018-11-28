#include <cstdio>
#include <iostream>
using namespace std;


int main()
{
    freopen("t.in", "r", stdin);
    freopen("t.out", "w", stdout);

    int T;
    cin >> T;
    for (int c = 1; c <= T; ++c) {
        int A[4][4],B[4][4];
        int same = 0, mark = 0;
        int a,b;
        cin >> a;
        for (int i = 0; i < 4; ++i)
             for (int j = 0; j < 4; ++j)
                cin >> A[i][j];

        cin >> b;
        for (int i = 0; i < 4; ++i)
             for (int j = 0; j < 4; ++j)
                cin >> B[i][j];

        for (int u = 0; u < 4; ++u) {
            for (int v = 0; v < 4; ++v) {
                if (A[a-1][u] == B[b-1][v]) {
                    same++;
                    mark = u;
                }
            }
        }

        if (same == 1) {
            cout << "Case #" << c << ": " << A[a-1][mark] << endl;
        } else if (same > 1) {
            cout << "Case #" << c << ": " << "Bad magician!" << endl;
        } else {
            cout << "Case #" << c << ": " << "Volunteer cheated!" << endl;
        }

    }

    return 0;
}
