#include <algorithm>
#include <iostream>
#include <iomanip>
#include <string>

using namespace std;

/**

We use the convention:
 - happy side up  : s = 1
 - happy side down: s = 0

The last flip should bring all pancakes happy side up (s=1).
This means all pancakes in the last flip should be s = 0

So if N(k,s) is the number of flip to turn pancakes 1 to k to side s
and if all pancakes from i to n are side s=1.
Then : N(n,s) = 1+N(i,!s)

We can compute recursively.
 */

typedef string::const_iterator s_iterator;

char opposite_side(char c) 
{
    if('+' == c) return '-';
    return '+';
}


unsigned n_flips(s_iterator first, s_iterator last, char side) 
{
    char side_ = opposite_side(side);
    auto p = find(first, last, side_);
    if(p == last)
        return 0;
    return 1+n_flips(p, last, side_);
}

int main() 
{
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    cerr.tie(0);

    size_t T;
    cin >> T;
    for(size_t t=1; t<=T; ++t) {
        cout << "Case #" << t << ": ";

        std::string input;
        cin >> input;
        reverse(begin(input), end(input));
        cout << n_flips(begin(input), end(input), '+') << "\n";
    }
}
