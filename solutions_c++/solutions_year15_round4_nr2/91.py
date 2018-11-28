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

#define equal equalll
#define less lesss
const int N = 111;
const int INF = 1e9;

bool equal(double a, double b) {
    return abs(a - b) < 1e-9;
}

struct T {
    double r, c;
};

double V, X;
int n;
T b[N];

void read() {
    cin >> n >> V >> X;
    for (int i = 0; i < n; i++)
        cin >> b[i].r >> b[i].c;
}

bool cmpC(T a, T b) {
    return a.c < b.c;
}

void solve() {
    for (int i = 0; i < n; i++)
        b[i].c -= X;
    sort(b, b + n, cmpC); 

    vector < T > down;
    vector < T > up;
    for (int i = 0; i < n; i++)
        if (b[i].c < 0)
            down.pb(b[i]);
        else
            up.pb(b[i]);
    double sumD = 0, sumU = 0;
    for (auto x: down)
        sumD += -x.c * x.r;
    for (auto x: up)
        sumU += x.c * x.r;

    double vv = min(sumD, sumU);
    double speed = 0;
    double tmp = vv; 
    for (auto x: up) {
        if (equal(x.c, 0)) {
            speed += x.r;
            continue;
        }
        double d = min(tmp, x.r * x.c);
        tmp -= d;
        speed += d / x.c;
    }
    reverse(down.begin(), down.end());
    tmp = vv;
    for (auto x: down) {
        if (equal(x.c, 0)) {
            speed += x.r;
            continue;
        }
        double d = min(tmp, -x.r * x.c);
        tmp -= d; 
        speed += d / (-x.c);
    }
    //db(speed);
    if (equal(speed, 0)) {
        printf("IMPOSSIBLE\n");
    }
    else
        printf("%.17f\n", V / speed);
}

void printAns() {

}

void stress() {

}


int main(){
#ifdef DEBUG
    freopen("in", "r", stdin);
    freopen("test.txt", "r", stdin);
    freopen("out1", "w", stdout);
#endif
    if (1) {
        int k = 1;
        scanf("%d", &k);
        for (int tt = 0; tt < k; tt++) {
            printf("Case #%d: ", tt + 1);
            read();
            solve();
            printAns();
        }
    }
    else {
        stress();
    }

    return 0;
}

