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
#define db3(x, y, z) cerr << "(" << #x << ", " << #y << ", " << #z << ") = (" << x << ", " << y << ", " << z << ")\n"
#define all(a) (a).begin(), (a).end()

#define equal equalll
#define less lesss
const int N = -1;
const long long INF = 1e9 + 19;

struct A {
    int cnt;
    int type;
    string s;
    A(int cnt, int type, string s): cnt(cnt), type(type), s(s) { }
};

int n, p, r, s;

void read() {
    scanf("%d%d%d%d", &n, &r, &p, &s);
}

int buttle(int x, int y) {
    if (x > y) swap(x, y);
    if (x == 0 && y == 1) return 0;
    if (x == 1 && y == 2) return 1;
    if (x == 0 && y == 2) return 2;
    assert(false);
}

string merge(string a, string b) {
    assert(a.size() == b.size());
    if (a < b) return a + b;
    return b + a;
}

string go(A a, A b, A c) {
    int sum = a.cnt + b.cnt + c.cnt;    
    //db(sum);
    if (sum == 1) {
        if (a.cnt == 1) return a.s;
        if (b.cnt == 1) return b.s;
        if (c.cnt == 1) return c.s;
        assert(false);
    }
    assert(sum % 2 == 0);
    sum /= 2;
    int ab = sum - c.cnt;
    int ac = sum - b.cnt;
    int bc = sum - a.cnt;
    //db(sum);
    //db3(ab, ac, bc);
    if (ab < 0 || ac < 0 || bc < 0) 
        return "";
    
    string ABs = merge(a.s, b.s);    
    string ACs = merge(a.s, c.s);
    string BCs = merge(b.s, c.s);

    return go(A(ab, buttle(a.type, b.type), ABs),
              A(ac, buttle(a.type, c.type), ACs),
              A(bc, buttle(b.type, c.type), BCs));
}

void solve() {
    string res = go(A(p, 0, "P"), A(r, 1, "R"), A(s, 2, "S"));
    if ((int)res.size() != (1 << n)) {
        puts("IMPOSSIBLE");
        return;
    }
    cout << res << "\n";

}

void stress() {

}


int main(){
#ifdef MY_DEBUG
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

