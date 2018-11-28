/*
*/

#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <queue>
#include <algorithm>
using namespace std;

int minMinutes(vector<int> P, int remove) {
    sort(P.begin(), P.end(), greater<int>());
    int currMin = P.front();
    int usedMinutes = 0;
    while (P.front() > remove) {
        int maxV = P.front();
        P[0] = maxV - remove;
        P.push_back(maxV - P[0]);
        sort(P.begin(), P.end(), greater<int>());
        ++usedMinutes;
        currMin = min(currMin, usedMinutes + P.front());
    }
    return currMin;
}

int main(int argc, char *argv[])
{
    int T, D;
    cin >> T;
    for (int i = 0; i < T; ++i) {
        cin >> D;
        vector<int> P(D);
        for (int i = 0; i < D; ++i) cin >> P[i];
        int m1 = minMinutes(P, 2);
        int m2 = minMinutes(P, 3);
        int m3 = minMinutes(P, 4);
        cout << "Case #" << i + 1 << ": " << min(min(m1, m2), m3) << endl;
    }
    return 0;
}
