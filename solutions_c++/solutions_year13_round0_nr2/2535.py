#include <iostream>

using namespace std;

int N, M, T;
int a[100][100];
int maxcol[100], maxrow[100];

int main ()
{
    cin >> T;
    for (int testCase = 1; testCase <= T; ++testCase) {
        cin >> N >> M;
        for (int i = 0; i < N; ++i) {
            for (int j = 0; j < M; ++j) {
                cin >> a[i][j];
            }
        }
        for (int i = 0; i < N; ++i) {
            maxrow[i] = 0;
        }
        for (int i = 0; i < M; ++i) {
            maxcol[i] = 0;
        }

        for (int i = 0; i < N; ++i) {
            for (int j = 0; j < M; ++j) {
                if (a[i][j] > maxrow[i]) {
                    maxrow[i] = a[i][j];
                }
                if (a[i][j] > maxcol[j]) {
                    maxcol[j] = a[i][j];
                }
            }
        }
        bool no = false;
        for (int i = 0; i < N && !no; ++i) {
            for (int j = 0; j < M && !no; ++j) {
                if (a[i][j] < maxrow[i] && a[i][j] < maxcol[j]) {
                    no = true;
                }
            }
        }
        cout << "Case #" << testCase << ": " << (no? "NO": "YES") << '\n';
    }
    return 0;
}