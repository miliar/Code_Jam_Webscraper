#include <iostream>
#include <fstream>
#include <cstring>
using namespace std;
int T, sol, n;
string S;

int main()
{
    ifstream fin("input.in");
    ofstream fout("output.out");
    fin >> T;
    for(int t = 1; t <= T; ++t)
    {
        fin >> S;
        n = S.size();
        sol = 0;
        int i = 0;
        bool before = false;
        while(i < n)
        {
            if(S[i] == '+')
            {
                before = true;
                i++;
                continue;
            }
            while(i < n && S[i] == '-')
                i++;
            if(before)
                sol += 2;
            else
            {
                sol++;
                before = true;
            }
        }
        fout << "Case #" << t << ": " << sol << "\n";
    }
    fin.close();
    fout.close();
    return 0;
}


