#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>
#include <time.h>
#define fo(i,a,b) dfo(int,i,a,b)
#define fr(i,n) dfr(int,i,n)
#define fe(i,a,b) dfe(int,i,a,b)
#define fq(i,n) dfq(int,i,n)
#define nfo(i,a,b) dfo(,i,a,b)
#define nfr(i,n) dfr(,i,n)
#define nfe(i,a,b) dfe(,i,a,b)
#define nfq(i,n) dfq(,i,n)
#define dfo(d,i,a,b) for (d i = (a); i < (b); i++)
#define dfr(d,i,n) dfo(d,i,0,n)
#define dfe(d,i,a,b) for (d i = (a); i <= (b); i++)
#define dfq(d,i,n) dfe(d,i,1,n)
#define ffo(i,a,b) dffo(int,i,a,b)
#define ffr(i,n) dffr(int,i,n)
#define ffe(i,a,b) dffe(int,i,a,b)
#define ffq(i,n) dffq(int,i,n)
#define nffo(i,a,b) dffo(,i,a,b)
#define nffr(i,n) dffr(,i,n)
#define nffe(i,a,b) dffe(,i,a,b)
#define nffq(i,n) dffq(,i,n)
#define dffo(d,i,a,b) for (d i = (b)-1; i >= (a); i--)
#define dffr(d,i,n) dffo(d,i,0,n)
#define dffe(d,i,a,b) for (d i = (b); i >= (a); i--)
#define dffq(d,i,n) dffe(d,i,1,n)
#define ll long long
#define alok(n,t) ((t*)malloc((n)*sizeof(t)))
#define pf printf
#define sf scanf
#define pln pf("\n")
#define flsh fflush(stdout)
#include <map>
#include <algorithm>
#include <vector>
#include <set>
#include <iostream>
#include <string>
#include <sstream>
#include <iterator>
using namespace std;

struct edge {
    int s, e;
    int cap;
    int flow;
    edge *pair;
    edge(int s, int e, int cap): s(s), e(e), cap(cap), flow(0) {}
    int sunod(int v) {
        return v == s ? e : s;
    }
};

int N;
map<string, int> idx;
vector< vector<edge*> > adj(111111);
int S, E;
void init() {
    N = 0;
    S = E = -1;
    idx.clear();
}

int add_node() {
    // printf("add node %d\n", N);
    adj[N].clear();
    return N++;
}
void add_edge(int i, int j, int cap) {
    // printf("edge %d %d: %d\n", i, j, cap);
    edge *a = new edge(i, j, cap);
    edge *b = new edge(j, i, 0);
    a->pair = b;
    b->pair = a;
    adj[i].push_back(a);
    adj[j].push_back(b);
}

int word_idx(string s) {
    if (idx.find(s) == idx.end()) {
        idx[s] = N;
        int I = add_node();
        int J = add_node();
        add_edge(I, J, 1);
    }
    return idx[s];
}

vector<int> queue;
edge *parent[111111];
bool aug() {
    for (int i = 0; i < N; i++) {
        parent[i] = NULL;
    }
    queue.clear();
    queue.push_back(S);
    for (int f = 0; f < queue.size(); f++) {
        int i = queue[f];
        for (int nb = 0; nb < adj[i].size(); nb++) {
            edge *e = adj[i][nb];
            if (e->flow == e->cap) continue;
            int j = e->sunod(i);
            if (!parent[j]) {
                parent[j] = e;
                if (j == E) {
                    return true;
                }
                queue.push_back(j);
            }
        }
    }
    return false;
}

vector<string> split(string s) {
  vector<string> res;
  stringstream ss(s);
  string word;
  while(getline(ss, word, ' ')) res.push_back(word);
  return res;
}

int main() {
    int z;
    sf("%d", &z);
    fq(cas,z) {
        int n;
        sf("%d\n", &n);
        init();
        for (int i = 0; i < n; i++) {
            int R = add_node();
            if (i == 0) S = R;
            if (i == 1) E = R;

            string line;
            getline(cin, line);
            vector<string> spl = split(line);
            for (int j = 0; j < spl.size(); j++) {
                int W = word_idx(spl[j]);
                add_edge(R, W, 1);
                add_edge(W+1, R, 1);
            }
        }

        int ans = 0;
        while (aug()) {
            ans++;
            for (int curr = E; curr != S;) {
                edge *e = parent[curr];
                e->flow++;
                e->pair->flow--;
                curr = e->sunod(curr);
            }
        }
        pf("Case #%d: %d\n", cas, ans);
    }    
}
