#include <bits/stdc++.h>
using namespace std;
#define PII pair<int, int>

int main() {
    ifstream cin("testC.in");
    ofstream cout("testC2.out");

    int t; cin >> t;
    for(int t_case = 1; t_case <= t; ++t_case) {
        cout << "Case #" << t_case << ": ";
        int n; cin >> n;
        vector<PII> hikers;
        for(int i = 0; i < n; ++i) {
            int starting; cin >> starting;
            int number; cin >> number;
            int fastest; cin >> fastest;
            for(int j = 0; j < number; ++j)
                hikers.push_back(make_pair(starting, fastest + j));
        }

        sort(hikers.begin(), hikers.end());
        if(hikers[1].second == hikers[0].second) {
            cout << 0 << "\n";
            continue;
        }
        int fastest = 0;
        if(hikers[1].second < hikers[0].second)
            fastest = 1;

        int ans = 1;

            double timeOther = (hikers[1 - fastest].second + 0.0) / 360.0 * (360 - hikers[1 - fastest].first);
            double traveledByFastest = timeOther * (360.0 / hikers[fastest].second);
            if(hikers[fastest].first + traveledByFastest >= 2 * 360)
                ans = 1;
            else 
                ans = 0;
        
        cerr << traveledByFastest << "\n";
        cout << ans << "\n";
    }
}
