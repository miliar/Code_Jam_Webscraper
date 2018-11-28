#include <iostream>
#include <vector>

using namespace std;

void Fill(int x, vector<bool>& v) {
    if (x == 0) {
        v[0] = true;
        return;
    }
    while (x) {
        v[x % 10] = true;
        x /= 10;
    }
}

bool Stop(const vector<bool>& v) {
    for (size_t i = 0; i < v.size(); ++i)
        if (v[i] == false)
            return false;
    return true;
}
void Solve() {
    int n;
    cin >> n;
    vector<bool> v(10, false);
    for (int i = 1; i <= 100; ++i) {
        Fill(i * n, v);
        if (Stop(v)) {
            cout << i * n << endl;
            return;
        }
    }
    cout << "INSOMNIA" << endl;
}

int main() {
    int t;
    cin >> t;
    for (int i = 1; i <= t; ++i) {
        cout << "Case #" << i << ": ";
        Solve();
    }
    return 0;
}
