#include <iostream>
#include <fstream>
#include <cmath>

using namespace std;

int main()
{
    ifstream fin("A-small-attempt2.in");
    ofstream fout("A-small-attempt2.out");

    int T;
    fin >> T;

    for(int caseNumber = 1; caseNumber <= T; caseNumber++)
    {
        long output = 0;
        long p, q;
        char slash;
        fin >> p >> slash >> q;
        if(log(q)/log(2) != ceil(log(q)/log(2)))
        {
            fout << "Case #" << caseNumber << ": " << "impossible" << endl;
            continue;
        }
        else
        {
            double div = (double)q / (double)p;
            long output = ceil(log(div) / log(2));

            fout << "Case #" << caseNumber << ": " << output << endl;
            continue;
        }
    }

    fin.close();
    fout.close();
}
