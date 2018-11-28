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
const string bad_magician = "Bad magician!";
const string volunteer_cheated = "Volunteer cheated!";

const string solve (vector<vector<vector<int> > > sq, vector<int> answers) {
    assert(sq.size() == answers.size());
    assert(sq.size() > 0);
    int k = sq.size();
    unordered_set<int> candidates;
    for (auto& v: sq[0]) {
        for (auto& x: v) {
            candidates.insert(x);
        }
    }
    for (int i = 0; i < k ; ++i) {
        unordered_set<int> new_candidates;
        for (auto& x: sq[i][answers[i] - 1]) {
            if (candidates.count(x) > 0) {
                new_candidates.insert(x);
            }
        }
        candidates = new_candidates;
    }
    if (candidates.size() == 0) {
        return volunteer_cheated;
    }
    if (candidates.size() > 1) {
        return bad_magician;
    }
    return to_string(*candidates.begin());
}

vector<vector<int> > read_sq () {
    vector<vector<int> > sq(4, vector<int>(4));
    for (int i = 0; i < 4; ++i) {
        for (int j = 0; j < 4; ++j) {
            cin >> sq[i][j];
        }
    }
    return sq;
}

int main() {
    int numberOfCases;
	cin >> numberOfCases;
	for (int testCase = 1; testCase <= numberOfCases; ++testCase) {
        vector<int> answers;
        vector<vector<vector<int> > > sq;
        for (int i = 0; i < 2; ++i) {
            int answer;
            cin >> answer;
            answers.push_back(answer);
            sq.push_back(read_sq());
        }
		cout << "Case #" << testCase << ": " << solve(sq, answers) << endl;
	}
}
