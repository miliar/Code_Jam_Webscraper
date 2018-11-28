#include <cstdio>
#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;


int main() {

    freopen("A.in", "r", stdin);
    freopen("A.out", "w", stdout);
    
    int tests, t; 
    int line;
    int mat[5][5];
    t = 1;
    for(cin >> tests; tests; tests--, t++) {
        cin >> line;
        for(int i = 1; i <= 4; i++)
            for(int j = 1; j <= 4; j++)
                cin >> mat[i][j];
        vector<int> first_line;
        for(int j = 1; j <= 4; j++)
            first_line.push_back(mat[line][j]);

        cin >> line;
        for(int i = 1; i <= 4; i++)
            for(int j = 1; j <= 4; j++)
                cin >> mat[i][j];

        int num = 0, sol = 0;
        for(int i = 0; i < first_line.size(); i++)
            for(int j = 1; j <= 4; j++) {
                if(first_line[i] == mat[line][j]) {
                    num++;
                    sol = first_line[i];
                }
            }
                 
        cout << "Case #" << t << ": "; 
        if(num == 1) {
            cout << sol << endl;
        } else if(num == 0) {
            cout << "Volunteer cheated!\n";
        } else {
            cout << "Bad magician!\n";
        }
    }


    return 0;
}
