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
const int N = 1e5;
const int INF = 1e9;

int n, k;
int s[N];

void read() {
    scanf("%d%d", &n, &k); 
    for (int i = 0; i < n - k + 1; i++)
        scanf("%d", &s[i]);
}

void solve() {
    long long s0 = s[0];
    vector < int > len;
    for (int i = 0; i < k; i++) {
        int l = 0;
        int r = 0;
        int dx = 0;
        for (int v = i; v + k < n; v += k) {
            dx += s[v + 1] - s[v];
            l = min(l, dx);
            r = max(r, dx);
        }
        s0 -= (-l);
        len.pb(r - l);
    }
    //for (auto x: len)
        //cerr << x << " ";
    //cerr << endl;
    int shift = 0;
    int mx = 0; 
    for (auto x: len)
        mx = max(x, mx);

    for (auto x: len)
        shift += mx - x; 
    long long tmp = abs(s0 / k);
    s0 += (tmp + 2) * k;
    long long g = s0 % k;
    if (g > shift) {
        //cerr << "here\n";
        mx++;
    }
    
    cout << mx << endl;




}

void printAns() {

}

void stress() {

}


int main(){
#ifdef DEBUG
    freopen("in", "r", stdin);
    freopen("out", "w", stdout);
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

