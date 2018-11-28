#include <vector>
#include <algorithm>
#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main()
{
//    ifstream fin("input.in");
    //ifstream fin("B-small-attempt0.in");
    ifstream fin("B-large.in");
    ofstream fout("output.out");

    //-- check if the files were opened successfully
    if (!fin.is_open()) cout << "input.in was not opened successfully" << endl;
    if (!fout.is_open()) cout << "output.out was not open successfully" << endl;
    int numCase;
    fin >> numCase;

    int smax = 0;
    std::string audience;
    for (int i = 0; i < numCase; i++)
    {
        std::string inp;
        fin >> inp;
        int ans = 0;
        if (inp[inp.size()-1] == '-') ans++;
        for (int i = 0; i < inp.size() - 1; i++ )
        {
            if (inp[i] != inp [i+1]) ans++;
        }

        fout << "Case #" << (i + 1) << ": " << ans << endl;
    }
    fin.close();
    fout.close();
    return 0;
}
