#include <iostream>
#include <string.h>
#include <math.h>
#include <fstream>

using namespace std;

int main()
{

    ifstream fin("input.in");
    ofstream fout("output.out");

    if (!fin.is_open()) cout << "BAD STUFF HAPPENED" << endl;;
    if (!fout.is_open()) cout << "MORE BAD STUFF" << endl;;

    int amount;
    fin >> amount;

    int input[amount][3];
    for (int i = 0; i < amount; i++)
    {
            fin >> input[i][0] >> input[i][1] >> input[i][2];
    }

    for (int i = 0; i < amount; i++)
    {
        if(input[i][0] > input[i][2])
        {
            fout << "Case #" << i + 1 << ": IMPOSSIBLE" << endl;
        }

        fout << "Case #" << i+1 << ": ";
        for(int j = 0; j < input[i][2]; j++)
        {
            fout << j + 1 << " ";
        }
        fout << endl;
    }

/*
    for (int i = 0; i < amount; i++)
    {
        if(input[i][0] > input[i][2])
        {
            cout << "Case #" << i + 1 << ": IMPOSSIBLE" << endl;
        }
        else if((input[i][0] * input[i][1]) == input[i][2])
        {
            cout << "Case #" << i + 1 << ": ";
            for(int j = 0; j < (input[i][0] * input[i][1]); j++)
            {
                cout << j + 1 << " ";
            }
            cout << endl;
        }
        else
        {
            cout << "Case #" << i + 1 << ": ";
            for(int j = 2; j < pow(input[i][0],input[i][1]);j*=3)
            {
                cout << j << " ";
            }
            cout << endl;
        }
    }

    //cout << input[0][1];
*/

    return 0;

}

