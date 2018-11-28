#include <fstream>
#include <iostream>

using namespace std;

void process_testcase(ifstream &f) {
    int N, M;
    int lawn[100][100];

    int maxcol[100];
    int maxrow[100];

    f >> N;
    f >> M;

    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
            f >> lawn[i][j];
            if (lawn[i][j] > 100) {
                cout << "NO";
                return;
            }
            maxcol[j] = 0;
        }
        maxrow[i] = 0;
    }

    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
            maxrow[i] = max(maxrow[i], lawn[i][j]);
            maxcol[j] = max(maxcol[j], lawn[i][j]);
        }
    }

    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
            if (maxrow[i] > lawn[i][j] && maxcol[j] > lawn[i][j]) {
                cout << "NO";
                return;
            }
        }
    }

    cout << "YES";
}

int main(int argc, char **argv) {
    int num_testcases;
    ifstream f(argv[1]);

    f >> num_testcases;

    for (int i = 0; i < num_testcases; i++) {
        cout << "Case #" << (i+1) << ": ";
        process_testcase(f);
        cout << endl;
    }
}
