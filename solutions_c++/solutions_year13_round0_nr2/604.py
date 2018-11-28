// #include "common.h"

// -W -Wall -Werror -std=c++0x -Wno-sign-compare -Wfloat-equal

// alias valgrind='\valgrind --malloc-fill=AA --track-origins=yes
// --read-var-info=yes --num-callers=50 --db-attach=no --db-command="kdbg %f -p %p"'

// alias callgrind='\valgrind --tool=callgrind --simulate-cache=yes --dump-instr=yes'

// Valgrind with stdin + debug:
// valgrind --input-fd=3 --db-attach=yes build/foo <input 3</dev/tty

#include <algorithm>
#include <cassert>
#include <climits>
#include <cmath>
#include <deque>
#include <iostream>
#include <limits>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <utility>
#include <vector>
#include <stack>

typedef int Int;
#define int long long

using namespace std;

void solve_test() {
    int rows, cols;
    cin >> rows >> cols;
    vector<vector<int> > lawn(rows, vector<int>(cols));
    for (vector<int>& row : lawn)
        for (int& cell : row)
            cin >> cell;
    vector<int> max_in_row(rows, 0);
    vector<int> max_in_col(cols, 0);
    for (int row = 0; row < rows; row++)
        for (int col = 0; col < cols; col++) {
            max_in_row[row] = max(max_in_row[row], lawn[row][col]);
            max_in_col[col] = max(max_in_col[col], lawn[row][col]);
        }
    bool possible = true;
    for (int row = 0; row < rows; row++)
        for (int col = 0; col < cols; col++)
            if (lawn[row][col] != min(max_in_row[row], max_in_col[col]))
                possible = false;
    if (possible)
        cout << "YES" << endl;
    else
        cout << "NO" << endl;
}

Int main() {
    
    int n;
    cin >> n;
    for (int i = 0; i < n; i++) {
        cout << "Case #" << (i+1) << ": ";
        solve_test();
    }
    
    return 0;
}
