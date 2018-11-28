#include <bits/stdc++.h>

#define FO(i,a,b) for (int i = (a); i < (b); i++)
#define sz(v) int(v.size())

using namespace std;

double sq(double a) {
    return a*a;
}

struct ln {
    double x, y, z;
    double vx, vy, vz;

    double ev(double t) {
        double xx = x + t*vx;
        double yy = y + t*vy;
        double zz = z + t*vz;
        return sq(xx)+sq(yy)+sq(zz);
    }
};

double d;

pair<double,double> is(ln a, ln b) {
    b.x -= a.x; b.y -= a.y; b.z -= a.z;
    b.vx -= a.vx; b.vy -= a.vy; b.vz -= a.vz;

    if (sq(b.vx) + sq(b.vy) + sq(b.vz) < 1e-9) {
        if (b.ev(0) <= d*d) {
            return make_pair(-1e18,1e18);
        } else {
            return make_pair(1e18,-1e18);
        }
    }

    double A = sq(b.vx) + sq(b.vy) + sq(b.vz);
    double B = 2 * (b.vx*b.x + b.vy*b.y + b.vz*b.z);
    double c = sq(b.x) + sq(b.y) + sq(b.z) - d*d;
    double D = B*B + (-4.0f)*A*c;

    if (D < 0) {
        return make_pair(1e18,-1e18);
    } else {
        D = sqrt(max(D,0.));
        return make_pair((-0.5)*(B+D)/A, (-0.5)*(B-D)/A);
    }

    //printf("----\n");
    //printf("%lf\n", b.ev(md));
    //printf("%lf\n", b.ev(ss));
    //printf("%lf\n", b.ev(se));
    //printf("----\n");
    //return make_pair(ss,se);
}

int n;
double s;
ln l[1005];
pair<double,double> ed[1005][1005];
double pt[1005];

priority_queue<tuple<double,double,int> > q;

bool can() {
    //printf("-???\n");
    //fflush(stdout);
    FO(i,0,n) FO(j,0,i) {
        pair<double,double> p = is(l[i],l[j]);
        //printf("%d,%d: %lf,%lf\n", i, j, p.first, p.second);
        ed[i][j] = ed[j][i] = p;
    }
    //printf("???\n");
    //fflush(stdout);
    FO(i,0,n) pt[i] = -1;
    while (!q.empty()) q.pop();
    q.emplace(0, s, 0);
    while (!q.empty()) {
        auto tp = q.top(); q.pop();
        double ts, te; int i; tie(ts, te, i) = tp;
        ts *= -1;

        //printf("%lf, %lf, %d\n", ts, te, i);

        if (i == 1) return true;
        ts = max(ts, pt[i]);
        if (ts >= te) continue;
        pt[i] = te;

        FO(j,0,n) if (i != j) {
            double os = max(ts, ed[i][j].first);
            double oe = min(te, ed[i][j].second);
            //printf("%d->%d, %lf %lf\n", i, j, os, oe);
            if (os <= oe) {
                //printf("!%d->%d, %lf %lf\n", i, j, os, ed[i][j].second+s);
                q.emplace(-os, ed[i][j].second+s, j);
            }
        }
    }
    return false;
}

int main() {
    int T; scanf("%d", &T);
    FO(Z,1,T+1) {
        scanf("%d %lf", &n, &s);
        FO(i,0,n) {
            scanf("%lf %lf %lf %lf %lf %lf",
                    &l[i].x, &l[i].y, &l[i].z,
                    &l[i].vx, &l[i].vy, &l[i].vz
                 );
        }
        //d = 2.00001;
        //printf("%d\n", can());
        double st = 0, e = 10000;
        FO(it,0,50) {
            d = (st+e)/2;
            if (can()) {
                e = d;
            } else {
                st = d;
            }
        }
        printf("Case #%d: %.7lf\n", Z, st);
        fflush(stdout);
    }
}

