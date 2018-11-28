#include <bits/stdc++.h>

using namespace std;

void solve()
{
    int n;
    cin >> n;
    vector <int> A(n);

    for (int i = 0; i < n; i++) {
        cin >> A[i];
    }

    while (*max_element(A.begin(), A.end()) > 0) {
        int best = *max_element(A.begin(), A.end());
        int pos1 = int(find(A.begin(), A.end(), best) - A.begin());
        int pos2 = int(find(A.begin() + pos1 + 1, A.end(), best) - A.begin());
        int pos3 = (pos2 < n ? int(find(A.begin() + pos2 + 1, A.end(), best) - A.begin()) : n);

        if (pos2 == n) {
            cout << char('A' + pos1) << ' ';
            A[pos1]--;
        } else if (pos3 == n) {
            cout << char('A' + pos1) << char('A' + pos2) << ' ';
            A[pos1]--;
            A[pos2]--;
        } else {
            cout << char('A' + pos1) << ' ';
            A[pos1]--;
        }
    }
}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);

    int T;
    cin >> T;

    for (int tst = 0; tst < T; tst++) {
        cout << "Case #" << tst + 1 << ": ";

        solve();

        cout << '\n';
    }
}
