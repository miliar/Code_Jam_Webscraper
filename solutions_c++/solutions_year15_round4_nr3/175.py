#include <iostream>
#include <string>
#include <array>
#include <cstring>
#include <queue>
#include <cstdlib>
#include <cmath>
#include <algorithm>
#include <unordered_map>
#include <iomanip>
#include <sstream>

using namespace std;
string s[205];
int n, t;
unordered_map<string, pair<int, int> > languages;
int e = 0, f = 0, ef = 0;

int getMin(int stringIndex) {
    if (stringIndex >= n) {
        // int tef = 0;
        // for (auto it = languages.begin(); it != languages.end(); it++) {
        //     cout << it->first << " " << it->second.first << " " << it->second.second << endl;
        //     if (it->second.first > 0 && it->second.second > 0) tef++;
        // }
        // cout << endl;
        // if (tef != ef) {
        //     throw 5;
        // }
        return ef;
    }
    int mins = 99999999;
    // english
    if (stringIndex >= 2 || stringIndex == 0) {
        istringstream sin(s[stringIndex]);
        // cout << s[stringIndex] << endl;
        string next;
        while (sin >> next) {

            if (languages.count(next) == 0) {
                languages[next] = make_pair(0, 0);
            }
            if (languages[next].first == 0) {
                if (languages[next].second != 0) {
                    ef++;
                }
            }
            languages[next].first++;
        }
        mins = getMin(stringIndex + 1);
        istringstream sin2(s[stringIndex]);
        while (sin2 >> next) {
            languages[next].first--;
            if (languages[next].first == 0) {
                if (languages[next].second != 0) {
                    ef--;
                }
            }
        }
    }
    // english
    if (stringIndex >= 2 || stringIndex == 1) {
        istringstream sin(s[stringIndex]);
        string next;
        while (sin >> next) {

            if (languages.count(next) == 0) {
                languages[next] = make_pair(0, 0);
            }
            if (languages[next].second == 0) {
                if (languages[next].first != 0) {
                    ef++;
                }
            }
            languages[next].second++;
        }
        mins = min(mins, getMin(stringIndex + 1));
        istringstream sin2(s[stringIndex]);
        while (sin2 >> next) {
            languages[next].second--;
            if (languages[next].second == 0) {
                if (languages[next].first != 0) {
                    ef--;
                }
            }
        }
    }
    return mins;
}

int main() {
    cin >> t;
    for (int test = 1; test <= t; test++) {
        cin >> n;
        languages.clear();
            getline(cin, s[0]);
        for (int i = 0; i < n; i++) {
            getline(cin, s[i]);
            // cout << s[i] << endl;
        }
        int minNum = getMin(0);
            cout << "Case #" << test << ": " << minNum << endl;
    }
}
