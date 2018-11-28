#include<stdlib.h>
#include<iostream>
#include<vector>
#include<string>


const int N = 4;
using namespace std;
int main() {

    int T;

    cin >> T;
    int M[N][N];
    int frow[N];
    int row;

    // save row
    for (int t = 0; t < T; t++) {
     cin >> row;
        for (int i = 0; i < N; ++i) {
            for (int j = 0; j < N; ++j) {
                cin >> M[i][j];
            }
        }


        // Ask the first number
        for (int i = 0; i < N; ++i){
            frow[i] = M[row-1][i];
        }

        cin >> row;
        //DRY
        for (int i = 0; i < N; ++i) {
            for (int j = 0; j < N; ++j) {
                cin >> M[i][j];
            }
        }


        int total = 0;
        int result = 0;
        for(int i = 0; i < N; ++i) {
            for(int j = 0; j < N; ++j) {
                if (frow[i] == M[row-1][j]){
                    total++;
                    result = frow[i];
                    break;
                }

            }

        }

        cout << "Case #" << t+1 << ": ";
        if (total == 0)
            cout << "Volunteer cheated!" << endl;
        else if(total == 1)
            cout << result << endl;
        else
            cout << "Bad magician!" << endl;
    }

    return EXIT_SUCCESS;
}
