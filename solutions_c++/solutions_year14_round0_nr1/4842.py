#include <iostream>
#include <stdio.h>
#include <fstream>

using namespace std;

int main()
{
    FILE* fin = fopen("A-small-attempt0.in","r");
    ofstream fout;
    fout.open("output.out");

    int numCases;
    fscanf(fin, "%d", &numCases);
    int temp1, temp2, temp3, temp4;

    for (int i = 0; i < numCases; i++){
        int currentFirstRow[4];
        int currentSecondRow[4];

        int place1 = 0;
        fscanf(fin, "%d\n", &place1);

        for (int j = 0; j < place1-1; j++){
            fscanf(fin, "%d %d %d %d\n", &temp1, &temp2, &temp3, &temp4);
        }

        fscanf(fin, "%d %d %d %d\n", &currentFirstRow[0], &currentFirstRow[1], &currentFirstRow[2], &currentFirstRow[3]);

        for (int j = 0; j < 4-place1; j++){
            fscanf(fin, "%d %d %d %d\n", &temp1, &temp2, &temp3, &temp4);
        }

        int place2;
        fscanf(fin, "%d\n", &place2);

        for (int j = 0; j < place2-1; j++){
            fscanf(fin, "%d %d %d %d\n", &temp1, &temp2, &temp3, &temp4);
        }

        fscanf(fin, "%d %d %d %d\n", &currentSecondRow[0], &currentSecondRow[1], &currentSecondRow[2], &currentSecondRow[3]);

        for (int j = 0; j < 4-place2; j++){
            fscanf(fin, "%d %d %d %d\n", &temp1, &temp2, &temp3, &temp4);
        }

        int numMatches = 0;
        int firstMatch;

        for (int k = 0; k < 4; k++) {
            for (int m = 0; m < 4; m++){
                if (currentFirstRow[k] == currentSecondRow[m]) {
                        numMatches++;
                        firstMatch = currentFirstRow[k];
                }
            }

        }

    if (numMatches > 1)
        fout << "Case #" << i+1 << ": " << "Bad magician!" << endl;
    else if (numMatches == 1)
        fout << "Case #" << i+1 << ": " << firstMatch << endl;
    else if (numMatches == 0)
        fout << "Case #" << i+1 << ": " << "Volunteer cheated!" << endl;
    }
    return 0;
}
