#include <iostream>
#include <cstdio>
#include <cstring>
#include <vector>
#include <algorithm>
#include <set>
#include <cassert>

using namespace std;

#define forn(i,n) for(int i=0;i<(int)(n);i++)
#define forsn(i,s,n) for(int i=(s);i<(int)(n);i++)

#define forall(it,c) for(typeof((c).begin()) it = (c).begin(); it != (c).end(); it++

typedef long long tint;

const tint INF = 1000000000000000000LL;

tint intDist(tint a1, tint a2, tint b1, tint b2)
{
    tint r1 = max(a1, b1);
    tint r2 = min(a2, b2);
    if (r1 <= r2) return 0;
    return r1 - r2;
}

struct Building
{
    tint x1,y1,x2,y2;
    
    tint dist(const Building &o) const
    {
        return max(intDist(x1, x2, o.x1, o.x2), intDist(y1, y2, o.y1, o.y2));
    }
};

int main()
{
    int TT; scanf("%d", &TT);
    forn(tt,TT)
    {
        tint W,H,B; cin >> W >> H >> B;
        vector<Building> v;
        forn(i,B)
        {
            Building b; cin >> b.x1 >> b.y1 >> b.x2 >> b.y2;
            b.x2++; b.y2++;
            v.push_back(b);
        }
        Building LEFT; LEFT.x1 = -1; LEFT.x2 = 0; LEFT.y1 = 0; LEFT.y2 = H;
        Building RIGHT; RIGHT.x1 = W; RIGHT.x2 = W+1; RIGHT.y1 = 0; RIGHT.y2 = H;
        int startIndex = v.size(); v.push_back(LEFT); 
        int endIndex = v.size(); v.push_back(RIGHT);
        // Dijkstra
        vector<tint> distance(v.size(), INF);
        vector<bool> used(v.size(), false);
        distance[startIndex] = 0;
        forn(steps, v.size())
        {
            int best = -1;
            forn(i, v.size())
            if ((!used[i]) && (best == -1 || distance[i] < distance[best]))
                best = i;
            assert(best >= 0);
            used[best] = true;
            forn(j, v.size())
            {
                tint newDist = distance[best] + v[best].dist(v[j]);
                if (newDist < distance[j])
                    distance[j] = newDist;
            }
        }
        printf("Case #%d: %lld\n" , tt+1, distance[endIndex]);
    }
    return 0;
}

