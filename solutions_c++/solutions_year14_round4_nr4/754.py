#include <iostream>
#include <vector>
#include <set>

using namespace std;

int t, m, n;
vector<string> s;
int v[10];
vector<string> u;
int sm, sq;

void laske() {
    int qq = 0;
    for (int i = 1; i <= n; i++) {
        u.clear();
        for (int j = 0; j < m; j++) {
            if (v[j] == i) u.push_back(s[j]);
        }
        set<string> q;
        for (string z : u) {
            for (int j = 0; j <= z.size(); j++) {
                q.insert(z.substr(0,j));
            }
        }
        qq += q.size();
    }
    if (qq > sm) {
        sm = qq;
        sq = 1;
    } else if (qq == sm) {
        sq++;
    }
}

void haku(int k) {
    if (k == m) {
        laske();
        return;
    }
    for (int i = 1; i <= n; i++) {
        v[k] = i;
        haku(k+1);
    }
}

int main() {
    cin >> t;
    for (int x = 1; x <= t; x++) {
        cin >> m >> n;
        s.resize(m);
        for (int i = 0; i < m; i++) cin >> s[i];
        sm = 0;
        haku(0);
        cout << "Case #" << x << ": " << sm << " " << sq << "\n";
    }
}
