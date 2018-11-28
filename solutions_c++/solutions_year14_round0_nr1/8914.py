#include <cstdio>
#include <algorithm>
#include <iostream>
#include <vector>
#include <fstream>

using namespace std;


int main() {
    ifstream cin("test.in");
    ofstream cout("test.out");

    int T; cin >> T;
    for (int testcase = 1; testcase <= T; ++testcase) {
        int row; cin >> row;

        vector <vector <int> > matrix(5, vector <int>(5, 0));
        vector <int> count(20, 0);

        for (int i = 1; i <= 4; ++i) {
            for(int j = 1; j <= 4; ++j) {
                cin >> matrix[i][j];
                if (i == row) {
                    count[matrix[i][j]] += 1;
                }
            }
        }
        cin >> row;

        for (int i = 1; i <= 4; ++i) {
            for (int j = 1; j <= 4; ++j) {
                cin >> matrix[i][j];
                if (i == row) {
                    count[matrix[i][j]] += 1;
                }
            }
        }
        int answer = -1;
        int nr = 0;
        for (int i = 1; i <= 16; ++i) {
            if (count[i] > 2) {
                answer = -1;
                nr = 0;
                break;
            } if(count[i] == 2) {
                nr++;
                answer = i;
            }
        }

        cout << "Case #" << testcase <<": " ;
        if (answer != -1 && nr == 1) {
            cout << answer << "\n";
            continue;
        }
        if (nr == 0) {
            cout << "Volunteer cheated!\n";
            continue;
        }

        cout << "Bad magician!\n";


    }

}

