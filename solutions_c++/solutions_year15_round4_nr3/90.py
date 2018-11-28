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
const int N = -1;
const int INF = 1e9;

int n;
vector < vector < string > > b;
vector < vector < int > > g;

vector < string > split(string s) {
    vector < string > t;
    for (int i = 0; i < (int)s.size(); ) {
        for (; i < (int)s.size() && s[i] == ' '; i++);
        if (i == (int)s.size()) break;
        int j = i;
        for (; i < (int)s.size() && s[i] != ' '; i++);
        t.pb(s.substr(j, i - j));
    }
    return t;
}

void read() {
    cin >> n;
    map < string, int > q;
    b.assign(n, vector < string >());
    g.assign(n, vector < int > ());
    for (int i = 0; i < n; i++) {
        string s;
        getline(cin, s); 
        if (s.empty()) {
            i--;
            continue;
        }
        //db(s.length());
        b[i] = split(s);
    }
    int cur = 0;
    for (int i = 0; i < n; i++)
        for (auto x: b[i]) {
            if (q.count(x) == 0)
                q[x] = cur++;
            g[i].pb(q[x]);
        }

    int ans = INF;

    //db(cur);
    for (int mask = 0; mask < (1 << (n - 2)); mask++) {
        if (mask % 1000 == 0)
            db(mask);
        vector < int > tmp(cur);    
        for (auto x: g[0])
            tmp[x] |= 1;
        for (auto x: g[1])
            tmp[x] |= 2; 


        for (int i = 0; i < n - 2; i++) {
            int val = 0;
            if (((mask >> i) & 1) == 1)
                val = 1;
            else 
                val = 2;
            for (auto x: g[i + 2])
                tmp[x] |= val;
        }
        int res = 0;
        for (auto x: tmp)
            res += x == 3;
        ans = min(ans, res);
    } 
    printf("%d\n", ans);
}

void solve() {

}

void printAns() {

}

void stress() {

}


int main(){
#ifdef DEBUG
    freopen("in", "r", stdin);
    freopen("out", "w", stdout);
    freopen("test.txt", "r", stdin);
#endif
    if (1) {
        int k = 1;
        scanf("%d", &k);
        for (int tt = 0; tt < k; tt++) {
            db(tt);
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

