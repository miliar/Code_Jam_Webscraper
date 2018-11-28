#include <iostream>
#include <string>
#include <fstream>
#include <stdlib.h>
#include <sstream>
#include <math.h>
using namespace std;

int main() {
    
    ifstream fin("/Users/usamaelnily/Desktop/in.txt");
    ofstream fout("/Users/usamaelnily/Desktop/out.txt");
    
    int t, c = 1, n, m;
    fin >> t;
    while(t--) {
        string op = "YES";
        int b[100][100];
        fin >> n >> m;
        for(int i = 0; i < n; i++) {
            for(int j = 0; j < m; j++) {
                fin >> b[i][j];
            }
        }
        
        for(int i = 0; i < n; i++) {
            for(int j = 0; j < m; j++) {
                if(b[i][j] < 100) {
                    int row = 1, col = 1;
                    for(int k = 0; k < n; k++) {
                        if(b[k][j] > b[i][j])
                            row = 0;
                    }
                    for(int k = 0; k < m; k++) {
                        if(b[i][k] > b[i][j])
                            col = 0;
                    }
                    if(!(row || col)) {
                        op = "NO";
                        break;
                    }
                }
            }
        }
        
        fout <<"Case #" << c << ": " << op << endl;
        c++;
    }
    return 0;
}