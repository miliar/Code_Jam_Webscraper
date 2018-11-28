#include <iostream>
#include <fstream>
using namespace std;

int main()
{
    ifstream in("../MagicTrick/A-small-attempt1.in");

    if(!in.is_open())
    {
        cerr << "Could not open textfile!" << endl;
        return 1;
    }

    int testCases;
    in >> testCases;

    int row[testCases * 2], rows[testCases * 2][4][4];
    int i = 0;
    while(!in.eof())
    {
        in >> row[i];
        in >> rows[i][0][0] >> rows[i][0][1] >> rows[i][0][2] >> rows[i][0][3];
        in >> rows[i][1][0] >> rows[i][1][1] >> rows[i][1][2] >> rows[i][1][3];
        in >> rows[i][2][0] >> rows[i][2][1] >> rows[i][2][2] >> rows[i][2][3];
        in >> rows[i][3][0] >> rows[i][3][1] >> rows[i][3][2] >> rows[i][3][3];
        i++;
    }

    ofstream out("A-small-attempt0.out");

    int countEq = 0;
    int tmp;
    int cnt = 0;
        for(int j = 0; j < testCases * 2; j = j + 2)
        {
            for(int k = 0; k < 4; k++)
            {
                for(int m = 0; m < 4; m++)
                {
                    //cout << rows[j][row[j] - 1][k] << "\t" << rows[j + 1][row[j + 1] - 1][m] << endl;
                    if(rows[j][row[j] - 1][k] == rows[j + 1][row[j + 1] - 1][m])
                    {
                        countEq++;
                        tmp = rows[j][row[j] - 1][k];
                    }
                }
            }
            if(countEq == 1)
            {
                out << "Case #" << j / 2 + 1 << ": " << tmp << endl;
            }

            if(countEq > 1)
            {
                out << "Case #" << j / 2 + 1 << ": Bad magician!" << endl;
            }
            if(countEq == 0)
            {
                out << "Case #" << j / 2 + 1 << ": Volunteer cheated!" << endl;
            }
            countEq = 0;
        }
    return 0;
}

