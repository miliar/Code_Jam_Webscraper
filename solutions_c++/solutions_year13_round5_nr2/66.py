#include <iostream>
#include <fstream>
#include <cstdio>
#include <sstream>
#include <string>
#include <cmath>
#include <stack>
#include <list>
#include <queue>
#include <deque>
#include <set>
#include <map>
#include <vector>
#include <algorithm>
#include <numeric>
#include <utility>
#include <functional>
#include <iomanip>
#include <cstring>
using namespace std;

typedef long long ll;
typedef unsigned long long ull;
#define SZ size()
#define PB push_back
#define SORT(a) sort((a).begin(), (a).end())
#define REV(a) reverse((a).begin(), (a).end())
#define FOR(i, a, b) for(int i = (a); i < (b); i++)
#define TR(i, a) for(typeof(a.begin()) i = a.begin(); i != a.end(); i++)
#define DEBUG(a) cout << #a << ": " << (a) << endl;
#define DEBUG1D(a, x1, x2) { cout << #a << ":"; for(int _i = (x1); _i < (x2); _i++){ cout << " " << a[_i]; } cout << endl; }
#define DEBUG2D(a, x1, x2, y1, y2) { cout << #a << ":" << endl; for(int _i = (x1); _i < (x2); _i++){ for(int _j = (y1); _j < (y2); _j++){ cout << (_j > y1 ? " " : "") << a[_i][_j]; } cout << endl; } }

#define CROSS(x1, y1, x2, y2) ((x1) * (y2) - (y1) * (x2))
#define CROSS2(x1, y1, x2, y2, x0, y0) (((x1) - (x0)) * ((y2) - (y0)) - ((y1) - (y0)) * ((x2) - (x0)))
#define EUCL(x1, y1, x2, y2) (((x1) - (x2)) * ((x1) - (x2)) + ((y1) - (y2)) * ((y1) - (y2)))


struct vertex
{
    int x, y;

    vertex(int _x = 0, int _y = 0)
    {
        x = _x;
        y = _y;
    }

    vertex operator=(const vertex& v)
    {
        x = v.x;
        y = v.y;
    }

    bool operator==(const vertex& v) const
    {
        return (x == v.x && y == v.y);
    }
};


struct edge
{
    vertex a, b;

    edge(vertex _a, vertex _b)
    {
        a = _a;
        b = _b;
    }

    bool operator==(const edge& e)
    {
        return (a == e.a && b == e.b) || (a == e.b && b == e.a);
    }

    bool intersect(edge &e)
    {
        // non-intersecting rectangles
        if(max(a.x , b.x) < min(e.a.x , e.b.x)){
            return 0;
        }
        if(min(a.x , b.x) > max(e.a.x , e.b.x)){
            return 0;
        }
        if(max(a.y , b.y) < min(e.a.y , e.b.y)){
            return 0;
        }
        if(min(a.y , b.y) > max(e.a.y , e.b.y)){
            return 0;
        }

        int det = (b.x - a.x) * (e.b.y - e.a.y) - (e.b.x - e.a.x) * (b.y - a.y);
        int area1 = (e.a.x - a.x) * (e.b.y - a.y) - (e.b.x - a.x) * (e.a.y - a.y);

        // parallel
        if(det == 0){

            // not on the same line
            if(area1 != 0){
                return 0;
            }

            // on the same line, not vertical
            if(a.x != b.x){
                int px1 = min(a.x , b.x), px2 = max(a.x ,b.x), qx1 = min(e.a.x , e.b.x), qx2 = max(e.a.x , e.b.x);
                if(px1 <= qx1 && qx1 < px2){
                    return 1;
                }
                if(px1 < qx2 && qx2 <= px2){
                    return 1;
                }
                if(qx1 <= px1 && px1 < qx2){
                    return 1;
                }
                if(qx1 < px2 && px2 <= qx2){
                    return 1;
                }
            }

            // on the same line, vertical
            else{
                int py1 = min(a.y , b.y), py2 = max(a.y ,b.y), qy1 = min(e.a.y ,e.b.y), qy2 = max(e.a.y ,e.b.y);
                if(py1 <= qy1 && qy1 < py2){
                    return 1;
                }
                if(py1 < qy2 && qy2 <= py2){
                    return 1;
                }
                if(qy1 <= py1 && py1 < qy2){
                    return 1;
                }
                if(qy1 < py2 && py2 <= qy2){
                    return 1;
                }
            }

            return 0;
        }

        // common vertex, not parallel edges -> do not intersect
        if(a == e.a || a == e.b || b == e.a || b == e.b){
            return 0;
        }

        int area2 = (e.b.x - b.x) * (e.a.y - b.y) - (e.a.x - b.x) * (e.b.y - b.y);
        int area3 = (a.x - e.a.x) * (b.y - e.a.y) - (b.x - e.a.x) * (a.y - e.a.y);
        int area4 = (b.x - e.b.x) * (a.y - e.b.y) - (a.x - e.b.x) * (b.y - e.b.y);

        area1 /= (area1 != 0 ? abs(area1) : 1);
        area2 /= (area2 != 0 ? abs(area2) : 1);
        area3 /= (area3 != 0 ? abs(area3) : 1);
        area4 /= (area4 != 0 ? abs(area4) : 1);

        // segments intersect iff for each segment the line described by it intersects with the other segment
        return (area1 * area2 >= 0 && area3 * area4 >= 0);
    }
};





