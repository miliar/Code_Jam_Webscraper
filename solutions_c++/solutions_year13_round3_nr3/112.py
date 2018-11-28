#pragma comment(linker, "/STACK:102400000,102400000")
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <iostream>
#include <algorithm>
#include <queue>
using namespace std;

#define INF 0x3f3f3f3f
#define LL long long
#define eps 1e-8
#define lson (pos << 1)
#define rson (pos << 1 | 1)
#define ZERO 500
template<class T> void checkMax(T &a, T b)
{
    a = max(a, b);
}
template<class T> void checkMin(T &a, T b)
{
    a = min(a, b);
}
struct Node
{
    int d, n, w, e, s;
    int deltaD, deltaP, deltaS;
    bool operator < (const Node &cur)const
    {
        return d > cur.d;
    }
    void read()
    {
        scanf("%d%d%d%d%d%d%d%d", &d, &n, &w, &e, &s, &deltaD, &deltaP, &deltaS);
        w *= 2;
        e *= 2;
        deltaP *= 2;
    }
};
priority_queue<Node> que;
vector<Node> list;
int n, h[1005];
int main()
{
    freopen("C-small-attempt0.in", "r", stdin);
    freopen("C.out", "w", stdout);
    int t, cas = 1, i, j, k;
    Node tribe;
    scanf("%d", &t);
    while(t--)
    {
        scanf("%d", &n);
        while(!que.empty()) que.pop();
        for(i = 1; i <= n; i++)
        {
            tribe.read();
            que.push(tribe);
        }
        memset(h, 0, sizeof(h));
        int ans = 0;
        while(!que.empty())
        {
            list.clear();
            int today = que.top().d;
            while(!que.empty())
            {
                if(que.top().d != today)
                    break;
                list.push_back(que.top());
                que.pop();
            }
            for(i = 0; i < list.size(); i++)
            {
                tribe = list[i];
                for(k = ZERO + tribe.w; k <= ZERO + tribe.e; k++)
                {
                    if(h[k] < tribe.s)
                    {
                        ans++;
                        break;
                    }
                }
            }
            for(i = 0; i < list.size(); i++)
            {
                tribe = list[i];
                for(k = ZERO + tribe.w; k <= ZERO + tribe.e; k++)
                    h[k] =  max(h[k], tribe.s);
                tribe.n--;
                tribe.d += tribe.deltaD;
                tribe.w += tribe.deltaP;
                tribe.e += tribe.deltaP;
                tribe.s += tribe.deltaS;
                if(tribe.n != 0)
                    que.push(tribe);
            }
        }
        printf("Case #%d: %d\n", cas++, ans);
    }
    return 0;
}
