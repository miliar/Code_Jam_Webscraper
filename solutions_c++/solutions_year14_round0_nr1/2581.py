//postfix calculator

#include <iostream>
#include <vector>
#include <utility> 
#include <algorithm>
#include <fstream>
#include <set>

using namespace std;


int main() {
    ofstream fOutput;
    fOutput.open ("result.out");
    int tests, row, temp, matches, result;;
    cin >> tests;
    for (int i = 1; i <= tests; i++) {
        set<int> numbs;
        cin >> row;
        for (int k = 1; k <= 4; k++) {
            for (int l = 1; l <= 4; l++) {
                cin >> temp;
                if (k == row) {
                    numbs.insert(temp);
                }
            }
        }
        cin >> row;
        matches = 0;
        for (int k = 1; k <= 4; k++) {
            for (int l = 1; l <= 4; l++) {
                cin >> temp;
                if (k == row) {
                    if(numbs.find(temp) != numbs.end()) {
                        result = temp;
                        matches++;
                    }
                }
            }
        }

        fOutput << "Case #" << i << ": ";
        if(matches == 0){
            fOutput << "Volunteer cheated!" << endl;
        } else if (matches == 1) {
            fOutput << result << endl;
        } else {
            fOutput << "Bad magician!" << endl;
        }


    }

    return 0;
        
}
