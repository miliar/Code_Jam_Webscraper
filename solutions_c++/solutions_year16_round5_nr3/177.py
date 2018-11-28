#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <fstream>
#include <numeric>
#include <iomanip>
#include <bitset>
#include <list>
#include <stdexcept>
#include <functional>
#include <utility>
#include <ctime>
using namespace std;

typedef long long LL;
#define rep(it,s) for(__typeof((s).begin()) it=(s).begin();it!=(s).end();it++)

const double INF = 1.0e10;
const double eps = 1.0e-8;

class Point {
public:
    double x, y, z;
    Point(int _x, int _y, int _z) {
        x = _x;
        y = _y;
        z = _z;
    }
    Point() {}
};

Point v[1010];

double dist[1010];
set<pair<double, int> > q;
int n, s;

double calc(int i, int j) {

    double a = v[i].x - v[j].x;
    double b = v[i].y - v[j].y;
    double c = v[i].z - v[j].z;

    return sqrt(a*a + b*b + c*c);

}

int main() {

    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);

    int tt;
    cin>>tt;
    for (int cas=1; cas<=tt; cas++) {
        cin>>n>>s;
        //n = 1000;
        for (int i=0; i<n; i++) {
            int x, y, z, vx, vy, vz;
            scanf("%d%d%d%d%d%d", &x, &y, &z, &vx, &vy, &vz);
            //x = rand()%1000 - 500;
            //y = rand()%1000 - 500;
            //z = rand()%1000 - 500;
            v[i] = Point(x, y, z);
        }

        for (int i=0; i<n; i++) dist[i] = -1.0;
        dist[0] = 0;

        q.clear();

        q.insert(make_pair(0,0));

        set<pair<double, int> >::iterator it;
        while (!q.empty()) {

            int p = q.begin()->second;
            double tmp = q.begin()->first;

            //cout<<p<<" "<<tmp<<" "<<dist[p]<<endl;

            if (tmp > dist[p] + eps) {
                q.erase(q.begin());
                continue;
            }

            if (p == 1) {
                break;
            }

            q.erase(q.begin());

            //cout<<p<<" "<<tmp<<" "<<dist[p]<<endl;

            for (int i=0; i<n; i++) if (i!=p) {

                double d = calc(p, i);
                if (dist[i] < -0.5) {
                    //cout<<i<<endl;
                    dist[i] = d;
                    q.insert(make_pair(dist[i], i));
                }
                if (max(d, dist[p]) < dist[i] - eps) {

                    it = q.lower_bound(make_pair(i, -1.0));
                    if (it!=q.end() && it->second==i) {
                        q.erase(it);
                    }
                    dist[i] = max(d, dist[p]);
                    q.insert(make_pair(dist[i], i));
                }

            }

        }

        printf("Case #%d: %.12f\n", cas, dist[1]);
    }

    return 0;

}
