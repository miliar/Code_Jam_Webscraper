#include <iostream>
#include <sstream>
#include <algorithm>
#include <fstream>
#include <set>
#include <vector>
#include <map>

using namespace std;

int main() {
    ifstream cin("B-large.in");
    ofstream cout("out.txt");
    int T;
    cin >> T;
    for (size_t t = 1; t <= T; t++) {
        int N, M;
        cin >> N >> M;
        int g[100][100] = {};
        for (int i = 0; i < N; i++)
            for (int j = 0; j < M; j++)
                cin >> g[i][j];
        bool ok = true;
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                bool m1 = true, m2 = true;
                for (int k = 0; k < N; k++) {
                    if (g[k][j] > g[i][j])
                        m1 = false;
                }
                for (int k = 0; k < M; k++) {
                    if (g[i][k] > g[i][j])
                        m2 = false;
                }
                if (! m1 && ! m2)
                    ok = false;
            }
        }
        cout << "Case #" << t << ": ";
        if (ok)
            cout << "YES";
        else
            cout << "NO";
        cout << endl;
    }
}

