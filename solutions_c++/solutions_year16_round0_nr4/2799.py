#include <vector>
#include <algorithm>
#include <iostream>
#include <fstream>

using namespace std;


int main()
{
    //ifstream fin("input.in");
    ifstream fin("D-small-attempt0.in");
    //ifstream fin("D-large.in");
    ofstream fout("output.out");

    if (!fin.is_open()) cout << "input.in open fail" << endl;
    if (!fout.is_open()) cout << "output.out open fail" << endl;

    int numCase;
    fin >> numCase;

    int caise;
    for (caise = 0; caise < numCase; caise++)
    {
        int k, c, s;
        fin >> k;
        fin >> c;
        fin >> s;

        cout << endl << k << " " << c << " " << s << endl;

        cout << "Case #" << (caise + 1) << ": 1";
        fout << "Case #" << (caise + 1) << ": 1";
        for (int i = 1 ; i < k ; i++) {
            unsigned long long pos = i;
            for (int j = 1 ; j < c ; j++) {
                pos *= k;
            }
            cout << " " << pos +1 ;
            fout << " " << pos +1 ;
        }
        cout  << endl;
        fout  << endl;

    }

    fin.close();
    fout.close();
    return 0;
}
