#include <iostream>
#include <vector>

using namespace std;

int main()
{
    int T = 0;
    cin >> T;
    for (int i = 0; i < T; ++i)
    {
        int D = 0;
        cin >> D;
        vector<int> plates;
        int maxP = 0;
        for (int j = 0; j < D; ++j)
        {
            int p = 0;
            cin >> p;
            plates.push_back(p);
            if (maxP < p)
            {
                maxP = p;
            }
        }

        int minMinuteCount = maxP;
        for (int j = 2; j < maxP; ++j)
        {
            int sumMinute = 0;
            for (int k = 0; k < plates.size(); ++k)
            {
                sumMinute += (plates[k] - 1) / j;
            }
            sumMinute += j;
            if (minMinuteCount > sumMinute)
            {
                minMinuteCount = sumMinute;
            }
        }

        cout << "Case #" << i + 1 << ": " << minMinuteCount << endl;
    }
    return 0;
}
