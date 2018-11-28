#include <iostream>
#include <cstdio>
#include <algorithm> 
#include <cstring>

using namespace std;

string s[5];
int n;
int ans;
int p[5];
int used[5];
int bad;

void gen2(int v) {
    if (v == n) {
        return;
    }
    int tmp = 0;
    for (int i = 0; i < n; i++) {
        if (s[p[v]][i] == '1' && !used[i]) {
            tmp = 1;
            used[i] = 1;
            gen2(v + 1);
            used[i] = 0;
        }
    }
    if (tmp == 0) {
        bad = 1;
    } 
}

void check(int cost) {
    for (int i = 0; i < n; i++) {
        p[i] = i;
    }
    int ok = 1;
    do {
        memset(used, 0, sizeof(used));
        bad = 0;
        gen2(0);
        if (bad) {
            ok = 0;
        }
    } while (next_permutation(p, p + n));
    if (ok) {
        if (cost < ans) {
            ans = cost;
        }    
    }
}

void gen(int x, int y, int cost) {
    if (y == n) {
        y = 0;
        x++;
    } 
    if (x == n) {
        check(cost);
        return;
    }
    
    gen(x, y + 1, cost);
    if (s[x][y] == '0') {
        s[x][y] = '1';
        gen(x, y + 1, cost + 1);
        s[x][y] = '0';
    } 
}

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int testCases;
    cin >> testCases;
    for (int testCase = 1; testCase <= testCases; testCase++) {
        cout << "Case #" << testCase << ": ";
        cin >> n;
        for (int i = 0; i < n; i++) {
            cin >> s[i];
        }      
        ans = n * n;
        gen(0, 0, 0);
        cout << ans << endl;     
    }
    return 0;
}