#include <iostream>
#include <fstream>
using namespace std;

ifstream fin;
ofstream fout;
int t, sh;
string lev;

int main()
{
    fin.open("test.in");
    fin >> t;
    fout.open("test.out");

    for (int i=0; i<t; ++i)
    {
        int cum = 0;
        int fr = 0;
        fin >> sh;
        fin >> lev;
        for (int k=0; k<=sh; ++k)
        {
            int num = lev[k]-'0';
            if (num != 0) {
                if (k <= cum)
                {
                    cum += num;
                }
                else
                {
                    fr += (k - cum);
                    cum = k + num;
                }
            }
        }
        fout << "Case #" << i+1 << ": " << fr << endl;
    }

    fout.close();
    fin.close();
    return 0;
}
