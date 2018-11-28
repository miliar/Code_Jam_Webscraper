#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

void readTable(int row[4]) {
    int rowNum;
    cin >> rowNum;
    for (int i = 1; i <= 4; i++) {
        for (int j = 0; j < 4; j++) {
            if (i == rowNum) {
                cin >> row[j];
            } else {
                int temp;
                cin >> temp;
            }
        }
    }
}

void compareResults(int testNum, int row[4], int row2[4]) {
    std::vector<int> possibleResults(10);
    vector<int>::iterator it;

    sort(row, row + 4);
    sort(row2, row2 + 4);
    
    it = set_intersection(row, row + 4, row2, row2 + 4, possibleResults.begin());
    
    possibleResults.resize(it-possibleResults.begin());
    
    if (possibleResults.size() > 1) {
        cout << "Case #" << testNum << ": Bad magician!" << endl;
    } else if (possibleResults.size() == 1) {
        cout << "Case #" << testNum << ": " << possibleResults.at(0) << endl;
    } else {
        cout << "Case #" << testNum << ": Volunteer cheated!" << endl;
    }
}

int main() {
    
    int T;
    cin >> T;
    
    int row[4];
    int row2[4];
    
    for (int testNum = 1; testNum <= T; testNum++) {
        readTable(row);
        readTable(row2);
        compareResults(testNum, row, row2);
    }
    
    
}