#include <algorithm>
#include <bitset>
#include <cctype>
#include <climits>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <deque>
#include <functional>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>
using namespace std;

void _run() {
    int n;
    cin >> n;
    vector<string> strs(n);
    for (auto& str : strs) {
        cin >> str;
    }

    vector<vector<pair<char, int>>> ch_counts(n);
    for (int i = 0; i < n; i++) {
        char prev = ' ';
        int cnt = 0;
        for (auto ch : strs[i]) {
            if (isalpha(prev) && prev != ch) {
                ch_counts[i].push_back(make_pair(prev, cnt));
                cnt = 0;
            }
            cnt++;
            prev = ch;
        }
        ch_counts[i].push_back(make_pair(strs[i][strs[i].size() - 1], cnt));
    }

    if (ch_counts[0].size() != ch_counts[1].size()) {
        cout << "Fegla Won" << endl;
        return;
    }

    bool lose = false;
    int ans = 0;
    for (int i = 0; i < ch_counts[0].size(); i++) {
        if (ch_counts[0][i].first != ch_counts[1][i].first) {
            lose = true;
            break;
        }
        ans += abs(ch_counts[0][i].second - ch_counts[1][i].second);
    }
    if (lose) {
        cout << "Fegla Won" << endl;
    } else {
        cout << ans << endl;
    }
}

int main() {
    int t;
    cin >> t;
    for (int i = 0; i < t; i++) {
        printf("Case #%d: ", i + 1);
        _run();
    }
}
