#include <iostream>
#include <vector>

using namespace std;

int main( void ) {
    bool possible;
    int t;
    cin >> t;
    for(int k = 0; k < t; ++k) {
        possible = true;
        int row, col;
        cin >> row;
        cin >> col;
        vector< vector < int > > grass;
        vector < int > rowMax(row, 0);
        vector < int > colMax(col, 0);
        for(int i = 0; i < row; ++i) {
            vector < int > sillyVector;
            for(int j = 0; j < col; ++j) {
                int sillyInt;
                cin >> sillyInt;
                sillyVector.push_back(sillyInt);
            }
            grass.push_back(sillyVector);
        }
        for(int i = 0; i < row; ++i) {
            for(int j = 0; j < col; ++j) {
                if(grass[i][j] > rowMax.at(i)) {
                    rowMax[i] = grass[i][j];
                }
            }
        }
        for(int i = 0; i < col; ++i) {
            for(int j = 0; j < row; ++j) {
                if(grass[j][i] > colMax.at(i)) {
                    colMax[i] = grass[j][i];
                }
            }
        }
        for(int i = 0; i < row; ++i) {
            for(int j = 0; j < col; ++j) {
                if(grass[i][j] < rowMax[i] && grass[i][j] < colMax[j])
                    possible = false;
            }
            if(!possible)
                break;
        }
        if(possible) {
            cout << "Case #" << k + 1 << ": YES\n";
        } else {
            cout << "Case #" << k + 1 << ": NO\n";
        }
    }
    return 0;
}
