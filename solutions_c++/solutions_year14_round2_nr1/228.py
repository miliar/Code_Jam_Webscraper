#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <string>
#include <algorithm>
using namespace std;

int main() {
    cout.setf(ios_base::fixed);
    cout.precision(7);
    int T;
    cin >> T;
    for (int ti = 1; ti <= T; ++ti) {
        cout << "Case #" << ti << ": ";
        int n;
        cin >> n;
        vector< vector< pair< char, int > > > words(n);
        cin.ignore();
        for (int j = 0; j < n; ++j) {
            string s;
            getline(cin, s);
            for (int i = 0, count; i < s.size(); i += count) {
                count = 1;
                while (i + count < s.size() && s[i] == s[i + count]) {
                    count += 1;
                }
                words[j].push_back(make_pair(s[i], count));
                // cout << s[i] << count << " ";
            }
            // cout << endl;
        }
        bool possible = true;
        for (int j = 1; j < n; ++j) {
            if (words[j].size() != words[0].size()) {
                possible = false;
                break;
            }
        }
        int ans = 0;
        for (int i = 0; i < words[0].size() && possible; ++i) {
            char c = words[0][i].first;
            int min_count = words[0][i].second;
            int max_count = words[0][i].second;
            for (int j = 1; j < n; ++j) {
                if (words[j][i].first != c) {
                    possible = false;
                    break;
                }
                min_count = min(min_count, words[j][i].second);
                max_count = max(max_count, words[j][i].second);
            }
            ans += max_count - min_count;
        }
        if (possible) {
            cout << ans;
        }
        else {
            cout << "Fegla Won";
        }
        cout << "\n";
    }
    return 0;
}
