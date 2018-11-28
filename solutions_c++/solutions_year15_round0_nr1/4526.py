#include <fstream>
#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main (void)
{
    ifstream in("A.in");
    ofstream out("A.op");

    cout.rdbuf(out.rdbuf());

    int T;
    in >> T;

    for (int t = 1; t <= T; t++)
    {
        int Smax;
        in >> Smax;

        string s;

        in >> s;  

        vector<int> S(Smax + 1);

        for (int i = 0; i < Smax+1; i++)
        {
            S[i] = s[i] + - '0';
        }

        vector<int> cum(Smax+1);
        
        cum[0] = S[0];

        int maxNeeded = 1 - cum[0];

        for (int i = 1; i < Smax; i++)
        {
            cum[i] = cum[i-1] + S[i];     

            int needed = i+1 - cum[i];
            if (needed > maxNeeded)
            {
                maxNeeded = needed;
            }
        }

        if (maxNeeded < 0) maxNeeded = 0;
        
        cout << "Case #" << t << ": " << maxNeeded << endl;

    }    

    return 0;
}
