#include <iostream>
#include <vector>
#include <map>
#include <string>
#include <algorithm>
using namespace std;

int T, N, D, n;

int numbers(int num) {
    int res = 0;
    for(char c : to_string(num)) {
        res |= 1 << (c - '0');
    }
    return res;
}

void solve()
{
    if (N == 0) {
        cout << "INSOMNIA" << endl;
    }
    else {
        D = numbers(N), n = N;
        while (D != 0x03FF) {
            n += N;
            D |= numbers(n);
        }
        cout << n << endl;
    }
}

int main()
{
    cin >> T;
    for (int t = 1; t <= T; ++t)
    {
        cin >> N;
        cout << "Case #" << t << ": ";
        solve();
    }

    return 0;
}