#include <fstream>
#include <string>
#include <vector>
#include <set>
#include <queue>
#include <algorithm>
#include <iostream>
#include <cstdlib>

using namespace std;


enum WINNER{RI, GA, NA};

int main()
{
    int T;

    //ifstream fin("C:\\weilin\\Competition\\GCJ2015\\GCJ2015\\input.txt");
    ifstream fin("C:\\weilin\\Competition\\GCJ2015\\GCJ2015\\D-small-attempt2.in");
    ofstream fout("output.txt");

    fin >> T;    
    
    for (int i = 0; i < T; i++)
    {
        int X, R, C;
        fin >> X >> R >> C;
        WINNER w = NA;


        if (R * C < X)
        {
            w = RI;
        }
        else if ((R * C) % X != 0)
        {
            w = RI;
        }
        else if (X == 1)
        {
            w = GA;
        } 
        else if (X == 2)
        {
            w = GA;
        } 
        else if (X == 3)
        {
            if ((R == 1 && C == 3) || (R == 3 && C == 1))
            {
                w = RI;
            } 
            else if ((R == 2 && C == 3) || (R == 3 && C == 2))
            {
                w = GA;
            } 
            else if (R == 3 && C == 3)
            {
                w = GA;
            }
            else if ((R == 4 && C == 3) || (R == 3 && C == 4))
            {
                w = GA;
            }
        }
        else if (X == 4)
        {
            if ((R == 1 && C == 4) || (R == 4 && C == 1))
            {
                w = RI;
            }
            else if ((R == 2 && C == 4) || (R == 4 && C == 2))
            {
                w = RI;
            }
            else if (R == 2 && C == 2)
            {
                w = RI;
            }
            else if (R == 4 && C == 4)
            {
                w = GA;
            }
            else if ((R == 4 && C == 3) || (R == 3 && C == 4))
            {
                w = GA;
            }
        }

        //fout << X << " " << R << " " << C << " ";

        if (w == RI)
          fout << "Case #" << i + 1 << ": " << "RICHARD" << endl;
        else if (w == GA)
          fout << "Case #" << i + 1 << ": " << "GABRIEL" << endl;

    }
    return 0;
}