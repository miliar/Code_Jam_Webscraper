
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
#include <cln/cln.h>

typedef int builtin_int;
#define int long long

using namespace std;
using namespace cln;

typedef cl_I Int;
typedef cl_RA Frac;

Int operator/(Int x, Int y) {
    return floor1(x, y);
}

// struct Solution {
//     int nvalue;
//     int cons_at_start;
//     int cons_at_end;
// };
// 
// Solution result(const string& S, int first, int last, int n) {
//     if (first == last)
//         return Solution{0, 0, 0};
//     
//     int middle = first + (last - first)/2;
//     
//     Solution left  = result(S, first, middle, n);
//     int left_size = middle - first;
//     Solution right = result(S, middle, last, n);
//     int right_size = last - middle;
//     
//     Solution total;
//     
//     if (left.cons_at_end == left_size)
//         // left is all consonants
//         total.cons_at_start = left_size + right.cons_at_start;
//     else
//         total.cons_at_start = left.cons_at_start;
//     
//     if (right.cons_at_start == right_size)
//         // right is all consonants
//         total.cons_at_end = left.cons_at_end + right_size;
//     else
//         total.cons_at_end = right.cons_at_end;
//     
//     // ???
//     
//     return total;
// };



void solve_test() {
    string S;
    int n;
    cin >> S >> n;
    
    int count = 0;
    
    for (int i = 0; i < S.size(); i++)
        for (int j = i; j < S.size(); j++) {
            
            int local_count = 0;
            int max_local_count = 0;
            for (int k = i; k <= j; k++)
                switch (S[k]) {
                case 'a':
                case 'e':
                case 'i':
                case 'o':
                case 'u':
                    local_count = 0;
                    break;
                default:
                    local_count++;
                    max_local_count = max(max_local_count, local_count);
                }
            
            if (max_local_count >= n)
                ++count;
        }
    
    cout << count << endl;
}

builtin_int main() {
    
    int n;
    cin >> n;
    for (int i = 0; i < n; i++) {
        cout << "Case #" << (i+1) << ": ";
        solve_test();
    }
    
    return 0;
}
