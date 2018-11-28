#include <iostream>
#include <sstream>
#include <algorithm>
#include <fstream>
#include <set>
#include <queue>
#include <vector>
#include <map>
#include <cmath>

using namespace std;

int main() {
#define int long long
    ifstream cin("A-small-attempt1.in");
    ofstream cout("out.txt");
    int T;
    cin >> T;
    for (int t = 1; t <= T; t++) {
        int N = 0, M = 0;
        cin >> N >> M;
        vector<pair<pair<int, int>, int> > oep(M);
        for (int i = 0; i < M; i++)
            cin >> oep[i].first.first >> oep[i].first.second >> oep[i].second;
        sort(oep.begin(), oep.end());
        int cost = 0;
        for (int i = 0; i < M; i++) {
            int dist = oep[i].first.second - oep[i].first.first;
            int cur = dist * N - (dist - 1) * dist / 2;
            cur %= 1000002013;
            cost += cur * oep[i].second;
            // cout << "i: " << i << " " << oep[i].first.first << " " << oep[i].first.second << " " << oep[i].second << " " << cur << endl;
            cost %= 1000002013;
        }
        for (int i = 0; i < oep.size(); i++) {
            for (int j = i + 1; j < oep.size(); j++) {
                if (oep[i].first.first == oep[j].first.first)
                    continue;
                if (oep[i].first.second < oep[j].first.first)
                    continue;
                if (oep[i].first.second >= oep[j].first.second)
                    continue;
                //cout << "i: " << i << ", j: " << j << ", oep: " << oep.size() << endl;
                //cout << oep[i].first.first << " " << oep[i].first.second << " " << oep[i].second << endl;
                //cout << oep[j].first.first << " " << oep[j].first.second << " " << oep[j].second << endl;
                int count = min(oep[i].second, oep[j].second);
                oep[i].second -= count;
                oep[j].second -= count;
                pair<pair<int, int>, int> mx = oep[i];
                pair<pair<int, int>, int> mn = oep[i];
                mx.second = count;
                mx.first.second = oep[j].first.second;
                mn.second = count;
                mn.first.first = oep[j].first.first;
                if (oep[j].second == 0) {
                    oep.erase(oep.begin() + j);
                    j--;
                }
                oep.insert(upper_bound(oep.begin() + i, oep.end(), mx), 1, mx);
                oep.insert(upper_bound(oep.begin() + (j - 1), oep.end(), mn), 1, mn);
                if (oep[i].second == 0) {
                    oep.erase(oep.begin() + i);
                    i--;
                    break;
                }
            }
        }
        for (int i = 0; i < oep.size(); i++) {
            int dist = oep[i].first.second - oep[i].first.first;
            int cur = dist * N - (dist - 1) * dist / 2;
            // cout << "fin: " << i << " " << oep[i].first.first << " " << oep[i].first.second << " " << oep[i].second << " " << cur << endl;
            cur %= 1000002013;
            oep[i].second %= 1000002013;
            cost -= cur * oep[i].second;
            while (cost < 0)
                cost += 1000002013;
        }
        cout.precision(15);
        cout << "Case #" << t << ": ";
        cout << cost;
        cout << endl;
    }
}

