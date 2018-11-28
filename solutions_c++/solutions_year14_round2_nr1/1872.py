#include <fstream>
#include <algorithm>
#include <vector>
using namespace std;

ifstream in("input-a.txt");
ofstream out("output-a.txt");

int solve() {
    int n, ans = 0;
    string s;
    vector<pair<char, int> > v[105];
    in >> n;
    for (int i = 0; i < n; i++) {
        in >> s;
        for (int j = 0; j < s.size(); j++) {
            if (j == 0 || s[j] != s[j - 1]) {
                v[i].push_back(make_pair(s[j], 1));
            } else {
                v[i].back().second++;
            }
        }
    }
    for (int i = 1; i < n; i++)
        if (v[i].size() != v[i - 1].size()) {
            return -1;
        }
    for (int ind = 0; ind < v[0].size(); ind++)
        for (int j = 1; j < n; j++)
            if (v[j][ind].first != v[j - 1][ind].first) {
                return -1;
            }
    for (int ind = 0; ind < v[0].size(); ind++) {
        int sum = 0;
        for (int i = 0; i < n; i++) {
            sum += v[i][ind].second;
        }
        sum /= n;
        for (int i = 0; i < n; i++) {
            ans += abs(sum - v[i][ind].second);
        }
    }
    return ans;
}

int main() {
    int t;
    in >> t;
    for (int tt = 0; tt < t; tt++) {
        int f = solve();
        out << "Case #" << tt + 1 << ": ";
        if (f != -1) {
            out << f;
        } else {
            out << "Fegla Won";
        }
        out << '\n';
    }
    return 0;
}
