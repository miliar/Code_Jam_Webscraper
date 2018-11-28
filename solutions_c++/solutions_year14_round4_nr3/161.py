

#include <iostream>
#include <iomanip>
#include <cstdio>
#include <stdio.h>
#include <cstdlib>
#include <bitset>
#include <memory>
#include <algorithm>
#include <set>
#include <map>
#include <vector>
#include <list>
#include <string>
#include <cstring>
#include <fstream>
#include <functional>
#include <stack>
#include <complex>
#include <wchar.h>
#include <wctype.h>
#include <cmath>
#include <queue>
#include <ctime>
#include <numeric>
#include <bitset>


using namespace std;

template<typename T> T mabs(const T &a){ return a<0?-a:a;}
#define rep(x,y,z) for(int x=(y),e##x=(z);x<e##x;x++)
#define SQR(x) ((x)*(x))
#define all(c) (c).begin(), (c).end()

typedef long long ll;
typedef long double ld;
typedef unsigned long long ull;
typedef unsigned int ui;
typedef short int si;
typedef pair<int,int> pii;
typedef pair<ll,ll> pll;
typedef pair<double, int> pdi;
typedef vector<int> vi;

typedef pair<int, string> pis;

struct Bd
{
    int x1, y1, x2, y2;
    int dist;
    vector<pii> edges;
    bool was = 0;
    Bd(int _x1 = 0, int _y1 = 0, int _x2 = 0, int _y2 = 0)
    {
        x1 = _x1, y1 = _y1, x2 = _x2, y2 = _y2;
        dist = 1e9;
        was = 0;
        edges.clear();
    }
} bds[1005];

bool between(int y, int y1, int y2)
{
    if (y >= y1 && y <= y2)
    {
        return true;
    }
    return false;
}

int getDist(Bd &b1, Bd &b2)
{
    if (b1.x1 > b2.x1)
    swap(b1, b2);
    if (between(b1.x1, b2.x1, b2.x2) || between(b1.x2, b2.x1, b2.x2))
    {
        if (between(b1.y1, b2.y1, b2.y2) || between(b1.y2, b2.y1, b2.y2))
        return 0;
        if (between(b2.y1, b1.y1, b1.y2) || between(b2.y2, b1.y1, b1.y2))
        return 0;
        
        if (b2.y1 >= b1.y2)
        return b2.y1 - b1.y2;
        else
        return b1.y1 - b2.y2;
    }
    if (between(b1.y1, b2.y1, b2.y2) || between(b1.y2, b2.y1, b2.y2))
    {
        if (between(b1.x1, b2.x1, b2.x2) || between(b1.x2, b2.x1, b2.x2))
        return 0;
        if (between(b2.x1, b1.x1, b1.x2) || between(b2.x2, b1.x1, b1.x2))
        return 0;
        if (b2.x1 >= b1.x2)
        return b2.x1 - b1.x2;
        else
        return b1.x1 - b2.x2;
    }
    swap(b1, b2);
    if (between(b1.x1, b2.x1, b2.x2) || between(b1.x2, b2.x1, b2.x2))
    {
        if (b2.y1 >= b1.y2)
        return b2.y1 - b1.y2;
        else
        return b1.y1 - b2.y2;
    }
    if (between(b1.y1, b2.y1, b2.y2) || between(b1.y2, b2.y1, b2.y2))
    {
        if (b2.x1 >= b1.x2)
        return b2.x1 - b1.x2;
        else
        return b1.x1 - b2.x2;
    }
    
//    not between
    if (b1.x1 > b2.x2)
    {
        if (b1.y1 > b2.y2)
        {
            return max(b1.x1 - b2.x2, b1.y1 - b2.y2);
        }
        else
        {
            return max(b1.x1 - b2.x2, b2.y1 - b1.y2);
        }
    }
    else //b2.x1 > b1.x2
    {
        if (b1.y1 > b2.y2)
        {
            return max(b2.x1 - b1.x2, b1.y1 - b2.y2);
        }
        else
        {
            return max(b2.x1 - b1.x2, b2.y1 - b1.y2);
        }
    }
    throw 1;//what the hell?
    return 0;
}

void dijkstra(int bg, int ed)
{
    bds[bg].dist = 0;
    
    priority_queue<pii> pq;
    
    pq.push({-0, bg});
    
    while (!pq.empty())
    {
        pii tp = pq.top();
        pq.pop();
        
        Bd &cur = bds[tp.second];
        if (cur.was)
        continue;
        cur.was = 1;
        
        rep(i, 0, cur.edges.size())
        {
            int to = cur.edges[i].first;
            int dist = cur.edges[i].second;
            
            if (cur.dist + dist < bds[to].dist)
            {
                bds[to].dist = cur.dist + dist;
                pq.push({-bds[to].dist, to});
            }
        }
    }
}

void test(int tIndex)
{
    printf("Case #%d: ", tIndex);
    
    int w, h, b;
    scanf("%d%d%d", &w, &h, &b);
    
    bds[0] = Bd(0, 0, 0, h);
    bds[b + 1] = Bd(w, 0, w, h);
    
    rep(i, 0, b)
    {
        int cx1, cy1, cx2, cy2;
        scanf("%d%d%d%d", &cx1, &cy1, &cx2, &cy2);
        cx2++, cy2++;
        
        bds[i+1] = Bd(cx1, cy1, cx2, cy2);
    }
    
    rep(i, 0, b+2)
    {
        rep(j, 0, i)
        {
            Bd b1 = bds[j], b2 = bds[i];
                int dst = getDist(b1, b2);
//            printf("%d %d %d\n", i, j, dst);
                bds[j].edges.push_back({i, dst});
                bds[i].edges.push_back({j, dst});
        }
    }
    dijkstra(0, b+1);
    
    int res = bds[b+1].dist;
    printf("%d\n", res);
    fprintf(stderr, "%d", tIndex);
}

void run()
{
	int T, t;
	scanf("%d", &T);
	for(t = 0; t < T; ++t)
	{
		test(t + 1);
	}
}

//#define prob "settling"


int main()
{
#ifdef LOCAL_DEBUG
    freopen("test.in","r",stdin);
    freopen("test.out","w",stdout);
    time_t st=clock();
#else
#ifdef prob
    freopen(prob".in","r",stdin);
    freopen(prob".out","w",stdout);
#endif
#endif
    run();
#ifdef LOCAL_DEBUG
    fprintf(stderr,  "\n=============\n");
    fprintf(stderr, "Time: %.2lf sec\n",(clock()-st)/double(CLOCKS_PER_SEC));
#endif
    
    return 0;
}