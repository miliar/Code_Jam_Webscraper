// -*- mode:c++; tab-width:4; c-basic-offset:4; indent-tabs-mode:nil -*-  
#include <iostream>
#include <vector>

using namespace std;

const int maxSize = 100;

int main() {
    int T, N, M;
    int i, j, k;
    vector<int> maxRow(maxSize, 0);
    vector<int> maxCol(maxSize, 0);
    bool okPattern;
    vector< vector<int> > lawn(maxSize);

    // allocate the matrix
    for (i=0; i<maxSize; i++)
        lawn[i].resize(maxSize, 0);
    
    cin >> T;
    for (i=0; i<T; i++) {
        cin >> N >> M;
        // Reset the max
        fill(maxRow.begin(), maxRow.end(), 0);
        fill(maxCol.begin(), maxCol.end(), 0);
        // Read the lawn values
        for (j=0; j<N; j++) {
            for (k=0; k<M; k++) {
                cin >> lawn[j][k];
                if (lawn[j][k] > maxRow[j])
                    maxRow[j] = lawn[j][k];
                if (lawn[j][k] > maxCol[k])
                    maxCol[k] = lawn[j][k];
            }
        }

        // Check if the pattern is ok
        okPattern = true;
        for (j=0; j<N && okPattern; j++) {
            for (k=0; k<M && okPattern; k++) {
                if (lawn[j][k] < maxRow[j] && lawn[j][k] < maxCol[k])
                    okPattern = false;
            }
        }
        if (okPattern)
            cout << "Case #" << i+1 << ": YES" << endl;
        else
            cout << "Case #" << i+1 << ": NO" << endl;

    }

  return 0;
}
