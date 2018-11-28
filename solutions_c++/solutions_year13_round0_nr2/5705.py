#include <iostream>
#include <vector>
#include <string>

using namespace std;

int lm[10][10];

bool checkPattern(int m, int n) {
    for(int i = 0; i < m; i++) {
        for(int j = 0; j < n; j++) {
            if(lm[i][j] == 1) {
                bool isRowAllOnes = true;
                for(int k = 0; k < n; k++) {
                    if(lm[i][k] != 1) {
                        isRowAllOnes = false;
                        break;
                    }
                }
                bool isColumnAllOnes = true;
                for(int k = 0; k < m; k++) {
                    if(lm[k][j] != 1) {
                        isColumnAllOnes = false;
                        break;
                   }
                }
                if(!isRowAllOnes && !isColumnAllOnes)
                    return false;
            }
        } 
    }
    return true;                
}


int main() {
    string stmp;
    int noTests, m, n;
    cin >> noTests;
    getline(cin, stmp);
    for(int i = 0; i < noTests; i++) {
        cin >> m >> n;
        getline(cin, stmp);
        for(int j = 0; j < m; j++) {
            for(int k = 0; k < n; k++) {
                cin >> lm[j][k];
            }
            getline(cin, stmp);
        }
        // output
        bool state = checkPattern(m, n);
        cout << "Case #" << i + 1 << ": " << string(state == false ? "NO" : "YES") << endl;
    }
}

