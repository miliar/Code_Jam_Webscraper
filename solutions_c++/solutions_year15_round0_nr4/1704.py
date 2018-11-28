#include <iostream>
#include <fstream>

using namespace std;

int main()
{
    ifstream input("input.txt");
    ofstream output("output.txt");
    int nbTests = 0;

    input >> nbTests;

    int X, R, C;

    bool richardWins = false;

    for(int i = 0 ; i < nbTests ; i++)
    {
        input >> X >> R >> C;

        richardWins = false;

        if(R*C % X != 0)
            richardWins = true;
        else
        {
            int x = X, y = 1;

            while(x >= y)
            {
                if(!((x <= R && y <= C) || (x <= C && y <= R))) // Can Richard find an omino that doesn't fit the grid ?
                {
                    richardWins = true;
                    break;
                }
                else if(x != 1 && y != 1 && !((x < R && y < C) || (x < C && y < R)) && x % R != 0 && x % C != 0)
                {
                    richardWins = true;
                    break;
                }

                x--;
                y++;
            }
        }

        output << "Case #" << i+1 << ": " << ((richardWins) ? "RICHARD" : "GABRIEL") << endl;

    }

    input.close();
    output.close();

    return 0;
}
