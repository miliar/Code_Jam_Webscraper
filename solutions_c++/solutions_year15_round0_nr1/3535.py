#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <sstream>
#include <algorithm>

using namespace std;

int main()
{
    ifstream in("in.txt");
    ofstream out("out.txt");

    int t;
    in >> t;

    for(int i = 0; i < t; ++i)
    {
        int smax;
        string digits;

        in >> smax >> digits;

        int needed = 0;
        int clapping = 0;
        for(int j = 0; j <= smax; ++j)
        {
            if(j > clapping)
            {
                needed += j - clapping;
                clapping = j;
            }
            clapping += digits[j] - '0';
        }

        out << "Case #" << i + 1 << ": " << needed << endl;
    }

    return 0;
}

