#include <iostream>
#include <sstream>
#include <set>
#include <stack>
#include <vector>
#include <algorithm>
#include <string.h>
using namespace std;

void reverse(string& s, int i)
{
    for (int k = 0; k <= i; ++k) {
        if (s[k] == '+') s[k] = '-';
        else s[k] = '+';
    }
    reverse(s.begin(), s.begin() + i + 1);
}

int solve(string s)
{
    int n = s.size();
    int res = 0;

    for (int i = n - 1; i >= 0; --i) {
        if (s[i] == '-') {
            res++;
            if (s[0] == '-') {
                reverse(s, i);
            } else {
                int j = 0;
                while (s[j] == '+' && j <= i) {
                    j++;
                }
                reverse(s, j - 1);

                if (j < i) {
                    res++;
                    reverse(s, i);
                }
            }
        }
    }

    return res;
}

int main()
{
    int T;
    cin >> T;

    cout.setf(ios::fixed, ios::floatfield);
    cout.precision(6);

    for (int test = 1; test <= T; ++test) {
        string s, revs;
        cin >> s;
        revs = s;
        reverse(revs, revs.size() - 1);

        int res = min(solve(s), solve(revs) + 1);

        cout << "Case #" << test << ": " << res << endl;
    }

    return 0;
}
