//
// Created by aliakseisemchankau on 10.4.16.
//

#ifndef GCJ_QUAL_A_H
#define GCJ_QUAL_A_H

#include <iostream>
#include <fstream>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <algorithm>

#define ll long long

using namespace std;

vector<int> redigit(ll x) {

    vector<int> result;

    if (x == 0) {
        result.push_back(0);
        return result;
    }

    while (x > 0) {
        result.push_back(x % 10);
        x /= 10;
    }

    return result;

}

string makeString(ll x) {

    string s = "";

    while (x > 0) {
        s += ('0' + x % 10);
        x /= 10;
    }

    string ss = "";

    for (int i = s.length() - 1; i >= 0; --i) {
        ss += s[i];
    }

    return ss;

}

string solve(ll n) {

    set<int> digits;

    for (ll i = 1; i <= 10000; ++i) {
        vector<int> subdig = redigit(i * n);
        for (int x : subdig) {
            digits.insert(x);
            if (digits.size() == 10) {
                return makeString(i * n);
            }
        }
    }

    return "INSOMNIA";

}

int main() {

    int T;
    cin >> T;

    for (int i = 0; i < T; ++i) {

        ll N;
        cin >> N;

        cout << "Case #" << i + 1 << ": " << solve(N) << "\n";

    }

}

#endif //GCJ_QUAL_A_H
