#include <bits/stdc++.h>
using namespace std;

int main() {

    ifstream cin("testD.in");
    ofstream cout("testD.out");
    
    int t; cin >> t;

    for(int t_case = 0; t_case < t; ++t_case) {
        cout << "Case #" << t_case + 1 << ": ";
        int k, c, s; cin >> k >> c >> s;
        for(int i = 0; i < k; ++i)
            cout << i + 1 << " ";
        cout << "\n";
    }
}
