#include <iostream>
#include <vector>
#include <string>

using namespace std;

constexpr int kMaxS = 1001;

int MinFriends(const vector<int> &counts) {
    int total = counts[0];
    int extra = 0;

    for (int i = 1; i < int(counts.size()); ++i) {
        if (total < i) {
            extra += i - total;
            total = i;
        }
        total += counts[i];
    }
    return extra;
}

int main() {
    cin.sync_with_stdio(false);

    int num_tests, s_max;
    cin >> num_tests;
    vector<int> counts;
    string chars;
    for (int t = 1; t <= num_tests; ++t) {
        cin >> s_max;
        cin >> chars;
        for (int s = 0; s <= s_max; ++s) {
            counts.push_back(chars[s] - '0');
        }
        cout << "Case #" << t << ": " << MinFriends(counts) << "\n";
        counts.clear();
    }
    return 0;
}
