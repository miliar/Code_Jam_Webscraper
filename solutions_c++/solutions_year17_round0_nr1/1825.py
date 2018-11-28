#include <iostream>
#include <algorithm>

using namespace std;


bool is_done(const string& s, size_t& pos)
{
    for (size_t i = 0; i < s.size(); ++i) {
        if (s[i] == '-') {
            pos = i;
            return false;
        }
    }
    return true;
}

bool flip(string& s, size_t pos, size_t k)
{
    if (pos + k - 1 >= s.size()) return false;
    for (size_t i = 0; i < k; ++i) {
        if (s[pos + i] == '+') {
            s[pos + i] = '-';
        } else {
            s[pos + i] = '+';
        }
    }
    return true;
}

/*
size_t recur(string& s, size_t pos, size_t k, size_t trial)
{
    if (pos + k - 1 >= s.size() || is_done(s)) {
        return trial;
    }
    size_t min_trial = trial;
    if (s[pos] == '-') {
        flip(s, pos, k);
        for (size_t i = pos + 1; i < s.size(); ++i) {
            min_trial = min(min_trial, recur(s, i, k, trial + 1));
        }
        flip(s, pos, k);
    } else {
        for (size_t i = pos + 1; i < s.size(); ++i) {
            min_trial = min(min_trial, recur(s, i, k, trial + 1));
        }
    }
    return min_trial;
}
*/

int main(void)
{
    size_t t;
    cin >> t;
    for (size_t i = 0; i < t; ++i) {
        string s;
        size_t k;
        cin >> s >> k;
        size_t pos, trial = 0;
        while (true) {
            if (is_done(s, pos)) {
                cout << "Case #" << (i + 1) << ": " << trial << endl;
                break;
            } else if (!flip(s, pos, k)) {
                cout << "Case #" << (i + 1) << ": IMPOSSIBLE" << endl;
                break;
            }
            ++trial;
        }
    }
}

