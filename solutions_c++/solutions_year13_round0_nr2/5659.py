#include "string"
#include "iostream"
using namespace std;

int main() {
    int T;
    cin >> T;
    int N, M;
    int A[10][10];
    bool check[10][10];
    string result;
    int i,j;
    int row[10];
    int col[10];
    for (int k=0; k<T; k++) {
        cin >> N >> M;
        for (i=0; i<N; i++) {
            row[i] = 0;
            for (j=0; j<M; j++) {
                cin >> A[i][j];
                row[i] += A[i][j];
                check[i][j] = false;
            }
            if (row[i] == M) {
                for (j=0; j<M; j++)
                    check[i][j] = true;
            }
        }

        for (j=0; j<M; j++) {
            col[j] = 0;
            for (i=0; i<N; i++) {
                col[j] += A[i][j];
            }
            if (col[j] == N) {
                for (i=0; i<N; i++)
                    check[i][j] = true;
            }
        }
        result = "YES";
        for (i=0; i<N; i++) {
            for (j=0; j<M; j++) {
                if (A[i][j] == 1 && !check[i][j])
                    result = "NO";
            }
        }


        cout << "Case #" << k+1 << ": " << result << endl;
    
    }
    return 0;
}
