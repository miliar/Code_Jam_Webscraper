#include <cstdio>
#include <cstring>
#include <algorithm>
#include <string>
#include <map>
#include <iostream>
#include <sstream>

const int N = 15000;
const int M = 1000000;
const int INF = 1 << 29;

struct Edge {
    int to, flow, capa, next;
    Edge(int v = 0, int c = 0, int n = 0): to(v), flow(0), capa(c), next(n) {}
} g[M];
int first[N], arc[N], edge_count;
int vs, vt;

void add_edge(int u, int v, int c) {
    edge_count ++;
    g[edge_count] = Edge(v, c, first[u]), first[u] = edge_count;
    g[M - edge_count] = Edge(u, 0, first[v]), first[v] = M - edge_count;
    //printf("%d %d %d\n", u, v, c);
}

int queue[N], label[N];

bool bfs() {
    memset(label, 0, sizeof(label));
    queue[0] = vs;
    label[vs] = 1;
    for (int head = 0, tail = 0; head <= tail; ++ head) {
        int u = queue[head];
        for (int iter = first[u]; iter; iter = g[iter].next) {
            int v = g[iter].to;
            if (g[iter].flow < g[iter].capa && label[v] == 0) {
                label[v] = label[u] + 1;
                queue[++ tail] = v;
            }
        }
    }
    return label[vt];
}

int dfs(int u, int d) {
    if (u == vt) {
        return d;
    }
    int delta = 0;
    for (int &iter = arc[u]; iter; iter = g[iter].next) {
        int v = g[iter].to;
        if (g[iter].flow < g[iter].capa && label[u] + 1 == label[v]) {
            int r = dfs(v, std::min(d - delta, g[iter].capa - g[iter].flow));
            g[iter].flow += r;
            g[M - iter].flow -= r;
            delta += r;
            if (delta == d) {
                break;
            }
        }
    }
    return delta;
}

std::map<std::string, int> ids;
int counter;

int GetId(std::string& s) {
    if (ids.find(s) == ids.end()) {
        ids[s] = ++ counter;
    }
    return ids[s];
}

void Init() {
    counter = 0;
    ids.clear();
    memset(first, 0, sizeof(first));
    edge_count = 0;
}

int n, m;

int main() {
    //std::ios::sync_with_stdio(false);
    int test;
    std::cin >> test;
    for (int t = 1; t <= test; ++ t) {
        Init();
        std::cin >> n;
        std::string string;
        std::getline(std::cin, string);

        vs = N - 1;
        vt = N - 2;
        for (int i = 1; i <= n; ++ i) {
            if (i == 1) {
                add_edge(i, vt, INF);
            } else if (i == 2) {
                add_edge(vs, i, INF);
            }
            std::getline(std::cin, string);
            std::stringstream buffer;
            buffer << string;
            while (buffer >> string) {
                int id = GetId(string);
                //std::cout << string << " " << id << std::endl;
                add_edge(n + id, i, 1);
                add_edge(i, n + id, 1);
            }
        }
        int flow = 0;
        while (bfs()) {
            memcpy(arc, first, sizeof(first));
            flow += dfs(vs, INF);
        }
        printf("Case #%d: %d\n", t, flow);
    }
    return 0;
}
