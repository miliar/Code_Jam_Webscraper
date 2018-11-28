#include <iostream>
#include <fstream>

using namespace std;

int main()
{
    ifstream fin;
    fin.open("D-small-attempt0.in");
    ofstream fout;
    fout.open("output.txt");

    int t;
    fin >> t;
    for (int o = 1; o <= t; ++o)
    {
        int x, r, c, i;
        fin >> x >> r >> c;
        fout << "Case #" << o << ": ";
        if (x == 1) fout << "Gabriel";
        if (x == 2 && r * c % 2) fout << "Richard";
        else if (x == 2) fout << "Gabriel";
        if (x == 3 && !(r * c % 3) && r * c != 3) fout << "Gabriel";
        else if (x == 3) fout << "Richard";
        if (x == 4 && (r * c == 12 || r * c == 16)) fout << "Gabriel";
        else if (x == 4) fout << "Richard";
        fout << endl;
    }
    fin.close();
    fout.close();
}
