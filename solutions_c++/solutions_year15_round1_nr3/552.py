#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <map>
#include <algorithm>
#include <vector>
#include <cstring>
using namespace std;


//Convex Hull : Save the original point set in p
//and after finishing the andrew's monotone chain
//CH will become a convex hull which is what we want
const int MAXP = 110;
struct point{ long long x, y; int idx; };
point p[MAXP], CH[MAXP], totalp[MAXP];
bool ok[MAXP];

long long cross(const point& a, const point& b, const point& c)
{
       return (b.x-a.x)*(c.y-a.y) - (b.y-a.y)*(c.x-a.x); 
}

long long distsq(const point& a, const point& b)
{
    long long dx = a.x-b.x, dy = a.y-b.y;
    return dx*dx+dy*dy;
}

bool cmp(const point& a, const point& b)
{
     return a.x<b.x || (a.x==b.x && a.y<b.y);
}

int main()
{
    int TC;
    scanf("%d", &TC);

    for (int tc = 1; tc <= TC; ++tc) {
        int ans[MAXP];
        int N, MAXMASK; 

        scanf("%d", &N);

        for (int i = 0; i < N; ++i) {
            scanf("%lld%lld", &totalp[i].x, &totalp[i].y);
            totalp[i].idx = i;
            ans[i] = N;
        }

        MAXMASK = 1<<N;
        for (int mask = 0; mask < MAXMASK; ++mask) {
            int cnt = 0, cost = 0;

            for (int i = 0; i < N; i++) {
                int testm = 1<<i;
                if (mask & testm) {
                   p[cnt++] = totalp[i];
                }
            }
            cost = N-cnt;

            //if (cnt <= 2) { //it's not polygon!!!
            //    continue;
            //}

            memset(ok, 0, sizeof(ok));
            sort(p, p+cnt, cmp);     

            //line checking
            bool line = true;

            for (int i = 0; i < cnt; ++i) {
                if (cross(p[0], p[1], p[i]) != 0) {
                    line = false;
                    break;
                }
            }

            if (line) {
                for (int i = 0; i < cnt; ++i) {                        
                    ans[ p[i].idx ] = min(ans[ p[i].idx ], cost);
                }
                continue;
            }

            int m = 0;              
            for (int i = 0; i < cnt; i++) {
                while( m>=2 && cross(CH[m-2], CH[m-1], p[i]) <= 0 ) m--;
                CH[m++] = p[i];
            }
           
            for (int i = cnt-2, t = m+1; i >= 0; i--) {
                while( m>=t && cross(CH[m-2], CH[m-1], p[i]) <= 0 ) m--;
                CH[m++] = p[i];
            }
            --m;

            for (int i = 0; i < m; ++i) {
                ok[CH[i].idx] = true;
            }

            //checking
            for (int i = 0; i < cnt; ++i) {
                if (!ok[p[i].idx]) {
                    for (int j = 0; j < m; ++j) {
                        int f = j, t = (j+1)%m;
                        if (cross(CH[f], CH[t], p[i]) == 0) {
                            if (distsq(CH[f], p[i]) <= distsq(CH[f], CH[t])) {
                                ok[p[i].idx] = true;
                                break;
                            }
                        }
                    }
                }
            }

            for (int i = 0; i < cnt; i++) {
                if(ok[p[i].idx]) {
                    ans[ p[i].idx ] = min(ans[ p[i].idx ], cost);   
                }
            }
        }      

        printf("Case #%d:\n", tc);
        for (int i = 0; i < N; ++i) {
            printf("%d\n", ans[i]);
        }        
    }
    return 0;
}