#include <cstdio>
#include <cstdlib>
#include <cassert>
#include <iostream>
#include <set>
#include <vector>
#include <cstring>
#include <string>
#include <algorithm>
#include <numeric>
#include <cmath>
#include <unordered_map>
#include <queue>
using namespace std;
typedef long long ll;
typedef vector<int> vi;
typedef vector<ll> vl;
typedef vector<vi> vvi;
typedef vector<vl> vvl;
typedef vector<double> vd;
typedef pair<int, int> pii;
typedef pair<double, double> pdd;
typedef vector<pii> vii;
typedef vector<string> vs;

struct TEdge {
    int from, to;
    ll capacity, flow;
    ll cost;
    TEdge* reverse;
};

TEdge edgePool[1000000];
int edgePoolPtr = 0;

typedef vector<TEdge*> ve;
vector< ve > edges; //resize

int SOURCE, TARGET; //assign

TEdge* AddEdge(int from, int to, ll capacity, ll cost = 0) {
    TEdge* e1 = &edgePool[edgePoolPtr++];
    TEdge* e2 = &edgePool[edgePoolPtr++];
    TEdge fw = {from, to, capacity, 0, cost, e2};
    TEdge bw = {to, from, 0, 0, cost, e1};
    assert(from < edges.size());
    assert(to < edges.size());
    *e1 = fw;
    *e2 = bw;
    edges[from].push_back(e1);
    edges[to].push_back(e2);
    return e1;
}

inline ll AvailableCapacity(const TEdge* p) {
    return (p->capacity - p->flow);
}

vector<int> Distances;
vector<size_t> Ptr;
int N;
void BFS() {
    deque<int> q;
    Distances.assign(N, -1);
    Distances[SOURCE] = 0;
    q.push_back(SOURCE);
    while (!q.empty()) {
        int p = q.front();
        q.pop_front();
        for (size_t i = 0; i < edges[p].size(); i++) {
            if (!AvailableCapacity(edges[p][i]))
                continue;
            int c = edges[p][i]->to;
            if (Distances[c] == -1) {
                Distances[c] = Distances[p] + 1;
                q.push_back(c);
            }
        }
    }
}
ll DFS(int p, ll fl) {
    if (fl == 0)
        return 0;
    if (p == TARGET)
        return fl;
    ll res = 0;

    for (size_t &i = Ptr[p]; Ptr[p] < edges[p].size() && fl != 0; ++i) {
        if (!AvailableCapacity(edges[p][i])) {
            continue;
        }
        if (Distances[edges[p][i]->from] + 1 != Distances[edges[p][i]->to])
            continue;
        ll pushed = DFS(edges[p][i]->to, min(fl, AvailableCapacity(edges[p][i])));
        fl -= pushed;
        res += pushed;
        edges[p][i]->flow += pushed;
        edges[p][i]->reverse->flow -= pushed;
        if (fl == 0)
            break;
    }
    return res;
}
ll GetMaxFlow() {
    N = (int)edges.size();
    ll res = 0;
    while (true) {
        BFS();
        Ptr.assign(N, 0);
        ll p = DFS(SOURCE, 1e18 / 2);
        if (!p)
            break;
        res += p;
    }
    return res;
}

char buf[100000];

int main() {
    int T;
    cin >> T;
    for (int test = 1; test <= T; ++test) {
        edgePoolPtr = 0;
        edges.clear();
        printf("Case #%d: ", test);
        int n;
        cin >> n;
        vector<vs> sent(n);
        unordered_map<string, int> ind;
        for (int i = 0; i < n; ++i) {
            string s;
            char c = ' ';
            while (scanf("%s%c", buf, &c) == 2) {
                s = string(buf);
                if (c == '\n') break;
                sent[i].push_back(s);
            }
            sent[i].push_back(s);
//            for (int j = 0; j < sent[i].size(); ++j) cerr << sent[i][j] << ' '; cerr << endl;
            sort(sent[i].begin(), sent[i].end());
            sent[i].resize(unique(sent[i].begin(), sent[i].end()) - sent[i].begin());
        }
        for (int i = 0; i < n; ++i) for (int j = 0; j < sent[i].size(); ++j) {
            if (!ind.count(sent[i][j])) {
                int sz = ind.size();
                ind[sent[i][j]] = sz;
            }
        }
        SOURCE = 0;
        TARGET = 1;
        edges.resize(n + 2*ind.size());
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < sent[i].size(); ++j) {
                int x = ind[sent[i][j]];
                assert(x < ind.size());
                AddEdge(i, n + x, 1);
                AddEdge(n + x + ind.size(), i, 1);
            }
        }
        for (int i = 0; i < ind.size(); ++i) {
            AddEdge(n + i, n + i + ind.size(), 1);
        }
        cout << GetMaxFlow() << endl;
    }
    return 0;
}
