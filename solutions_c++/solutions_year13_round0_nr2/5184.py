
#include <iostream>

using namespace std;

void do_testcase() {
    unsigned short int N, M;
    cin >> N >> M;
    unsigned short int *arr = new unsigned short int[N * M];
    unsigned short int *max_rows = new unsigned short int[N];
    unsigned short int *max_cols = new unsigned short int[M];

    for (unsigned short int i = 0; i < N; ++i) {
        max_rows[i] = 0;
    }
    for (unsigned short int j = 0; j < M; ++j) {
        max_cols[j] = 0;
    }

    for (unsigned short int i = 0; i < N; ++i) {
        for (unsigned short int j = 0; j < M; ++j) {
            unsigned short int h;
            cin >> h;
            arr[i * M + j] = h;
            if (h > max_rows[i]) {
                max_rows[i] = h;
            }
            if (h > max_cols[j]) {
                max_cols[j] = h;
            }
        }
    }

    bool is_possible = true;
    for (unsigned short int i = 0; i < N && is_possible; ++i) {
        for (unsigned short int j = 0; j < M && is_possible; ++j) {
            unsigned short int h = arr[i * M + j];
            if (h < max_rows[i] && h < max_cols[j]) {
                is_possible = false;
            }
        }
    }

    if (is_possible) {
        cout << "YES";
    } else {
        cout << "NO";
    }

    delete[] arr;
    delete[] max_rows;
    delete[] max_cols;
}

int main(int argc, char *argv[]) {
    unsigned short int T;
    cin >> T;
    for (unsigned short int i = 0; i < T; ++i) {
        cout << "Case #" << i + 1 << ": ";
        do_testcase();
        cout << endl;
    }
}
