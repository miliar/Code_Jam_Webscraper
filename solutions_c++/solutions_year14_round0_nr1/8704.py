#include <iostream>
#include <string>
#include <fstream>
using namespace std;

int main()
{
    string str;    // string from file
    ifstream fin;  // input file
    ofstream fout; // output file
    int T;         // number of test cases
    const int ROWS = 4;
    const int COLS = 4;
    int cards1[ROWS][COLS] = {0,0,0,0, 0,0,0,0, 0,0,0,0, 0,0,0,0};
    int cards2[ROWS][COLS] = {0,0,0,0, 0,0,0,0, 0,0,0,0, 0,0,0,0};
    int row1 = 0;
    int row2 = 0;
    int card = 0;
    int found = 0;
    fin.open("A-small-attempt0.in");
    fout.open("A-small-attempt0.out");
    fin >> T;
    for(int i=0; i<T; i++)
    {
        fin >> row1;
        for(int j=0; j<ROWS; j++)
        {
            fin >> cards1[j][0] >> cards1[j][1] >> cards1[j][2] >> cards1[j][3];
        }
        fin >> row2;
        for(int j=0; j<ROWS; j++)
        {
            fin >> cards2[j][0] >> cards2[j][1] >> cards2[j][2] >> cards2[j][3];
        }

        for(int k=0; k<COLS; k++)
        {
            for(int l=0; l<COLS; l++)
            {
                if(cards1[row1-1][k]==cards2[row2-1][l]){
                    card = cards1[row1-1][k];
                    found += 1;
                }
            }
        }

        fout << "Case #" << i+1 << ": ";
        if(card!=0)
        {
            if(found==1){
                fout << card << endl;
            }
            if(found>1){
                fout << "Bad magician!" << endl;
            }
            card = 0;
            found = 0;
        }
        else
        {
            fout << "Volunteer cheated!" << endl;
        }
    }
    fin.close();

    return 0;
}
