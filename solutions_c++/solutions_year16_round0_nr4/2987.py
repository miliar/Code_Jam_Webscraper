#include <bits/stdc++.h>

using namespace std;

int main()
{
    int T;
    cin >> T;
    
    for (int tst = 0; tst < T; tst++) {
        int k, c, s;
        cin >> k >> c >> s;
        cout << "Case #" << tst + 1 << ": ";

        for (int i = 1; i <= s; i++) {
            cout << i << ' ';
        }
        cout << "\n";
    }
    return 0;
}
