#include <iostream>
#include <fstream>
using namespace std;


int main(int argc, char * argv[])
{
    int cases = 0;

    int k = 1,
        c = 1,
        s = 0;

    // The places to check
    long long * ans = NULL;
    int caught = 0;

    ifstream fin("D-small-attempt0.in");
    ofstream fout("write3.txt");

    if(fin.is_open())
    {
        //cout << "Opened File." << endl;

        fin >> cases;

        for(int casenum = 1; casenum <= cases; casenum++)
        {
            fout << "Case #" << casenum << ": ";

            fin >> k;
            fin >> c;
            fin >> s;

            ans = new long long[k];
            for(int initialize = 0; initialize < k; initialize++)
            {
                ans[initialize] = initialize;
            }
            caught = k;

            for(int cycle = 0; cycle < c - 1; cycle++)
            {
                for(int enter = cycle + 1; enter < k; enter++)
                {
                    ans[enter] = ans[cycle] * k;
                    /*for(int power = 0; power < k; power++)
                    {
                        ans[enter] *= k;
                    }*/
                    ans[enter] += enter;
                }
                if(caught != 1)
                {
                    ans[cycle] = -1;
                    caught--;
                }

            }

            if(caught > s)
            {
                fout << "IMPOSSIBLE" << endl;
            }
            else
            {
                for(int out = 0; out < k; out++)
                {
                    if(ans[out] != -1)
                    {
                        fout << ans[out] + 1 << " ";
                    }
                }
                fout << endl;
            }
            delete[] ans;
        }

        fin.close();
        fout.close();
    }
    else
    {
        cout << "Could not open file." << endl;
    }

    return 0;
}
