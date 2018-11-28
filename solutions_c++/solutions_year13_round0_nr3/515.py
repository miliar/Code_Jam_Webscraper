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

vector<int> solutions;

bool palindrome(int n) {
    int i = 0;
    int pow10 = 1;
    while (pow10 <= n) {
        ++i;
        pow10 *= 10;
    }
    // pow10 > n
    // 10^i == pow10
    for (int k = 0, k10 = 1; k < i/2; k++, k10 *= 10) {
        if (((n / k10) % 10) != ((n / (pow10 / k10 / 10)) % 10))
            return false;
    }
    return true;
}

void solve_test() {
    
    int A, B;
    cin >> A >> B;
    
    int count = 0;
    for (int x : solutions)
        if (A <= x && x <= B)
            count++;
    
    cout << count << endl;
}

Int main() {
    
    int N = 10000000+1;
    
    cout << endl;
    for (int i = 1; i < N; i++)
        if (palindrome(i) && palindrome(i*i))
            solutions.push_back(i*i);
    
    int n;
    cin >> n;
    for (int i = 0; i < n; i++) {
        cout << "Case #" << (i+1) << ": ";
        solve_test();
    }
    
    return 0;
}
