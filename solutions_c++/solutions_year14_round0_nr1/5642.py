#include <iostream>
#include <fstream>
using namespace std;

int main (int argc, char* args[]){
    ifstream infile;
    ofstream outfile;
    
    if (argc == 2 && strcmp(args[1], "small") == 0) {
        infile.open("small.in");
        outfile.open("small.out");
    }
    else if (argc == 2 && strcmp(args[1], "large") == 0) {
        infile.open("large.in");
        outfile.open("large.out");
    }
    
    int cases;
    infile >> cases;
    cout << cases << endl ;
    
    //algorithm
    
    int row1;
    int row2;
    int board1[4][4];
    int board2[4][4];
    int possibles[4];
    int results[4];
    
    for (int i=0; i<cases; ++i) {
        // read from file
        infile >> row1;
        
        for (int j=0; j<4; ++j) {
            for (int k=0; k<4; ++k) {
                infile >> board1[j][k];
            }
        }
        
        infile >> row2;
        
        for (int j=0; j<4; ++j) {
            for (int k=0; k<4; ++k) {
                infile >> board2[j][k];
            }
        }
        
        // algorithm
        
        for (int j=0; j<4; ++j) {
            possibles[j]= board1[row1-1][j];
        }
        
        for (int j=0; j<4; ++j) {
            results[j]= board2[row2-1][j];
        }
        int count = 0;
        int card;
        for (int j=0; j<4; ++j) {
            for (int k=0; k<4; ++k) {
                if(possibles[j]==results[k]){
                count++;
                    card = possibles[j];
                }
            }
        }
        outfile << "Case #" << i+1 << ": ";
        if (count == 0) outfile << "Volunteer cheated!" << endl;
        else if (count > 1) outfile << "Bad magician!" << endl;
        else if (count == 1)outfile << card << endl;
        
    }
    
    infile.close();
    outfile.close();
    
    return 0;
}
