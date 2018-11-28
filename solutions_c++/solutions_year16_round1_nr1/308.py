#include <iostream>

using namespace std;

const int maxn = 10000;

char a[maxn];

void solve() {
    string s;
    cin >> s;
    int le = 2000;
    int ri = 2000;
    a[le] = s[0];
    for (int i = 1; i < s.size(); i++) {
        if (s[i] >= a[le]) {
            le--;
            a[le] = s[i];
        } else {
            ri++;
            a[ri] = s[i];
        }
    }
    for (int i = le; i <= ri; i++)
        cout << a[i];

}

int main() {
    ios_base :: sync_with_stdio(false);
    cin.tie(0);
    int test = 0;
    cin >> test;
    for (int id = 1; id <= test; id++) {
        cout << "Case #" << id << ": ";
        solve();
        cout << endl;
    }
    return 0;
}