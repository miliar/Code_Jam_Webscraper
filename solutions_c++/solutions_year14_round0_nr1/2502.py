#include <iostream>
#include <fstream>
using namespace std;

int main () {
    ifstream read("input.txt");
    ofstream myfile;
    myfile.open("output.txt");
    int t; // Number of test cases
    int r1, r2;
    int square[5][5];
    bool first[17];
    bool second[17];
    int rs, count;
    read >> t;
    for (int z = 0; z < t; z++)
    {
        for (int i = 0; i < 17; i++)
        {
            first[i] = false;
            second[i] = false;
        }
        read >> r1;
        for (int i = 1; i < 5; i++)
            for (int j = 1; j < 5; j++)
                read >> square[i][j];
        for (int j = 1; j < 5; j++)
            first[square[r1][j]] = true;
        read >> r2;
        for (int i = 1; i < 5; i++)
            for (int j = 1; j < 5; j++)
                read >> square[i][j];
        for (int j = 1; j < 5; j++)
            second[square[r2][j]] = true;
            
        rs = -1;
        count = 0;
        for (int i = 1; i < 17; i++)
            if (first[i] && second[i])
            {
               count = count + 1;
               rs = i;
            }
        myfile << "Case #" << (z+1) << ": ";
        if (count == 1)
           myfile << rs;
        else if (count == 0)
           myfile << "Volunteer cheated!";
        else 
           myfile << "Bad magician!";
        myfile << "\n";
    }
    myfile.close();
}
