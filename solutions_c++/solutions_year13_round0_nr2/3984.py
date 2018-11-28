#include <iostream>
using namespace std;

int main(char* argv[]) {
    ios_base::sync_with_stdio(false);

    int T;
    int N, M;
    int tab[101][101];
    bool possible = true;

    cin >> T;
    for (int i = 0; i < T; i++) {
        possible = true;
        cin >> N >> M;

        for (int n = 0; n < N; n++) {
            for (int m = 0; m < M; m++) {
                cin >> tab[n][m];
            }
        }

        for (int n = 0; n < N; n++) {
            for (int m = 0; m < M; m++) {
                tab[n][100] = max(tab[n][100], tab[n][m]);
                tab[100][m] = max(tab[100][m], tab[n][m]);
            }
        }

        for (int n = 0; n < N && possible; n++) {
            for (int m = 0; m < M && possible; m++) {
                if (tab[n][m] < tab[100][m] && tab[n][m] < tab[n][100])
                    possible = false;
            }
        }

        for (int n = 0; n < N; n++) {
            for (int m = 0; m < M; m++) {
                tab[n][100] = 0;
                tab[100][m] = 0;
            }
        }

        if (possible)
            cout << "Case #" << i+1 << ": YES" << endl;
        else
            cout << "Case #" << i+1 << ": NO" << endl; 
    }

    return 0;
}