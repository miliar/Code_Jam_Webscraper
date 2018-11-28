#include <bits/stdc++.h>

using namespace std;

set<int> Set;
int main() {
    freopen("input", "r", stdin);
    freopen("output", "w", stdout);

    int t;
    cin >> t;
    int tt = 0;
    while(t--) {
        int n;
        cin >> n;

        cout << "Case #" << ++tt << ": ";

        if(n == 0) {
            cout << "INSOMNIA\n";
            continue;
        }

        Set.clear();
        for(int i = n; ; i += n) {
            for(int j = i; j; j /= 10) {
                Set.insert(j % 10);
            }
            if(Set.size() == 10) {
                cout << i << "\n";
                break;
            }
        }

    }

    return 0;
}
