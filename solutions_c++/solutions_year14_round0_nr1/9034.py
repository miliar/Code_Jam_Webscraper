#include <iostream>
#include <iomanip>
#include <fstream>

using namespace std;

int commonElements(int* row1, int* row2) {
    int common = 0;
    int numFound = 0;
    // 0 is not found yet
    // 0 is magician cheated
    for(int j = 0; j < 4; j++) {
        for(int k = 0; k < 4; k++) {
            if(row1[j] == row2[k])
            {
                common = row1[j];
                numFound++;
            }
        }
    }

    if(numFound == 1)
        return common;
    else if(numFound == 0) {
        // volunteer cheated
        return 0;
    } else {
        return -1;
        // bad magician
    }
}

int main(int argc, char** argv) {
    int numTests;
    ifstream in(argv[1]);
    ofstream out("output.out");
    in >> numTests;

    for(int i = 0; i < numTests; i++) {
        int choice1;
        in >> choice1;
        choice1--;
        int row1[4];
        int row2[4];
        int temp;
        for(int j = 0; j < 4; j++)
        {
            for(int k = 0; k < 4; k++) {
                if(j == choice1) {
                    in >> row1[k];
                } else {
                    in >> temp;
                }
            }
        }
        int choice2;
        in >> choice2;
        choice2--;
        for(int j = 0; j < 4; j++)
        {
            for(int k = 0; k < 4; k++) {
                if(j == choice2) {
                    in >> row2[k];
                } else {
                    in >> temp;
                }
            }
        }

        // row1 has answers from first time
        // row2 has answers from second time
        // find common elements
        int returnVal = commonElements(row1, row2);
        if(returnVal >= 1)
            out << "Case #" << (i+1) << ": " << returnVal << '\n';
        else if(returnVal == 0) {
            // volunteer cheated
            out << "Case #" << (i+1) << ": Volunteer cheated!\n";
        } else {
            // bad magician
            out << "Case #" << (i+1) << ": Bad magician!\n";
        }   
    }       

    out.close();

    return 0;
}
