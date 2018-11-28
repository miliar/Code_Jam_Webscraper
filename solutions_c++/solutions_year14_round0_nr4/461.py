#include <iostream>
#include <vector>
#include <algorithm>
#include <set>
using namespace std;

void solve() {
    int n;
    cin >> n;
    vector<double> a(n);
    vector<double> b(n);
    for (int i = 0; i < n; i++)
        cin >> a[i];
    for (int j = 0; j < n; j++)
        cin >> b[j];
    sort(a.begin(), a.end());
    sort(b.begin(), b.end());

    int ansOrigin = 0;
    set<double> S;
    for (int i = 0; i < n; i++)
        S.insert(b[i]);
    for (int i = 0; i < n; i++) {
        if (S.upper_bound(a[i]) == S.end()) {
            ansOrigin++;
            S.erase(S.begin());
        } else 
            S.erase(S.upper_bound(a[i]));
    }

    int l = 0, r = n,  ansModify = 0;
    for (int i = 0; i < n; i++)
        if (a[i] > b[l]) {
            ansModify++;
            l++;
        } else {
            r--;
        }

    cout << ansModify << " " << ansOrigin << endl;
}

int main() {
    int t;
    cin >> t;
    for (int i = 1; i <= t; i++) {
        printf("Case #%d: ", i);
        solve();
    }
        
}
