/*
g++ -g -DBUG -D_GLIBCXX_DEBUG -std=c++11 -Wall -Wfatal-errors -o cjam{,.cpp}
g++ -O3 -std=c++11 -Wall -Wfatal-errors -o cjam{,.cpp}
ulimit -s 1268435456
*/
#include <bits/stdc++.h>
#ifdef BUG
    #include "debug.hpp"
#else
    #define DEBUG(var)
#endif
#define CASE(i) "Case #" << (i) + 1 << ": "

using namespace std;
template<class T1, class T2> inline istream &
operator>>(istream & fin, pair<T1, T2> & pr)
{ fin >> pr.first >> pr.second; return fin; }
template<class T0, class T1, class T2> inline istream &
operator>>(istream & fin, tuple<T0, T1, T2> & t)
{ fin >> get<0>(t) >> get<1>(t) >> get<2>(t); return fin; }
template<class T> inline istream &
operator>>(istream & fin, vector<T> & a) {
for(auto & u: a) fin >> u; return fin; }
template<class T, size_t n> inline istream &
operator>>(istream & fin, array<T, n> & a) {
for(auto & u: a) fin >> u; return fin; }
/* ------------------------------ */

typedef struct {
    const size_t next; /* the other end of edge */
    const int cap; /* capacities can be non-symmetric */
    int flow; /* flows have sign, are symmetric with diff. signs */
    const size_t i; /* adj[next][i]:self; index of self in adj vector of next*/
} edge_t;

int push_flow(const size_t node,
              const int flow, /* incoming flow */
              const size_t sink,
              vector<vector<edge_t>> & adj,
              vector<bool> & tag)
{
    if(node == sink) return flow;

    tag[node] = true;
    int acc = 0; /* total flow pushed out of this node */

    for(auto & e: adj[node])
        if(!tag[e.next] && e.flow < e.cap)
        {
            const auto fl = min(flow - acc, e.cap - e.flow);
            const auto inc = push_flow(e.next, fl, sink, adj, tag);

            if(inc)
            {
                acc += inc;
                e.flow += inc;
                adj[e.next][e.i].flow -= inc;

                if(acc == flow) break;
            }
        }

    tag[node] = !acc; // false;  XXX verify this!!!
    return acc;
}

int max_flow(const size_t src,
             const size_t sink,
             vector<vector<edge_t>> & adj)
{
    const auto size = adj.size();

    /* need to tag to avoid looping or visiting a node twice */
    vector< bool > tag(size, false );

    /* push infinite flow to source node */
    const auto inf = numeric_limits<int>::max();
    while(push_flow(src, inf, sink, adj, tag))
        fill(begin(tag), end(tag), false); /* XXX */

    /* add up all to flow out of source node */
    int out = 0;
    for(const auto & e: adj[src]) out += e.flow;

    return out;
}

inline size_t
technobabble()
{
    size_t n;
    cin >> n;
    vector<pair<string, string>> w(n);
    cin >> w;

    vector<pair<size_t, size_t>> a(n);
    size_t cnt = 1;

    {
        unordered_map<string, size_t> idx;

        for(size_t i = 0; i < n; ++ i)
        {
            auto & ref = idx[w[i].first];
            if(ref == 0) ref = cnt++;
            a[i].first = ref;
        }
    }

    const auto tcnt = cnt;

    {
        unordered_map<string, size_t> idx;

        for(size_t i = 0; i < n; ++ i)
        {
            auto & ref = idx[w[i].second];
            if(ref == 0) ref = cnt++;
            a[i].second = ref;
        }
    }

    ++cnt;
    vector<vector<edge_t>> adj(cnt);

    const auto src = 0;
    const auto sink = cnt - 1;

    const auto add =  /* inits a *directed* edge (u, v) w/ flow cap */
        [&adj](const size_t u, const size_t v, const int cap, const int fl=0){
            /* both should have same 'cap' for undirected edge */
            adj[u].push_back({ v, cap, fl, adj[v].size() });
            adj[v].push_back({ u, 0, -fl, adj[u].size()-1});
        };

    for(size_t i = 1; i < tcnt; ++i)
        add(src, i, 1);

    for(size_t i = tcnt; i < sink; ++ i)
        add(i, sink, 1);

    for(const auto & pr: a)
        add(pr.first, pr.second, 1);

    auto out = max_flow(src, sink, adj);
    for(size_t i = 1; i + 1 < cnt; ++ i)
    {
        bool fail = true;
        for(const auto & e: adj[i])
            if((e.next == src || e.next == sink) && e.flow != 0)
            {
                fail = false;
                break;
            }

        if(fail) ++ out;
    }

    return n - out;
}

int main(const int argc, char * argv [])
{
    ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);

    size_t ncase;
    cin >> ncase;

    for(size_t i = 0; i < ncase; ++i, cout << '\n')
        cout << CASE(i) << technobabble();

    return EXIT_SUCCESS;
}
