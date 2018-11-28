#include <iostream>
#include <string>
#include <cmath>
#include <vector>
#include <algorithm>

using namespace std;

void solve(int test_nr)
{
    string s;
    cin >> s;

    int flips = 0;
    // always flip last '-'
    for (int i = s.length() - 1; i >= 0; i--)
        if ((s[i] == '-' && !(flips & 1)) || (s[i] == '+' && (flips & 1)))
            flips ++;

    cout << "Case #" << test_nr << ": " << flips << endl;
}

int main()
{
    int T;
    cin >> T;
    for (int i = 1; i <= T; i ++) {
        solve(i);
    }

    return 0;
}
