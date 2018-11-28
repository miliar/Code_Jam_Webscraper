#include <cstdlib>
#include <iostream>
#include <iomanip>
#include <stdio.h>

using namespace std;

int main(int argc, char** argv) {
    int cases;
    cin >> cases;

    int height = 100;
    for (int i = 1; i <= cases; i++) {
        int rows=0, cols=0;
        cin >> rows; cin>>cols;
        
        int lawn[200][200];
        int visited[200][200];
        for (int r = 1; r <= rows; r++) {
            for(int c=1; c<=cols; c++){
                cin >> lawn[r][c];
                visited[r][c] = 0;
            }
        }

        for(int h=height; h >=0; h--) {
            for (int r = 1; r <= rows; r++) {
                int run=1;
                for (int c = 1; c <= cols; c++) {
                    if (lawn[r][c] > h) {
                        run = 0;
                    }
                }
                
                for (int c = 1; run == 1 && c <= cols; c++) {
                    if(lawn[r][c] == h){
                        visited[r][c] = 1;    
                    }                    
                }
            }            
        }

        for(int h=height; h >=0; h--) {
            for (int c = 1; c <= cols; c++) {
                int run=1;
                for (int r = 1; r <= rows; r++) {
                    if (lawn[r][c] > h) {
                        run = 0;
                    }
                }
                
                for (int r = 1; run == 1 && r <= rows; r++) {
                    if(lawn[r][c] == h){
                        visited[r][c] = 1;    
                    }                    
                }
            }            
        }

        int workable=1;
        for (int r = 1; r <= rows; r++) {
            for (int c = 1; c <= cols; c++) {
                if (visited[r][c] == 0) {
                    workable = 0;
                }
            }
        }        
        
        cout << "Case #" << i << ": " << (workable == 1 ? "YES": "NO") << endl;
//        
//        if(workable == 0) {
//            for (int r = 1; r <= rows; r++) {
//                for (int c = 1; c <= cols; c++) {
//                    cout << visited[r][c] << " ";
//                }
//                cout << endl;
//            }
//        }
    }
    return 0;
}

