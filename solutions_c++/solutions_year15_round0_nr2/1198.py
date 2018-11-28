#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>

using namespace std;

ofstream fout("output2.txt");

int main()
{
    int T;
    cin >> T;	
    for (int t = 0; t < T; ++t)
    {
        int D;
        cin >> D;
        vector<int> P(D);
        for (int i = 0; i < D; ++i)
            cin >> P[i];

        sort(P.begin(), P.end());
        reverse(P.begin(), P.end());
        int maxP = P[0];
        int minTime = P[0];

        for (int all = 1; all < maxP; ++all)
        {
            int special = 0;
            for (int i = 0; P[i] > all && i < D; ++i)
            {
                special += P[i] / all - 1 + (P[i] % all == 0? 0: 1);
            }
            minTime = min(minTime, all + special);
        }

        fout << "Case #" << t + 1 << ": " << minTime << endl;
    }

	return 0;
}