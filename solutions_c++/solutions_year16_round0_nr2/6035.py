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

    string input[amount];
    for (int i = 0; i < amount; i++)
    {
            fin >> input[i];
    }

    int flips = 0;
    for (int i = 0; i < amount; i++)
    {
        flips = 0;
        bool face = true, start;
        string cakes = input[i];

        for(int j = 0; j <= input[i].size(); j++)
        {
            if(j == 0 && (cakes[0] == '+'))
            {
                flips++;
                face = true;
            }
            else if(cakes[j] == '+' && face == false)
            {
                flips++;
                face = true;
            }
            else if(cakes[j] == '-' && face == true)
            {
                flips++;
                face = false;
            }
        }
        if(face == true) flips--;
        if(flips < 0)
        {
            flips = 0;
        }
        fout << "Case #" << i+1 << ": " << flips << endl;
    }

    return 0;
}
