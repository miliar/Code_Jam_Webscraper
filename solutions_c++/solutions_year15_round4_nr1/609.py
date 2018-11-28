#include <array>
#include <cassert>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <functional>
#include <string>
#include <vector>
#include <queue>
#include <map>
#include <set>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <thread>

using namespace std;

#define REP(i, n) for(int i = 0; i < (int)(n); ++ i)
#define FOR(i, b, e) for(auto i = b; i < e; ++ i)
#define all(x) (x).begin(), (x).end()

struct UnionFind {
    int n;
    vector<int> uf;
    vector<int> sz;

    UnionFind(int n) : n(n) {
        uf.resize(n);
        sz.resize(n);
        REP(i, n) uf[i] = i;
        REP(i, n) sz[i] = 1;
    }
    void merge(int x, int y) {
        x = find(x);
        y = find(y);
        uf[x] = y;
        sz[y] += sz[x];
        sz[x] = 0;
    }
    int size(int x) {
        x = find(x);
        return sz[x];
    }
    int find(int x) {
        if(x == uf[x]) return x;
        return uf[x] = find(uf[x]);
    }
};


int n, m;
vector<string> a;

pair<int, int> get_next(int i, int j, char cu) {
    if(cu == '>') {
        j++;
        while(j < m && a[i][j] == '.') j ++;
        if(j >= m) return {-1, -1};
        else return {i, j};
    }
    if(cu == '<') {
        j--;
        while(j >= 0 && a[i][j] == '.') j --;
        if(j < 0) return {-1, -1};
        else return {i, j};
    }
    if(cu == 'v') {
        i++;
        while(i < n && a[i][j] == '.') i ++;
        if(i == n) return {-1, -1};
        else return {i, j};
    }
    if(cu == '^') {
        i--;
        while(i >= 0 && a[i][j] == '.') i --;
        if(i < 0) return {-1, -1};
        else return {i, j};
    }
    assert(false);
}

int go() {
    pair< int, int > next[100][100];

    UnionFind uf( n * m );

    REP(i, n) REP(j, m) {
        if(a[i][j] != '.') {
            next[i][j] = get_next(i, j, a[i][j]);
//                printf("%d %d next %d %d\n", i, j, next[i][j].first, next[i][j].second);
            int v = (i*m+j);
            if(next[i][j] != pair<int, int>{-1, -1}) {
                int w = next[i][j].first * m + next[i][j].second;
//                printf("%d %d == %d %d\n", i, j, next[i][j].first, next[i][j].second);
                uf.merge(v, w);
            }
        }
    }

    set<int> heads;
    REP(i, n) REP(j, m) {
        if(a[i][j] != '.') {
            int v = (i*m+j);
            if(next[i][j] == pair<int, int>{-1, -1}) {
//                printf("%d %d -> dead\n", i, j);
                if(uf.size(v) == 1) {
                    // find neighbor
                    bool alive = false;
                    for(char ch : string("<>^v")) {
                        if( get_next(i, j, ch).first >= 0 )
                            alive = true;
                    }
                    if(!alive) return -1;
                }
                heads.insert( uf.find(v) );
            }
        }
    }
    return heads.size();
}

int main(int argc, char** argv) {
    int T;
    cin >> T;

    for(int kase = 1; kase <= T; ++ kase) {
        cin >> n >> m;
        a.resize(n);
        REP(i, n) cin >> a[i];

        int t = go();
        if(t >= 0)
            printf("Case #%d: %d\n", kase, t);
        else
            printf("Case #%d: %s\n", kase, "IMPOSSIBLE");
    }

    return 0;
}
