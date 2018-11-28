#include <iostream>
#include <sstream>
#include <iomanip>
#include <set>
#include <map>
#include <vector>
#include <stack>
#include <queue>
#include <algorithm>
#include <cstring>
#include <cstdlib>
#include <cmath>
using namespace std;

vector<int> dels[100];
set<string> wset;

string uniq(const string &str, vector<int> &deletions) {
    deletions.clear();
    string s = "";
    s += str[0];
    deletions.push_back(0);
    for (int i = 1; i < str.length(); i++) {
        if (s.back() != str[i]) {
            s += str[i];
            deletions.push_back(0);
        } else {
            deletions[deletions.size() - 1]++;
        }
    }
    return s;
}

int main() {
    int T, N;
    string str;
    cin >> T;
    for (int t = 1; t <= T; t++) {
        wset.clear();
        cin >> N;
        for (int i = 0; i < N; i++) {
            cin >> str;
            wset.insert(uniq(str, dels[i]));
        }
        if (wset.size() > 1) {
            cout << "Case #" << t << ": Fegla Won\n";
        } else {
            int moves = 0;
            for (int j = 0; j < dels[0].size(); j++) {
                int sum = 0;
                for (int i = 0; i < N; i++) {
                    sum += dels[i][j];
                }
                int mean = (int)round((double)sum / (double)N);
                for (int i = 0; i < N; i++) {
                    moves += abs(dels[i][j] - mean);
                }
            }
            cout << "Case #" << t << ": " << moves << '\n';
        }
    }
    cout << flush;
    return 0;
}