ll xb, yb;

struct point
{
    ll x, y;
    bool operator<(const point& p) const
    {
        ll a = CROSS2(x, y, p.x, p.y, xb, yb);
        if(a > 0) return true;
        //return false;
        if(a < 0) return false;
        return EUCL(x, y, xb, yb) < EUCL(p.x, p.y, xb, yb);
    }
};

ll area(vector< pair<ll, ll> > poly)
{
    ll a = 0;
    FOR(i, 0, poly.SZ)
    {
        a += CROSS(poly[i].first, poly[i].second, poly[(i + 1) % poly.SZ].first, poly[(i + 1) % poly.SZ].second);
    }
    return a;
}

int n;
point P[55555];
int ans[55555];

void solve()
{
    map< pair<ll, ll>, int > ptoind;
    FOR(i, 0, n) ptoind[make_pair(P[i].x, P[i].y)] = i;

    vector< pair<ll, ll> > polyRes;

    xb = P[0].x;
    yb = P[0].y;
    int ind = 0;
    FOR(i, 1, n)
    {
        if(yb > P[i].y or (yb == P[i].y and xb > P[i].x))
        {
            xb = P[i].x;
            yb = P[i].y;
            ind = i;
        }
    }
    swap(P[0], P[ind]);
    sort(P + 1, P + n);

    //cout << "P: "; FOR(i, 0, n) printf("(%lld, %lld) ", P[i].x, P[i].y); cout << endl;

    int H[55555], top = 1;
    H[0] = 0;
    H[1] = 1;
    FOR(i, 2, n)
    {
        ll a = CROSS2(P[H[top]].x, P[H[top]].y, P[i].x, P[i].y, P[H[top - 1]].x, P[H[top - 1]].y);
        while(top > 1 and a < 0)
        {
            top--;
            a = CROSS2(P[H[top]].x, P[H[top]].y, P[i].x, P[i].y, P[H[top - 1]].x, P[H[top - 1]].y);
        }
        H[++top] = i;
    }
    int ii = H[top] - 1;
    while(ii > 1 and CROSS2(P[H[top]].x, P[H[top]].y, P[ii].x, P[ii].y, P[H[0]].x, P[H[0]].y) == 0)
    {
        H[++top] = ii;
        ii--;
    }

    //cout << "H: "; FOR(i, 0, top + 1)printf("(%lld, %lld) ", P[H[i]].x, P[H[i]].y); cout << endl;

    if(top + 1 == n)
    {
        FOR(i, 0, top + 1)
        {
            polyRes.PB(make_pair(P[H[i]].x, P[H[i]].y));
        }
    }
    else
    {

        set<int> inHull;
        FOR(i, 0, top + 1) inHull.insert(H[i]);
        vector< pair<ll, ll> > middle;
        FOR(i, 0, n) if(inHull.find(i) == inHull.end()) middle.PB(make_pair(P[i].y, P[i].x));
        sort(middle.begin(), middle.end());

        int upper = 0;
        FOR(i, 1, top + 1)
        {
            if(P[H[i]].y > P[H[upper]].y) upper = i;
        }

        vector< pair<ll, ll> > polyL, polyR;
        FOR(i, 0, upper + 1)
        {
            polyR.PB(make_pair(P[H[i]].x, P[H[i]].y));
        }
        for(int i = middle.SZ - 1; i >= 0; i--) polyR.PB(make_pair(middle[i].second, middle[i].first));
        FOR(i, 0, middle.SZ) polyL.PB(make_pair(middle[i].second, middle[i].first));
        FOR(i, upper, top + 1)
        {
            polyL.PB(make_pair(P[H[i]].x, P[H[i]].y));
        }
        polyL.PB(make_pair(P[H[0]].x, P[H[0]].y));

        ll aL = area(polyL), aR = area(polyR);


        //cout << "L: "; FOR(i, 0, polyL.SZ) printf("(%lld, %lld) ", polyL[i].first, polyL[i].second); cout << endl;
        //cout << "R: "; FOR(i, 0, polyR.SZ) printf("(%lld, %lld) ", polyR[i].first, polyR[i].second); cout << endl;

        //cout << aL << " " << aR << endl;


        if(aR < aL)
        {
            FOR(i, 1, upper)
            {
                middle.PB(make_pair(P[H[i]].y, P[H[i]].x));
            }
            sort(middle.begin(), middle.end());

            FOR(i, 0, middle.SZ) polyRes.PB(make_pair(middle[i].second, middle[i].first));
            FOR(i, upper, top + 1)
            {
                polyRes.PB(make_pair(P[H[i]].x, P[H[i]].y));
            }
            polyRes.PB(make_pair(P[H[0]].x, P[H[0]].y));
        }
        else
        {
            FOR(i, upper + 1, top + 1)
            {
                middle.PB(make_pair(P[H[i]].y, P[H[i]].x));
            }
            sort(middle.begin(), middle.end());

            FOR(i, 0, upper + 1)
            {
                polyRes.PB(make_pair(P[H[i]].x, P[H[i]].y));
            }
            for(int i = middle.SZ - 1; i >= 0; i--) polyRes.PB(make_pair(middle[i].second, middle[i].first));
        }

    }

    //cout << "Res: "; FOR(i, 0, polyRes.SZ) printf("(%lld, %lld) ", polyRes[i].first, polyRes[i].second); cout << endl;

    memset(ans, 0, sizeof(ans));
    FOR(i, 0, polyRes.SZ)
    {
        ans[i] = ptoind[polyRes[i]];
    }
};

