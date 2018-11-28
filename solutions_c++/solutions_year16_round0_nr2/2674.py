//
// Created by aliakseisemchankau on 10.4.16.
//

#ifndef GCJ_QUAL_B_H
#define GCJ_QUAL_B_H


#include <iostream>
#include <fstream>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <algorithm>

#define ll long long

using namespace std;

int solve(string s) {

    bool flag = (s[0] == '-');

    vector<int> lens;

    int cur = 0;

    while (cur < s.length()) {

        int curn = cur;
        while (s[curn] == s[cur] && curn < s.length()) {
            ++curn;
        }
        lens.push_back(curn - cur);

        cur = curn;

    }

    /*for (int x : lens) {
        cout << x << " ";
    }
    cout << "\n";*/

    if (flag) {
        int ans = lens.size();
        if (ans % 2 == 0) {
            --ans;
        }
        return ans;
    }

    int ans = lens.size();
    if (ans % 2 == 1) {
        --ans;
    }

    return ans;

}


int main() {

    int T;
    cin >> T;

    for (int i = 0; i < T; ++i) {

        string s;
        cin >> s;

        cout << "Case #" << i + 1 << ": " << solve(s) << "\n";

    }

}


#endif //GCJ_QUAL_B_H
