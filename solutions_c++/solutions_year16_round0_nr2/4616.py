#include <iostream>
#include <fstream>

using namespace std;

int main()
{
    ifstream fi ("B-large.in");
    ofstream fo ("output_large.txt");
    int t;
    fi >> t;
    string line;getline(fi, line);
    for (int o = 1; o <= t; ++o)
    {
        getline(fi, line);
        int d = line.size();
        int counter = 0;
        char c = '+';
        for (int i = d - 1; i >= 0; --i)
        {
            if (line[i] == c) continue;
            ++counter;
            c = line[i];
        }
        fo << "Case #" << o << ": " << counter << endl;
    }
}
