#include <cstdio>
#include <iostream>

#include <vector>
#include <list>
#include <string>

#include <algorithm>
#include <functional>
#include <cmath>

using namespace std;

typedef long long int64;
typedef unsigned long long uint64;

bool palindrome(int x)
{
    int t = x;
    int y = 0;

    while(t != 0) {
        y = y * 10 + t % 10;
        t /= 10;
    }
    
    return x == y;
}

void solve_case(int a, int b, int case_number)
{
    int x = static_cast<int>(ceil(sqrt(a)));

    int ans = 0;
    for(int i = x; i * i <= b; ++i)
        if(palindrome(i) && palindrome(i * i))
            ++ans;

    cout << "Case #" << case_number << ": " << ans << endl;
}

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    int t;
    cin >> t;
    for(int i = 1; i <= t; ++i) {
        int a, b;
        cin >> a >> b;
        solve_case(a, b, i);
    }

    return 0;
}

// Local Variables:
// eval: (when (fboundp 'flymake-mode) (flymake-mode 1))
// End:
