#include <iostream>
#include <stdlib.h>
#include <fstream>

using namespace std;

int toInt(char);

int main()
{
    ifstream fin("A-large.in");
    ofstream fout("output.txt");

    int T;
    int smax; // highest shyness level
    string s;    // audience
    int n;    // number of friends to invite
    int si;   // number of friends with shyness level i
    int total; // number of people in audience

    if(fin.is_open())
    {
        fin >> T;

        for(int t = 1; t <= T; t++)
        {
            n = 0;
            total = 0;
            si = 0;

            fin >> smax;
            fin >> s;

            for(int i = 0; i <= smax; i++)
            {
                si = toInt(s[i]);
                total += si;
                while(total <= i)
                {   ; ++n;  ++total;    }
            }

            fout << "Case #" << t << ": " << n << endl;
        }


    } else cout << "Failed to open input file.";

    return 0;
}

int toInt(char c)
{
    switch(c)
    {
        case '0': return 0; break;
        case '1': return 1; break;
        case '2': return 2; break;
        case '3': return 3; break;
        case '4': return 4; break;
        case '5': return 5; break;
        case '6': return 6; break;
        case '7': return 7; break;
        case '8': return 8; break;
        case '9': return 9; break;
    }
}
