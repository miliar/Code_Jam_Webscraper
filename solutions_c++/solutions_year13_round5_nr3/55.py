//#pragma comment(linker, "/STACK:16777216")

#include <iostream>
#include <cstdio>
#include <cmath>
#include <set>
#include <vector>
#include <map>
#include <cstring>
#include <sstream>
#include <algorithm>
#include <string>
#include <queue>
#include <fstream>

#define FOR(i,a,b) for(int i = (a); i <= (b); i++)
#define FR(i,a) for(int i = 0; i < (a); i++)
#define DR(i,a) for(int i = (a)-1; i >=0; i--)
#define DOWN(i,a,b) for(int i = (a); i >= (b); i--)
#define FORD(i,a,b) for(int i = (a), _b = (b); i >= _b; i--)
#define REPD(i,n) for(int i = (n) - 1; i >= 0; i--)
#define PB push_back
#define MP make_pair

#define F first
#define S second
#define RESET(c,x) memset(c,x,sizeof(c))
#define SIZE(c) (c).size()
#define ALL(c) (c).begin(), (c).end()

#define REP(i,a) for(int i = 0; i < (a); i++)

#define sqr(x) ((x)*(x))
#define oo 1000000009
using namespace std;
/*************************TEMPLATE**********************************/
long long convertToNum(string s)
{
    long long val = 0; FR(i,s.size()) val = val * 10 + s[i] - '0';
    return val;
}
char bu[50];
string convertToString(int a) {
    sprintf(bu,"%d",a);
    return string(bu);
}
long long GCD(long long x,long long y)  {
    if (!x) return y; if (!y) return x;
    if (x == y) return x; if (x < y) return GCD(x,y%x); else return GCD(x%y,y);
}
long long POW(long long x,long long y,long long Base){
    if (!y) return 1; long long u = POW(x,y/2,Base);
    u = (u * u) % Base;
    if (y % 2) return (u * x) % Base; else return u;
}
void extended_euclid(long long A, long long B, long long &x,long long &y) {
    if (A == 1 && B == 0) {
        x = 1;
        y = 0;
        return;
    }
    if (A < B) extended_euclid(B,A,y,x);
    else {
        long long xx,yy;
        extended_euclid(A%B,B,xx,yy);
        x = xx;
        y = yy - (A/B)*xx;

    }
}
//newstate = (newstate-1) & oldstate
/*******************************CODE HERE***********************************/
#define maxn 10000
int n,m,P;
int min_a[maxn], max_a[maxn];
vector< pair<int,int> > edge[maxn];
vector< pair<int,int> > edge_n[maxn];
bool onway[maxn];
bool dd[maxn];
int X[maxn], Y[maxn];
int d[maxn],g[maxn],t[maxn];
int C[maxn];

int ds[maxn];
bool isRes[maxn];
bool ijk() {
    FOR(i,1,n) dd[i] = true;
    FOR(i,1,n) d[i] = oo;
    d[1] = 0;

    do {
        int u = -1, minVal = oo;
        FOR(i,1,n)
        if (dd[i] && d[i] < minVal) {
            minVal = d[i];
            u = i;
        }
        if (u == -1) break;
        dd[u] = false;
        FR(i,edge[u].size()) {
            int v = edge[u][i].first;
            int id = edge[u][i].second;
            int cost;
            cost = C[id];
            if (d[v] > d[u] + cost) {
                d[v] = d[u] + cost;
            }
        }
    } while (true);
    FOR(i,1,n) dd[i] = true;
    FOR(i,1,n) g[i] = oo;
    g[2] = 0;
    do {
        int u = -1, minVal = oo;
        FOR(i,1,n)
        if (dd[i] && g[i] < minVal) {
            minVal = g[i];
            u = i;
        }
        if (u == -1) break;
        dd[u] = false;
        FR(i,edge_n[u].size()) {
            int v = edge_n[u][i].first;
            int id = edge_n[u][i].second;
            int cost;
            cost = C[id];
            if (g[v] > g[u] + cost) {
                g[v] = g[u] + cost;
            }
        }
    } while (true);

    FOR(i,1,P) {
        int st = X[ds[i]], fn = Y[ds[i]];
        if (d[2] == d[st] + C[ds[i]] + g[fn]) isRes[ds[i]] = true;
    }
}
void solve() {
    memset(isRes,false,sizeof(isRes));
    FR(state,(1<<m)) {
        FR(i,m)
        if (state&(1<<i)) C[i+1] = min_a[i+1];
        else C[i+1] = max_a[i+1];
        ijk();


    }
    FOR(i,1,P)
    if (!isRes[ds[i]]) {
        cout << ds[i] << endl;
        return;
    }

    cout << "Looks Good To Me" << endl;
}
int main() {
    freopen("test.in","r",stdin);
    freopen("test.out","w",stdout);
    int ntest;
    cin >> ntest;
    FOR(test,1,ntest) {
        cout << "Case #" << test << ": ";
        cin >> n >> m >> P;
        FOR(i,1,n) edge[i].clear();
        FOR(i,1,n) edge_n[i].clear();
        int u,v;
        FOR(i,1,m) {
            cin >> u >> v >> min_a[i] >> max_a[i];
            X[i] = u, Y[i] = v;
            edge[u].push_back(make_pair(v,i));
            edge_n[v].push_back(make_pair(u,i));
        }
        memset(onway,false,sizeof(onway));
        FOR(i,1,P) {
            cin >> ds[i];
            onway[ds[i]] = true;
        }
        solve();
    }
    return 0;
}
