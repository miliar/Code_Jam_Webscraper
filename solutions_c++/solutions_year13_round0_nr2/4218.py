#include <stdio.h>
#include <iostream>
#include <fstream>
#include <vector>
using namespace std;

bool compare(vector< vector<int> > &desiredLawn, vector< vector<int> > &currentLawn);
void print(vector< vector<int> > &currentLawn);
vector<int> mow(vector<int> toMow, int maxHeight);

const int INIT_HEIGHT = 100;

int main(void) {
    ofstream out;
    out.open("b.out");
    
    int T;
    cin >> T;

    for(int i = 0; i < T; i++) {
        int N, M;
        
        cin >> N;
        cin >> M;
        
        vector< vector<int> > desiredLawn;
        vector< vector<int> > startLawn;
        
        for(int j = 0; j < N; j++) {
            vector<int> row;
            vector<int> startRow;
            
            for(int k = 0; k < M; k++) {
                int desiredHeight;
                cin >> desiredHeight;
                
                row.push_back(desiredHeight);
                startRow.push_back(INIT_HEIGHT);
            }
            
            desiredLawn.push_back(row);
            startLawn.push_back(startRow);
        }
        
        string response = "";
        bool cont = true;
        while (cont) {
            vector< vector<int> > currentLawn = startLawn;
            int cols = 0;
            
            for(int a = 0; a < currentLawn.size(); a++){
                vector<int> row;
                cols = currentLawn[a].size();
                int maxHeightRow = 0;
                
                for(int b = 0; b < currentLawn[a].size(); b++) {
                    row.push_back(currentLawn[a][b]);
                    if(desiredLawn[a][b] > maxHeightRow)
                        maxHeightRow = desiredLawn[a][b];
                }
                
                vector<int> newRow = mow( row, maxHeightRow );
                
                for (int c = 0; c < currentLawn[a].size(); c++) {
                    currentLawn[a][c] = newRow[c];
                }
            }
            
            for(int b = 0; b < cols; b++) {
                vector<int> col;
                int maxHeightCol = 0;
                for (int c = 0; c < currentLawn.size(); c++) {
                    col.push_back( currentLawn[c][b] );
                    if( desiredLawn[c][b] > maxHeightCol )
                        maxHeightCol = desiredLawn[c][b];
                }
                
                vector<int> newCol = mow(col, maxHeightCol);
                
                for (int c = 0; c < currentLawn.size(); c++) {
                    currentLawn[c][b] = newCol[c];
                }
            }

            if (compare(desiredLawn, currentLawn))
                response = "YES";
            else
                response = "NO";
            
            cont = false;
        }
        
        out << "Case #" << i+1 << ": " << response << endl;
    }
    
    return 0;
}

bool compare(vector< vector<int> > &desiredLawn, vector< vector<int> > &currentLawn) {
    for(int a = 0; a < currentLawn.size(); a++){
        for(int b = 0; b < currentLawn[a].size(); b++) {
            if(currentLawn[a][b] != desiredLawn[a][b]) {
                return false;
            }
        }
    }
    
    return true;
}
void print(vector< vector<int> > &currentLawn) {
    for(int a = 0; a < currentLawn.size(); a++){
        for(int b = 0; b < currentLawn[a].size(); b++) {
            cout << currentLawn[a][b] << " ";
        }
        cout << endl;
    }
}

vector<int> mow(vector<int> toMow, int maxHeight) {
    for(int i = 0; i < toMow.size(); i++) {
        if(toMow[i] > maxHeight)
            toMow[i] = maxHeight;
    }
    
    return toMow;
}