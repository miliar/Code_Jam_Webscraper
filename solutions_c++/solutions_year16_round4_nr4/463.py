#include <iostream>

using namespace std;

int t;
int n;
string s[10];
int p;

int v1[10];
int v2[10];

bool ok;

void tutki(int k) {
    for (int i = 0; i < n; i++) {
        if (v1[i]) continue;
        v1[i] = 1;
        int c = 0;
        for (int j = 0; j < n; j++) {
            if (v2[j]) continue;
            if (s[i][j] == '0') continue;
            c++;
            v2[j] = 1;
            tutki(k+1);
            v2[j] = 0;
        }
        if (c == 0) ok = false;
        v1[i] = 0;
    }
}

void haku(int y, int x, int c) {
    if (y == n) {
        for (int i = 0; i < n; i++) v1[i] = 0;
        for (int i = 0; i < n; i++) v2[i] = 0;
        ok = true;
        tutki(0);
        if (ok) p = min(p,c);
        return;
    }
    if (x == n) {
        haku(y+1,0,c);
        return;
    }
    haku(y,x+1,c);
    if (s[y][x] == '0' && c < 12) {
        s[y][x] = '1';
        haku(y,x+1,c+1);
        s[y][x] = '0';
    }
}

int main() {
    cin >> t;
    for (int i = 1; i <= t; i++) {
        cin >> n;
        for (int i = 0; i < n; i++) cin >> s[i];
        p = 999999999;
        haku(0,0,0);
        cout << "Case #" << i << ": " << p << "\n";
    }
}
