#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int isXorT (char a){
    if (a == 'X' || a == 'T') {
        return 1;
    }
    return 0;
}

int isOorT (char a){
    if (a == 'O' || a == 'T') {
        return 1;
    }
    return 0;
}

int checkArray (char a[4][4]) {
    for (int i=0; i<4; i++) {
        // check if X won
        // rows
        if (isXorT(a[i][0]) && isXorT(a[i][1]) && isXorT(a[i][2]) && isXorT(a[i][3]) ) {
            return 0;
        } 
        // columns
        if (isXorT(a[0][i]) && isXorT(a[1][i]) && isXorT(a[2][i]) && isXorT(a[3][i]) ) {
            return 0;
        } 
        // check if O won
        // rows
        if (isOorT(a[i][0]) && isOorT(a[i][1]) && isOorT(a[i][2]) && isOorT(a[i][3]) ) {
            return 1;
        } 
        // columns
        if (isOorT(a[0][i]) && isOorT(a[1][i]) && isOorT(a[2][i]) && isOorT(a[3][i]) ) {
            return 1;
        }
    }
    
    // diagnols
    if (isXorT(a[0][0]) && isXorT(a[1][1]) && isXorT(a[2][2]) && isXorT(a[3][3]) ) {
        return 0;
    }
    if (isOorT(a[0][0]) && isOorT(a[1][1]) && isOorT(a[2][2]) && isOorT(a[3][3]) ) {
        return 1;
    }
    if (isXorT(a[0][3]) && isXorT(a[1][2]) && isXorT(a[2][1]) && isXorT(a[3][0]) ) {
        return 0;
    }
    if (isOorT(a[0][3]) && isOorT(a[1][2]) && isOorT(a[2][1]) && isOorT(a[3][0]) ) {
        return 1;
    }
    
    // check for incomplete game
    for (int i=0; i<4; i++) {
        for (int j=0; j<4; j++) {
            if (a[i][j]=='.') {
                return 2;
            }
        }
    }
    
    // otherwise draw
    return 3;
}

int main () {
    string line;
    ifstream infile ("data.txt");
    ofstream outfile;
    outfile.open ("output.txt");
    
    if (infile.is_open())
    {
        // get number of cases
        int cases;
        if (infile.good()) {
            getline (infile,line);
            cases = atoi(line.c_str());
        }
        
        // for each case
        for (int i=1; i<=cases; i++) {
            char grid[4][4];
            
            // get four lines and store them in a 4x4 char array
            for (int j=0; j<4; j++) {
                if (infile.good())
                {
                    getline (infile,line);
                    grid[j][0] = line[0];
                    grid[j][1] = line[1];
                    grid[j][2] = line[2];
                    grid[j][3] = line[3];
                }
            }

            // check array for game state
            int k = checkArray(grid);
            
            string result;
            switch (k) {
                case 0:
                    result = "X won"; 
                    break;
                case 1:
                    result = "O won";
                    break;
                case 2:
                    result = "Game has not completed";
                    break;
                case 3:
                    result = "Draw";
                    break;
                default:
                    result = "Failed to get k";
                    break;
            }
            
            // write output
            if (outfile.is_open()) {
                outfile << "Case #" << i << ": " << result << "\n";
            }
            
            // for new line between each case
            getline (infile,line);
        }
        
        outfile.close();
        infile.close();
    }
    
    else cout << "Unable to open file";
    
    return 0;
}