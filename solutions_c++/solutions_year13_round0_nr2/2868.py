#include <iostream>
#include <vector>
#include <map>
#include <cstring>
#include <fstream>
#include <string>
#include <stdlib.h>

using namespace std;

int main()
{
    int T, N, M;
    bool ret;

    cin >> T;
    for (int i = 1; i <= T; i++) {
        cin >> N >> M;

        int lawn[N][M];

        for (int j = 0; j < N; j++) {
            for (int k = 0; k < M; k++) {
                cin >> lawn[j][k];
            }
        }

        for (int j = 0; j < N; j++) {
            for (int k = 0; k < M; k++) {
                ret = false;
                int l;

                for (l = 0; l < N; l++) {
                    if (lawn[j][k] < lawn[l][k]) {
                        break;
                    }
                }
                
                if (l == N) {
                    ret = true;
                }


                for (l = 0; l < M; l++) {
                    if (lawn[j][k] < lawn[j][l]) {
                        break;
                    }
                }

                if (l == M) {
                    ret = true;
                }

                if (!ret) {
                    goto DONE;
                }
            }
        }

DONE:
        cout << "Case #" << i << ": " << (ret ? "YES" : "NO") << endl;
    }
}
