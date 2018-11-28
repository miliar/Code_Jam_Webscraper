#include <iostream>
#include <cmath>
#include <vector>
#include <map>
#include <set>
#include <string>
#include <cstring>
#include <queue>
#include <ctime>
#include <cassert>
#include <cstdio>
#include <algorithm>
#include <unordered_set>
#include <unordered_map>
#include <bitset>

using namespace std;

#define fr first
#define sc second
#define mp make_pair
#define pb push_back
#define epr(...) fprintf(stderr, __VA_ARGS__)
#define db(x) cerr << #x << " = " << x << endl
#define db2(x, y) cerr << "(" << #x << ", " << #y << ") = (" << x << ", " << y << ")\n"; 
#define all(a) (a).begin(), (a).end()

#define equal equalll
#define less lesss
const int N = -1;
const long long INF = 1e9 + 19;

long long k, c, s;

void read() {
    cin >> k >> c >> s;
}



void solve() {
    if (s < k) {
        puts("IMPOSSIBLE");
        return;
    }
    for (int i = 0; i < k; i++) {
        long long pos = i;
        for (int j = 0; j < c - 1; j++)
            pos = pos * k + i;
        assert(pos >= 0);
        printf("%lld ", pos + 1);
    }
    puts("");
}

void stress() {

}


int main(){
#ifdef DEBUG
    freopen("in", "r", stdin);
    freopen("out", "w", stdout);
#endif
    if (1) {
        int k; 
        scanf("%d", &k);
        for (int tt = 0; tt < k; tt++) {
            printf("Case #%d: ", tt + 1);
            read();
            solve();
        }
    }
    else {
        stress();
    }

    return 0;
}

