#include <cstdio>
#include <algorithm>
#include <cstdlib>
#include <vector>
#include <iostream>
#include <cstring>

#define forn(i, n) for(int i = 0; i < (int)(n); ++i)
#define ford(i, n )for(int i = (int)(n) - 1; i >= 0; --i)
#define fore(i, a, b) for(int i = (int)(a); i <= (int)(b); ++i)

#define pb push_back
#define all(v) (v).begin(), (v).end()

using namespace std;

typedef long long i64;

vector<i64> a;

int solve(i64 A, i64 B) {
    return upper_bound(all(a), B) - upper_bound(all(a), A-1);
}

bool ispalindr(i64 n) {
    char tmp[20];
    char amp[20];
    sprintf(tmp, "%lld", n);
    strcpy(amp, tmp);
    int l = strlen(amp);
    reverse(amp, amp + l);
    return strcmp(amp, tmp) == 0;
}

void init() {
    forn(i, 1e7) {
        if( ispalindr(i) && ispalindr(i*1ll*i) ) {
            a.pb(i * 1ll * i);
            cerr << i * 1ll * i << '\n';
        }
    }
}

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int T;
    init();
    cin >> T;
    i64 A, B;
    fore(t, 1, T) {
        cin >> A >> B;
        cout << "Case #" << t << ": " <<solve(A, B) << '\n';
    }
    return 0;
}
