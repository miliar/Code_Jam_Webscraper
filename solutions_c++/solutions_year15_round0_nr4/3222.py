#include <iostream>
#include <fstream>
#include <string>
#include <stdlib.h>

using namespace std;

int main () {
    
    ifstream input ("D-small-attempt2.in.txt");
    ofstream output ("output.txt");
    
    unsigned int count = 0;
    input >> count; cout << count << endl;

    unsigned int size, row, col;
    unsigned int grid;
    
    bool richard;
    
    for (unsigned int i = 1; i <= count; i++) {

        richard = 0;
        
        input >> size;
        input >> row;
        input >> col;
        
        grid = row * col;
        
        if (size > row && size > col) {
            richard = 1;
        }
        
        if (size > 2*row || size > 2*col) {
            richard = 1;
        }
        
        if (grid % size) {
            richard = 1;
            
        } else {
            if (grid == size && size > 2) {
                richard = 1;
                
            } else if (grid == 2*size) {
                if (size > 3) {
                    richard = 1;
                }
            }
        }
        
        
        if (richard) {
            cout << size << " " << row << " " << col << " RICHARD" << endl;
            output << "Case #" << i << ": " << "RICHARD" << endl;
        } else {
            cout << size << " " << row << " " << col << " GABRIEL" << endl;
            output << "Case #" << i << ": " << "GABRIEL" << endl;
        }
    }

    return 0;
}
