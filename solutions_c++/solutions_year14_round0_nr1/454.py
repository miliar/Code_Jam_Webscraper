#include <iostream>
#include <set>
using namespace std;


void solve() {
    int x, t, ans = 0;
    set<int> S;
    cin >> x;
    for (int i = 1; i <= 4; i++)
        for (int j = 1; j <= 4; j++) {
            cin >> t;
            if (i == x) S.insert(t);
        }
    cin >> x;
    for (int i = 1; i <= 4; i++)
        for (int j = 1; j <= 4; j++) {
            cin >> t;
            if (i == x && S.find(t) != S.end())
                if (ans) 
                    ans = -1;
                else
                    ans = t;
            else;
        }
    if (ans == -1)
        cout << "Bad magician!" << endl;
    else if (ans == 0)
        cout << "Volunteer cheated!" << endl;
    else
        cout << ans << endl;
}

int main() {
    int t;
    cin >> t;
    for (int i = 1; i <= t; i++) {
        cout << "Case #" << i << ": ";
        solve();
    }
}
