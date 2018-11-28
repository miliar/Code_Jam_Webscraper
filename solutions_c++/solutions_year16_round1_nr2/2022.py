#include <bits/stdc++.h>

using namespace std;

int main() {
    int T;
    cin >> T;
    for (int t = 1; t <= T; t++) {
        unordered_map<int, int> count;

        int n; cin >> n;
        for(int i = 0; i < 2 * n - 1; i++) {
            for(int j = 0; j < n; j++) {
                int x; cin >> x;
                count[x]++;
            }
        }

        vector<int> coords;
        for(auto &it : count) {
            //cout << it.first << " -> " << it.second << endl;
            if((it.second & 1) == 1) {
                coords.push_back(it.first);
            }
        }
        sort(coords.begin(), coords.end());


        cout << "Case #" << t << ": ";
        string sep = "";
        for(size_t i = 0; i < coords.size(); i++) {
            cout << sep << coords[i];
            sep = " ";
        }
        cout << endl;
    }

    return 0;
}
