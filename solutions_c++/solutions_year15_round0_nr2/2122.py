#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <climits>
#include <cstring>
#include <string>
#include <vector>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <algorithm>

using namespace std;

int main()
{
    int T, n, tmp;
    int minPeriod, maxPeriod;
    vector<int> v;
    cin >> T;
    for(int t=1; t <= T; ++t)
    {
        cin >> n;
        maxPeriod = 0;
        for(int j=0; j < n; ++j)
        {
            cin >> tmp;
            v.push_back(tmp);
            maxPeriod = max(maxPeriod, tmp);
        }
        minPeriod = maxPeriod;

        for(int i=1; i <= maxPeriod; ++i)
        {
            int extraMinutes = 0;
            for(int j=0; j < n; ++j)
            {
                extraMinutes += (v[j] - 1) / i;
            }
            minPeriod = min(minPeriod, extraMinutes + i);
        }
        
        cout << "Case #" << t << ": " << minPeriod << endl;
        v.clear();
    }

    return 0;
}
