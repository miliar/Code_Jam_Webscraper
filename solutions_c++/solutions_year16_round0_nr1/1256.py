#include <bits/stdc++.h>
using namespace std;

int getDigits(int x) {
    int mask = 0;
    while(x) {
        mask |= (1 << (x % 10));
        x /= 10;
    }
    return mask;
}

int solve(int n) {
    int now = n;
    int mask = 0;

    do {
        mask |= getDigits(now);
        now += n;
    } while(mask < (1 << 10) - 1);

    return now - n;
}

int main() {

    ifstream cin("testA.in");
    ofstream cout("testA.out");
    
    int t; cin >> t;

    for(int t_case = 0; t_case < t; ++t_case) {
        cout << "Case #" << t_case + 1 << ": ";

        int n; cin >> n;

        if(n == 0)
            cout << "INSOMNIA\n";
        else
            cout << solve(n) << "\n";
    }
}
