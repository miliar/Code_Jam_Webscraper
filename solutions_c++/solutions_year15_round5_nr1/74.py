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
const int N = 1e6 + 10;
const int INF = 1e9;

struct Event {
    int t, type, id;
    Event() { }
    Event(int t, int type, int id): t(t), type(type), id(id) { }
};

int n, D;
int S0, M0, AS, AM, CS, CM, RS, RM;
int s[N];
int m[N];
vector < int > e[N];
long long sum;
int status[N];
int p[N];


void read() {
    scanf("%d%d", &n, &D);
    scanf("%d%d%d%d", &S0, &AS, &CS, &RS);
    scanf("%d%d%d%d", &M0, &AM, &CM, &RM);
    for (int i = 0; i < n; i++)
        e[i].clear();
    sum = 0;
    for (int i = 0; i < n; i++)
        status[i] = 0;
}

bool cmp(const Event & a, const Event & b) {
    if (a.t != b.t) return a.t < b.t;
    return a.type > b.type;
}

void dfs1(int v) {
    assert(status[v] != 2);
    if (status[v] == 1) {
        status[v] = 2;
        sum++;
    } 
    else
       return; 
    for (auto u: e[v])
        dfs1(u);
}

void dfs0(int v) {
    assert(status[v] != 1);
    if (status[v] == 2) {
        sum--;
        status[v] = 1;
    } 
    else
        return;
    for (auto u: e[v])
        dfs0(u);
}

void solve() {
    s[0] = S0; 
    m[0] = M0;
    for (int i = 1; i < n; i++) {
        s[i] = (s[i - 1] * 1ll * AS + CS) % RS;
        m[i] = (m[i - 1] * 1ll * AM + CM) % RM;
    }
    for (int i = 1; i < n; i++) {
        int u = m[i] % i;
        e[u].pb(i);
        p[i] = u;
        //db2(u, i);
    }
    long long answer = 0;
    vector < Event > event; 
    for (int i = 0; i < n; i++) {
        event.pb(Event(s[i], 1, i));
        event.pb(Event(s[i] + D, -1, i));
    }
    sort(event.begin(), event.end(), cmp);

    for (auto x: event) {
        if (x.type == 1) {
            int v = x.id;
            assert(status[v] == 0);
            if (v == 0 || status[p[v]] == 2) {
                status[v] = 1;
                dfs1(x.id); 
            }
            else
                status[v] = 1;
        }
        else {
            int v = x.id;
            assert(status[v] != 0);
            if (status[v] == 2) {
                dfs0(v);
            }
            status[v] = 0;
        }
        answer = max(answer, sum);
    }
    cout << answer << endl;
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
            //cerr << "sdf\n";
            printf("Case #%d: ", tt + 1);
            //cerr << "sdf\n";
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

