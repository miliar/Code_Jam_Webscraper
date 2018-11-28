#include <vector>
#include <set>
#include <unordered_set>
#include <map>
#include <unordered_map>
#include <iostream>
#include <cstdint>
#include <string>
#include <cassert>
#include <boost/optional.hpp>

using namespace std;

vector<string> digits{ "ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE" };

string removeDigitsChars(const string& input, string digit) {
    string out;
    for (const auto c : input) {
        auto pos = digit.find(c);
        if (pos != string::npos) {
            digit.erase(pos, 1);
        } else {
            out += c;
        }
    }
    return out;
}

bool canUse(string input, const string& digit) {
    for (const auto c : digit) {
        auto pos = input.find(c);
        if (pos != string::npos) {
            input.erase(pos, 1);
        } else {
            return false;
        }
    }
    return true;
}

string solve(string input)
{
    string out;
    for (unsigned int i = 0; i != digits.size(); ++i) {
        while (canUse(input, digits[i])) {
            input = removeDigitsChars(input, digits[i]);
            out += to_string(i);
        }
    }
    assert(input.empty());
    return out;
}

boost::optional<string> solve2(const string& input, int pos) {
    if (pos >= digits.size()) {
        if (input.empty()) {
            return string();
        } else {
            return boost::none;
        }
    }
    auto can = canUse(input, digits[pos]);
    if (can) {
        auto tmp = removeDigitsChars(input, digits[pos]);
        auto s = solve2(tmp, pos);
        if (s) {
            return to_string(pos) + *s;
        }
        s = solve2(tmp, pos+1);
        if (s) {
            return to_string(pos) + *s;
        }
    }
    return solve2(input, pos+1);
}

int main() {
    int T;
    cin >> T;
    for (int i = 1; i <= T; ++i) {
        string input;
        cin >> input;
        const auto phone = solve2(input, 0);
        cout << "Case #" << i << ": " << *phone << endl;
    }

}
