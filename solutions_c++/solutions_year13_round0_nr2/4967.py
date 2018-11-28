#include <iostream>

using namespace std;

bool docase(int a[100][100], int N, int M)
{
    int b[100][100];
    for (int i=0; i<N; ++i) {
        for (int j=0; j<M; ++j) {
            b[i][j] = 100;
        }
    }

    for (int i=0; i<N; ++i) {
        // find max in row
        int max = a[i][0];
        for (int j=1; j<M; ++j) {
            if (a[i][j] > max) max = a[i][j];
        }
        // shave
        for (int j=0; j<M; ++j) {
            if (b[i][j] > max) {
                b[i][j] = max;
            }
        }
    }

    for (int j=0; j<M; ++j) {
        // find max in row
        int max = a[0][j];
        for (int i=1; i<N; ++i) {
            if (a[i][j] > max) max = a[i][j];
        }
        // shave
        for (int i=0; i<N; ++i) {
            if (b[i][j] > max) {
                b[i][j] = max;
            }
        }
    }

    for (int i=0; i<N; ++i) {
        for (int j=0; j<M; ++j) {
            if (a[i][j] != b[i][j])
                return false;
        }
    }
    return true;
}

int main()
{
    int T;
    cin >> T;

    int a[100][100];
    
    for (int caseno=0; caseno<T; ++caseno) {
        int N, M;
        cin >>  N >> M;
        for (int i=0; i<N; ++i) {
            for (int j=0; j<M; ++j) {
                cin >> a[i][j];
            }
        }
        // for (int i=0; i<N; ++i) {
        //     for (int j=0; j<M; ++j) {
        //         cout << a[i][j] << " ";
        //     }
        //     cout << endl;
        // }
        if (docase(a, N, M)) {
            cout << "Case #" << caseno+1 << ": YES" << endl;
        } else {
            cout << "Case #" << caseno+1 << ": NO" << endl;
        }
    }

    return 0;
}
