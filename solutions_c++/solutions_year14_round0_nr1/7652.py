#include <iostream>
#include <cstdio>
#include <vector>


using namespace std;


int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int t;
    cin >> t;                                                 
    for (int p = 0; p < t; ++p){
        cout << "Case #" << p + 1 << ": ";
        int r1, r2, mat1[4][4], mat2[4][4], row1[4], row2[4];
        vector < int > ans;
        cin >> r1;
        --r1;        
        for (int i = 0; i < 4; ++i) {
            for (int j = 0; j < 4; ++j) {
                cin >> mat1[i][j];
            }
        }

        cin >> r2;
        --r2;
                                      
        for (int i = 0; i < 4; ++i) {
            for (int j = 0; j < 4; ++j) {
                cin >> mat2[i][j];
            }
        }

        for (int i = 0; i < 4; ++i) {
            row1[i] = mat1[r1][i];
            row2[i] = mat2[r2][i];
        }
        for (int i = 0; i < 4; ++i) {
            for (int j = 0; j < 4; ++j) {
                if (row1[i] == row2[j]) {
                    ans.push_back(row1[i]);
                }
            }
        }
        if (ans.size() == 0) {
            cout << "Volunteer cheated!";
        }
        if (ans.size() > 1){
            cout << "Bad magician!";
        }
        if (ans.size() == 1) {
            cout << ans[0];
        }
        cout << endl;
    }
    return 0;
}