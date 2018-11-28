#include <iostream>
#include <vector>
#include <sstream>
#include <string>
#include <map>
#include <deque>
#include <list>
#include <algorithm>
#include <numeric>
#include <queue>
#include <set>
#include <functional>
#include <cstring>
#include <stdio.h>
#include <ctype.h>
#include <assert.h>

#define max3(x, y, z) max((x), max((y), (z)))
#define max4(w, x, y, z) max(max((x), (y)), max((z), (w)))
#define min3(x, y, z) min((x), min((y), (z)))
#define min4(w, x, y, z) min(min((x), (y)), min((z), (w)))

using namespace std;

struct UnionFind {
    vector<int> data;
    UnionFind(int size) : data(size, -1) { }
    bool unionSet(int x, int y) {
        x = root(x); y = root(y);
        if (x != y) {
            if (data[y] < data[x]) swap(x, y);
            data[x] += data[y]; data[y] = x;
        }
        return x != y;
    }
    bool findSet(int x, int y) {
        return root(x) == root(y);
    }
    int root(int x) {
        return data[x] < 0 ? x : data[x] = root(data[x]);
    }
    int size(int x) {
        return -data[root(x)];
    }
};

typedef int Weight;
struct Edge {
    int src, dst;
    Weight weight;
    Edge(int src, int dst, Weight weight) :
        src(src), dst(dst), weight(weight) { }
};

bool operator < (const Edge &e, const Edge &f) {
    return e.weight != f.weight ? e.weight > f.weight : // !!INVERSE!!
    e.src != f.src ? e.src < f.src : e.dst < f.dst;
}

typedef vector<Edge> Edges;
typedef vector<Edges> Graph;
typedef vector<Weight> Array;
typedef vector<Array> Matrix;
typedef long long ll;
typedef unsigned long long ull;

#define FOR(i, N) for (int i = 0; i < N; i++)
#define RFOR(i, N) for (int i = N - 1; i >= 0; i--)
#define REP(i, from, to) for (int i = from; i <= to; i++)
#define MP(x, y) make_pair((x), (y))

// ワーシャルフロイド(g ... 無効間はINFが必要)
void shortestPath(const Matrix &g, Matrix &dist) {
    int n = g.size();
    dist = g;
    //inter.assign(n, vector<int>(n, -1));
    FOR(k, n) FOR(i, n) FOR(j, n) {
        if (dist[i][j] > dist[i][k] + dist[k][j]) {
            dist[i][j] = dist[i][k] + dist[k][j];
            //inter[i][j] = k;
        }
    }
}

/////////////////////////////////////////////////////////////////////////////////////////

int T, N, X;


void insert(vector<int>& d, int n, int X)
{
    for (auto& dk : d) {
        if (dk + n <= X) {
            if (dk) dk = X + 1;
            else dk = n;
            return;
        }
    }
    d.push_back(n);
}

int main(void) {
    cin >> T;

    FOR(i, T) {
        cin >> N >> X;

        vector<int> files(N);
        FOR(j, N) cin >> files[j];

        sort(files.begin(), files.end());
        reverse(files.begin(), files.end());

        vector<int> disks;

        FOR(j, N) {
            insert(disks, files[j], X);
        }

        printf("Case #%d: %d\n", i + 1, disks.size());
    }
    
}
