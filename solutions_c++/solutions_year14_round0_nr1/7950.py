#include <iostream>
#include <vector>
#include <algorithm>
#include <fstream>
using namespace std;

int main()
{
    ifstream fin("input.txt");
    ofstream fout("output.txt");

    int T;

    fin >> T;
    int choice1, choice2;
    int cards[4][4];
    int answer[4];

    for (int k=0; k<T; k++) // test cases
    {
        fin >> choice1;

        for (int r=0; r<4; r++)
        {
            for (int c=0; c<4; c++)
            {
                if (r == choice1-1)
                    fin >> answer[c];
                else
                    fin >> cards[r][c];
            }
        }

        fin >> choice2;

        for (int r=0; r<4; r++)
        {
            for (int c=0; c<4; c++)
            {
                fin >> cards[r][c];
            }
        }

        int c = 0;
        int card = 0;

        for (int i=0; i<4; i++)
        {
            for (int l=0; l<4; l++)
            {
                if (answer[i] == cards[choice2-1][l])
                {
                    c++;
                    card = answer[i];
                }
            }
        }

        fout << "Case #" << k+1 << ": ";

        if (c == 1)
            fout << card;
        else if (c > 1)
            fout << "Bad magician!";
        else
            fout << "Volunteer cheated!";

        fout << endl;


    }

    return 0;
}
