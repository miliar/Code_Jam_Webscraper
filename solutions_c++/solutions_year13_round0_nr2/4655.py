#include <iostream>
#include <iomanip>
#include <cstdio>
#include <vector>
#include <queue>
#include <set>
#include <stack>
#include <string.h>
#include <algorithm>
#include <fstream>
#include <cassert>
#include <limits>
#include <numeric>
#include <map>
#define FOREACH(it, C) for(typeof((C).begin()) it = (C).begin(); it != (C).end(); ++it)
using namespace std;
const string YES = "YES";
const string NO = "NO";
typedef long long int ll;
typedef long double ld;

string solve(const int n, const int m, const vector<vector<int> >& board) {
    vector<int> max_in_row(n, 0);
    vector<int> max_in_col(m, 0);
    for (int i = 0 ; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            max_in_row[i] = max(max_in_row[i], board[i][j]);
            max_in_col[j] = max(max_in_col[j], board[i][j]);
        }
    }
    for (int i = 0 ; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            if (board[i][j] != max_in_row[i] &&
                board[i][j] != max_in_col[j]) {
                return NO;
            }
        }
    }
    return YES;
}

int main() {
    int numberOfCases;
	cin >> numberOfCases;
	for(int testCase = 1; testCase <= numberOfCases; ++testCase) {
        int n, m;
        cin >> n >> m;
        vector<vector<int> > board(n, vector<int>(m));
        for(int i = 0; i < n; ++i) {
            for(int j = 0; j < m; ++j) {
                cin >> board[i][j];
            }
        }
		cout << "Case #" << testCase << ": " << solve(n, m, board) << endl;
	}
}
