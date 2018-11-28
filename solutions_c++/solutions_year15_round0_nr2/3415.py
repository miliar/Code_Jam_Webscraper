#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <sstream>
#include <algorithm>

using namespace std;

int main()
{
    ifstream in("in.txt");
    ofstream out("out.txt");

    int t;
    in >> t;

    for(int i = 0; i < t; ++i)
    {
        int d;
        in >> d;

        vector<int> p;

        int maxp = 0;
        for(int j = 0; j < d; ++j)
        {
            int tmp;
            in >> tmp;
            p.push_back(tmp);
            maxp = max(maxp, tmp);
        }

        int minTurns = maxp;

        for(int eatTurns = 1; eatTurns < maxp; ++eatTurns)
        {
            int specTurns = 0;
            for(int k = 0; k < d; ++k)
            {
                specTurns += (p[k] - 1) / eatTurns;
            }
            minTurns = min(minTurns, specTurns + eatTurns);
        }

        out << "Case #" << i + 1 << ": " << minTurns << endl;
    }

    return 0;
}

