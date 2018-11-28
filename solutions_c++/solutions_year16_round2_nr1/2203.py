#include <iostream>
#include <map>
#include <unordered_map>

using namespace std;

bool has(const unordered_map<char, int>& m, const string& s) {
    for (auto ch : s) {
        if (m.find(ch)==end(m))
            return false;
        if (m.at(ch) <= 0)
            return false;
    }
    return true;
}

void remove(unordered_map<char, int>& m, const string& s) {
    for (auto ch : s) {
        m[ch] -= 1;
    }
}

string solve(string s) {
    string ret = "";
    unordered_map<char, int> m;
    map<char, int> r;
    for (auto ch : s) {
        m[ch] += 1;
    }

    while (has(m, "ZERO")) {
        r['0'] += 1;
        remove(m, "ZERO");
    }

    while (has(m, "TWO")) {
        r['2'] += 1;
        remove(m, "TWO");
    }

    while (has(m, "FOUR")) {
        r['4'] += 1;
        remove(m, "FOUR");
    }

    while (has(m, "EIGHT")) {
        r['8'] += 1;
        remove(m, "EIGHT");
    }

    while (has(m, "ONE")) {
        r['1'] += 1;
        remove(m, "ONE");
    }

    while (has(m, "THREE")) {
        r['3'] += 1;
        remove(m, "THREE");
    }

    while (has(m, "SIX")) {
        r['6'] += 1;
        remove(m, "SIX");
    }

    while (has(m, "FIVE")) {
        r['5'] += 1;
        remove(m, "FIVE");
    }

    while (has(m, "NINE")) {
        r['9'] += 1;
        remove(m, "NINE");
    }

    while (has(m, "SEVEN")) {
        r['7'] += 1;
        remove(m, "SEVEN");
    }

    for (auto item : r) {
        ret += string(item.second, item.first);
    }

    return ret;
}



int main() {
    int T;
    cin >> T;
    for (int c = 1; c <= T; c++) {
        string S;
        cin >> S;
        cout << "Case #" << c << ": " << solve(S) << endl;
    }
    return 0;
}