point P2[55555];
bool check()
{
    bool has[55555];
    memset(has, 0, sizeof(has));
    FOR(i, 0, n)
    {
        if(has[ans[i]]) return false;
        has[ans[i]] = 1;
    }


    FOR(i, 0, n - 1) FOR(j, i + 2, n)
    {
        if(i == 0 and j == n - 1) continue;
        ll p1x = P2[ans[i]].x, p1y = P2[ans[i]].y;
        ll q1x = P2[ans[i + 1]].x, q1y = P2[ans[i + 1]].y;
        ll p2x = P2[ans[j]].x, p2y = P2[ans[j]].y;
        ll q2x = P2[ans[(j + 1) % n]].x, q2y = P2[ans[(j + 1) % n]].y;

        vertex p1 = vertex(p1x, p1y);
        vertex q1 = vertex(q1x, q1y);
        vertex p2 = vertex(p2x, p2y);
        vertex q2 = vertex(q2x, q2y);

        edge e1 = edge(p1, q1);
        edge e2 = edge(p2, q2);

        if(e1.intersect((e2))) return false;
    }



    vector< pair<ll, ll> > poly1;
    FOR(i, 0, n) poly1.PB(make_pair(P2[ans[i]].x, P2[ans[i]].y));

    vector< pair<ll, ll> > poly2;
    int H[55555], top = 1;
    H[0] = 0;
    H[1] = 1;
    FOR(i, 2, n)
    {
        ll a = CROSS2(P[H[top]].x, P[H[top]].y, P[i].x, P[i].y, P[H[top - 1]].x, P[H[top - 1]].y);
        while(top > 1 and a < 0)
        {
            top--;
            a = CROSS2(P[H[top]].x, P[H[top]].y, P[i].x, P[i].y, P[H[top - 1]].x, P[H[top - 1]].y);
        }
        H[++top] = i;
    }
    FOR(i, 0, top + 1) poly2.PB(make_pair(P[H[i]].x, P[H[i]].y));

    ll a1 = area(poly1);
    ll a2 = area(poly2);

    if(a1 * 2 <= a2) return false;

    return true;
}

int main()
{
    freopen("Blarge.in", "r", stdin);
    freopen("Blarge.out", "w", stdout);
    int testCnt;
    cin >> testCnt;
    FOR(testNo, 1, testCnt + 1)
    {
        cin >> n;
        FOR(i, 0, n)
        {
            cin >> P[i].x >> P[i].y;
            P2[i].x = P[i].x;
            P2[i].y = P[i].y;
        }
        solve();
        cout << "Case #" << testNo << ":";
        FOR(i, 0, n) cout << " " << ans[i];
        cout << endl;
        /*
        if(!check())
        {
            cout << "BAD" << endl;
            FOR(i, 0, n) cout << P2[i].x << " " << P2[i].y << endl;
            break;
        }
        */
    }
}



