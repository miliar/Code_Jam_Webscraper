// CPPFLAGS=-std=gnu++11 -O3

#include <vector>
#include <set>
#include <iostream>
#include <sstream>
#include <algorithm>
#include <queue>
#include <stack>
#include <map>
#include <cmath>
#include <unordered_map>
#include <unordered_set>
#include <functional>
#include <cstdlib>
#include <string>
#include <cstdint>

#define D(x)

using namespace std;

struct label {
    int x, y;
    bool incoming;

    bool operator<(const label& other) const {
        if (x != other.x) return x < other.x;
        if (y != other.y) return y < other.y;
        return (!incoming && other.incoming);
    }
};

ostream& operator<<(ostream& os, const label& l) {
    return os << "{" << l.x << "," << l.y << "," <<
        (l.incoming ? "in" : "out") << "}";
}

struct edge {
    int capacity, flow;
};

template <typename T>
ostream& operator<<(ostream& os, const vector<T>& vec) {
    os << "[";
    for (int i = 0; i < vec.size(); i++) {
        if (i > 0) os << ", ";
        os << vec[i];
    }
    return os << "]";
}

template <typename T>
int get_id(map<T, int>& ids, const T& key) {
    typename map<T, int>::iterator it = ids.find(key);
    if (it != ids.end()) {
        return it->second;
    } else {
        int id = ids.size();
        ids[key] = id;
        D(cerr << key << " ==> " << id << endl);
        return id;
    }
}

void add_capacity(vector<map<int, edge>>& graph, map<label, int>& ids, const label& in, const label& out, int cap) {
    int id1 = get_id(ids, in);
    int id2 = get_id(ids, out);

    graph.resize(max((int) graph.size(), max(id1+1, id2+1)));
    graph[id1][id2].capacity += cap;
    graph[id2].insert(make_pair(id1, edge()));
}

int main() {
    int numCases;
    cin >> numCases;

    for (int T = 1; T <= numCases; T++) {
        int W, H, B;
        cin >> W >> H >> B;

        vector<vector<bool>> occ(W, vector<bool>(H));
        for (int i = 0; i < B; i++) {
            int X0, Y0, X1, Y1;
            cin >> X0 >> Y0 >> X1 >> Y1;

            for (int x = X0; x <= X1; x++) {
                for (int y = Y0; y <= Y1; y++) {
                    occ[x][y] = true;
                }
            }
        }

        map<label, int> ids;
        vector<map<int, edge>> graph;

        const vector<pair<int, int>> deltas{ {-1,0}, {1,0}, {0,-1}, {0,1} };

        label source{0, -1, false}, sink{0, -1, true};

        for (int x = 0; x < W; x++) {
            for (int y = 0; y < H; y++) {
                if (occ[x][y]) continue;

                label incoming{x, y, true};
                label outgoing = incoming, adj = incoming;
                outgoing.incoming = false;

                add_capacity(graph, ids, incoming, outgoing, 1);

                for (int delta = 0; delta < 4; delta++) {
                    const pair<int, int>& deltaPair = deltas[delta];
                    int dx = deltaPair.first, dy = deltaPair.second;

                    adj.x = outgoing.x+dx;
                    adj.y = outgoing.y+dy;
                    if (adj.x < 0 || adj.x >= W || adj.y < 0 || adj.y >= H) continue;
                    if (occ[adj.x][adj.y]) continue;

                    add_capacity(graph, ids, outgoing, adj, 1);
                }

                if (y == 0) {
                    add_capacity(graph, ids, source, incoming, 1);
                } else if (y == H-1) {
                    add_capacity(graph, ids, outgoing, sink, 1);
                }
            }
        }

        D(cerr << "doing max flow" << endl);

        int totalFlow = 0;
        int source_id = get_id(ids, source), sink_id = get_id(ids, sink);
        while (true) {
            D(cerr << "iteration" << endl);
            vector<int> current{source_id}, next;
            vector<int> parent(ids.size(), -1);
            set<int> visited;

            bool found = false;
            while (!found && !current.empty()) {
                for (int i = 0; i < current.size(); i++) {
                    int here = current[i];

                    if (visited.find(here) != visited.end()) continue;
                    visited.insert(here);
                    D(cerr << "visiting " << here << endl);

                    if (here == sink_id) {
                        int cap = -1;
                        for (int id = sink_id; id != source_id; id = parent[id]) {
                            D(cerr << "id=" << id << " parent=" << parent[id] << endl);
                            const edge& e = graph[parent[id]][id];
                            int thisCap = e.capacity - e.flow;

                            if (cap == -1 || thisCap < cap) {
                                cap = thisCap;
                            }
                        }

                        for (int id = sink_id; id != source_id; id = parent[id]) {
                            D(cerr << "adding "<<cap<<" from "<<parent[id]<<" to "<<id<<endl);
                            graph[parent[id]][id].flow += cap;
                            graph[id][parent[id]].flow -= cap;
                        }
                        totalFlow += cap;
                        found = true;
                        break;
                    }

                    for (map<int, edge>::iterator it = graph[here].begin(); it != graph[here].end(); it++) {
                        int there = it->first;
                        D(cerr << " adjacent: " << there << endl);
                        edge& e = it->second;

                        if (e.flow < e.capacity && parent[there] == -1) {
                            next.push_back(there);
                            parent[there] = here;
                        }
                    }
                }
                current = next;
                next.clear();
            }

            if (!found) break;
        }
            
        cout << "Case #" << T << ": ";
        cout << totalFlow;
        cout << endl;
    }
}
