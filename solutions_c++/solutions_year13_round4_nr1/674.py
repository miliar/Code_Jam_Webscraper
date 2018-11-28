#include <stdio.h>
#include <algorithm>
#include <queue>
#include <vector>
#include <iostream>

using namespace std;
const long long mod = 1000002013LL;

struct Node
{
    long long s;
    long long p;
    long long type;
    Node(long long _s, long long _p, long long _t):s(_s), p(_p), type(_t){}
    bool operator < (const Node &rhs) const
    {
        return s < rhs.s || s == rhs.s && type > rhs.type;
    }
};

struct HeapNode
{
    long long s;
    long long p;
    HeapNode(long long _s, long long _p):s(_s), p(_p){}
    bool operator < (const HeapNode &rhs) const
    {
        return s < rhs.s;
    }
};

priority_queue<HeapNode> pq;
int n, m;

long long cal(long long si, long long ei, long long pi)
{
    return (n + n + si - ei + 1) * (ei - si) / 2  % mod * pi % mod;
}

int main()
{
    int T, cas = 0;
    scanf("%d", &T);
    while (T--)
    {
        scanf("%d%d", &n, &m);
        long long origin = 0;
        vector<Node> nodes;
        nodes.clear();
        for (int i = 0; i< m; i++)
        {
            long long si, ei, pi;
            scanf("%I64d%I64d%I64d", &si, &ei, &pi);
            origin = (origin + cal(si, ei, pi)) % mod;
            nodes.push_back(Node(si, pi, 1));
            nodes.push_back(Node(ei, pi, -1));
        }
        sort(nodes.begin(), nodes.end());
        long long best = 0;
        while (!pq.empty()) pq.pop();
        for (int i = 0; i < nodes.size(); i++)
        {
            if (nodes[i].type == 1)
            {
                pq.push(HeapNode(nodes[i].s, nodes[i].p));
            }
            else
            {
                while (nodes[i].p > 0)
                {
                    HeapNode top = pq.top();
                    pq.pop();
                    long long pnum = min(top.p, nodes[i].p);
                    nodes[i].p -= pnum;
                    top.p -= pnum;
                  //  printf("::%I64d %I64d %I64d %I64d\n", top.s, nodes[i].s, pnum,
                    //    cal(top.s, nodes[i].s, pnum));
                    best = (best + cal(top.s, nodes[i].s, pnum)) % mod;
                    if (top.p > 0) pq.push(top);
                }
            }
        }
      //  printf("%I64d %I64d\n", origin, best);
        printf("Case #%d: %I64d\n", ++cas, (origin - best + mod) % mod);
    }
    return 0;
}
