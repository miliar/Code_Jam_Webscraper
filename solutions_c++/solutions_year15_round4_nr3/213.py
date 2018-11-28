#include <cassert>
#include <vector>
#include <algorithm>
#include <queue>
#include <sstream>
#include <cstdio>
#include <iostream>
#include <cstring>

using namespace std;

const int INF = 10000;
const int MAXV = 9000;
const int MAXE = 30000;

int last_edge[MAXV], cur_edge[MAXV], dist[MAXV];
int prev_edge[MAXE], cap[MAXE], flow[MAXE], adj[MAXE];
int nedges;

void d_init() {
    nedges = 0;
    memset(last_edge, -1, sizeof last_edge);
}

void d_edge(int v, int w, int capacity, int revcap, bool r = false) {
    assert(v < MAXV);
    assert(w < MAXV);
    assert(nedges < MAXE);

    prev_edge[nedges] = last_edge[v];
    cap[nedges] = capacity;
    adj[nedges] = w;
    flow[nedges] = 0;
    last_edge[v] = nedges++;

    if(!r) d_edge(w, v, revcap, capacity, true);
}

bool d_auxflow(int source, int sink) {
    queue<int> q;
    q.push(source);

    memset(dist, -1, sizeof dist);
    dist[source] = 0;
    memcpy(cur_edge, last_edge, sizeof last_edge);

    while(!q.empty()) {
        int v = q.front(); q.pop();
        for(int i = last_edge[v]; i != -1; i = prev_edge[i]) {
            if(cap[i] - flow[i] == 0) continue;

            if(dist[adj[i]] == -1) {
                dist[adj[i]] = dist[v] + 1;
                q.push(adj[i]);

                if(adj[i] == sink) return true;
            }
        }
    }

    return false;
}

int d_augmenting(int v, int sink, int c) {
    if(v == sink) return c;

    for(int& i = cur_edge[v]; i != -1; i = prev_edge[i]) {
        if(cap[i] - flow[i] == 0 || dist[adj[i]] != dist[v] + 1)
            continue;

        int val;
        if(val = d_augmenting(adj[i], sink, min(c, cap[i] - flow[i]))) {
            flow[i] += val;
            flow[i^1] -= val;
            return val;
        }
    }

    return 0;
}

int dinic(int source, int sink) {
    int ret = 0;
    while(d_auxflow(source, sink)) {
        int flow;
        while(flow = d_augmenting(source, sink, 0x3f3f3f3f))
            ret += flow;
    }

    return ret;
}

int main() {
    int t;
    cin >> t;

    for (int z = 1; z <= t; z++) {
        int N;
        cin >> N;
        cin.ignore();

        string sentences[N];
        vector<string> words;

        for (int i = 0; i < N; i++) {
            getline(cin, sentences[i]);
            stringstream sstr(sentences[i]);

            string word;
            while (sstr >> word)
                words.push_back(word);
        }

        sort(words.begin(), words.end());
        words.erase(unique(words.begin(), words.end()), words.end());

        int ENGLISH = 0, FRENCH = 1;
        int FIRST_SENTENCE = 2;
        int FIRST_WORD = 2 + N;
        d_init();

        d_edge(ENGLISH, FIRST_SENTENCE, INF, 0);
        d_edge(FIRST_SENTENCE + 1, FRENCH, INF, 0);

        for (int i = 0; i < N; i++) {
            stringstream sstr(sentences[i]);

            string word;
            while (sstr >> word) {
                int id = lower_bound(words.begin(), words.end(), word) - words.begin();
                d_edge(FIRST_SENTENCE + i, FIRST_WORD + 2*id, INF, 0);
                d_edge(FIRST_WORD + 2*id + 1, FIRST_SENTENCE + i, INF, 0);
            }
        }

        for (int i = 0; i < words.size(); i++)
            d_edge(FIRST_WORD + 2*i, FIRST_WORD + 2*i + 1, 1, 10000);

        int ans = dinic(ENGLISH, FRENCH);
        cout << "Case #" << z << ": " << ans << endl;
    }
}
