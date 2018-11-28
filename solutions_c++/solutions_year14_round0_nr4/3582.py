#include <iostream>
#include <iomanip>
#include <cstdio>
#include <vector>
#include <queue>
#include <set>
#include <stack>
#include <algorithm>
#include <fstream>
#include <cassert>
#include <limits>
#include <numeric>
#include <map>
#include <unordered_set>
#include <string>
#define FOREACH(it, C) for(typeof((C).begin()) it = (C).begin(); it != (C).end(); ++it)
using namespace std;
typedef long long int ll;
typedef long double ld;

const string solve (size_t n, vector<ld> naomi, vector<ld> ken) {
    sort(naomi.begin(), naomi.end());
    sort(ken.begin(), ken.end());
    size_t fair_score = 0;
    for (size_t i = 0, j = 0; i < n; ++i, ++j) {
        while (j < n && naomi[i] > ken[j]) {
            ++j;
        }
        if (j >= n)
            fair_score++;
    }
    size_t cheat_score = 0;
    for (size_t i = 0, j = 0; i < n; ++i) {
        if (naomi[i] > ken[j]) {
            // bluff
            cheat_score++;
            j++;
        } // else sacrifice
    }
    return to_string(cheat_score) + " " + to_string(fair_score);
}

int main() {
    int numberOfCases;
	cin >> numberOfCases;
	for (int testCase = 1; testCase <= numberOfCases; ++testCase) {
        size_t n;
        cin >> n;
        vector<ld> naomi(n);
        for (size_t i = 0; i < n; ++i) {
            cin >> naomi[i];
        }
        vector<ld> ken(n);
        for (size_t i = 0; i < n; ++i) {
            cin >> ken[i];
        }
		cout << "Case #" << testCase << ": " << solve(n, naomi, ken) << endl;
	}
}
