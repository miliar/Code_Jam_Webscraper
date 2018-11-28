#include <iostream>
#include <fstream>

using namespace std;

int main()
{
    int t, x, r, c;
    bool richWins;
    ifstream fin("D-small-attempt0.in");
    fin >> t;
    for(int i=0; i<t; i++)
    {
        fin >> x >> r >> c;
        richWins = false;
        if(!((r*c)%x))
            if(r>=(x-1) && c>=(x-1))
                if(x%2 || !((r*c)%2))
                    richWins = true;
        cout<< "Case #" << i+1 << ": " << (richWins ? "GABRIEL" : "RICHARD") << "\n";
    }
    return 0;
}