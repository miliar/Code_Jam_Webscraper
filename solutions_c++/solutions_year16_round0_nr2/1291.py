#include <bits/stdc++.h>
using namespace std;

string flip(string a) {
    int n = a.size();
    reverse(a.begin(), a.end());
    for(int i = 0; i < n; ++i)
        if(a[i] == '+')
            a[i] = '-';
        else a[i] = '+';
    return a;
}

int solve(string a) {
    int n = a.size();
    if(n == 0)
        return 0;
    if(a[n - 1] == '+')
        return solve(a.substr(0, n - 1));
    if(a[0] == '-')
        return 1 + solve(flip(a));

    for(int i = 0; i < n; ++i) {
        a[i] = '-';
        if(a[i + 1] == '-')
            break;
    }

    return 2 + solve(flip(a));
}

int main() {

    ifstream cin("testB.in");
    ofstream cout("testB.out");
    
    int t; cin >> t;

    for(int t_case = 0; t_case < t; ++t_case) {
        cout << "Case #" << t_case + 1 << ": ";
        string a; cin >> a;
        cout << solve(a) << "\n";
    }
}
