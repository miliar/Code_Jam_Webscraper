#include<iostream>
#include<cmath>
#include<vector>
#include<algorithm>
#include<unordered_map>
#include<unordered_set>
#include<queue>

using namespace std;

vector<unordered_map<char, int>> dic = {{{'Z', 1}, {'E', 1}, {'R', 1}, {'O', 1}},
                                        {{'O', 1}, {'N', 1}, {'E', 1}},
                                        {{'T', 1}, {'W', 1}, {'O', 1}},
                                        {{'T', 1}, {'H', 1}, {'R', 1}, {'E', 2}},
                                        {{'F', 1}, {'O', 1}, {'U', 1}, {'R', 1}},
                                        {{'F', 1}, {'I', 1}, {'V', 1}, {'E', 1}},
                                        {{'S', 1}, {'I', 1}, {'X', 1}},
                                        {{'S', 1}, {'E', 2}, {'V', 1}, {'N', 1}},
                                        {{'E', 1}, {'I', 1}, {'G', 1}, {'H', 1}, {'T', 1}},
                                        {{'N', 2}, {'I', 1}, {'E', 1}}};

bool number(unordered_map<char, int> & sm, string & res, int n) {
    if (sm.empty()) {
        return true;
    }

    for (auto &x : dic[n]) {
        if (sm.count(x.first) == 0 || sm[x.first] < x.second) {
            return false;
        }
    }

    for (auto &x : dic[n]) {
        sm[x.first] -= x.second;
        if (sm[x.first] == 0) {
            sm.erase(x.first);
        }
    }

    res += to_string(n);

    for (int i = n; i <= 9; ++i) {
        if (number(sm, res, i)) {
            return true;
        }
    }

    res.pop_back();

    for (auto &x : dic[n]) {
        sm[x.first] += x.second;
    }
}

string number(string & s) {
    unordered_map<char, int> sm;
    for (auto & c : s) {
       ++sm[c];
    }

    string res;

    for (int i = 0; i <= 9; ++i) {
        if (number(sm, res, i)) {
            break;
        }
    }

    return res;
}

int main() {
    int t;
    cin >> t;
    for (int i = 1; i <= t; ++i) {
        string s;
        cin >> s;
        cout << "Case #" << i << ": " << number(s) << "\n";
    }
    return 0;
}