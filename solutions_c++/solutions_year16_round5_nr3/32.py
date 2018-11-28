#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <ctype.h>
#include <deque>
#include <queue>
#include <cstring>
#include <set>
#include <list>
#include <map>
#include <unordered_map>
#include <stdio.h>

using namespace std;

typedef long long ll;
typedef std::vector<int> vi;
typedef std::vector<bool> vb;
typedef std::vector<string> vs;
typedef std::vector<double> vd;
typedef std::vector<long long> vll;
typedef std::vector<std::vector<int> > vvi;
typedef vector<vvi> vvvi;
typedef vector<vll> vvll;
typedef std::vector<std::pair<int, int> > vpi;
typedef vector<vpi> vvpi;
typedef std::pair<int, int> pi;
typedef std::pair<ll, ll> pll;
typedef std::vector<pll> vpll;

const long long mod = 1000000007;

#define all(c) (c).begin(),(c).end()
#define sz(c) (int)(c).size()
#define forn(i, a, b) for(int i = a; i < b; i++)

#define pb push_back
#define mp make_pair

struct Point {
    double x,y,z;
};
typedef vector<Point> vp;
int n,s;
vp p;
vp v;

int MAXN = 2001000;
vi parent(MAXN);
vi rnk(MAXN);

void make_set (int v) {
    parent[v] = v;
    rnk[v] = 0;
}

int find_set (int v) {
    if (v == parent[v])
        return v;
    return parent[v] = find_set (parent[v]);
}

void union_sets (int a, int b) {
    a = find_set (a);
    b = find_set (b);
    if (a != b) {
        if (rnk[a] < rnk[b])
            swap (a, b);
        parent[b] = a;
        if (rnk[a] == rnk[b])
            ++rnk[a];
    }
}

void fillinter(vector<vector<pair<double, double>>> & inter) {
    inter.resize(n);
    forn(i,0,n) inter[i].resize(n);
}

double dist(Point a, Point b) {
    double x = a.x-b.x;
    double y = a.y-b.y;
    double z = a.z-b.z;
    return sqrt(x*x+y*y+z*z);
}

bool check(double d) {
//    vector<vector<pair<double, int>>> e(n);
//    vector<vector<pair<double, double>>> inter;
//    fillinter(inter);
//    int cur = 1;
//    forn(i,0,n) {
//        forn(j,i,n) {
//            e[i].pb(mp(inter[i][j].first, cur));
//            make_set(2*i*n+j);
//            cur++;
//            e[i].pb(mp(inter[i][j].second, cur));
//            make_set(2*i*n+j+1);
//            cur++;
//            e[j].pb(mp(inter[i][j].first, cur));
//            make_set(2*j*n+i);
//            cur++;
//            e[j].pb(mp(inter[i][j].second, cur));
//            make_set(2*j*n+i+1);
//            cur++;
//        }
//    }
    forn(i,0,n) {
        make_set(i);
    }
    forn(i,0,n) forn(j,0,n) {
        if(dist(p[i], p[j]) <= d) union_sets(i, j);
    }
    if(find_set(0)==find_set(1)) return true;
    else return false;
}

int main()
{
#ifndef ONLINE_JUDGE
    freopen("input.txt", "rt", stdin);
    freopen("output.txt", "wt", stdout);
#endif
    int T;
    cin>>T;
    forn(caseNum, 1, T + 1) {
        cout<<"Case #"<<caseNum<<": ";
        
        cin >>n>>s;
        p.resize(n);
        v.resize(n);
        forn(i,0,n) {
            cin >> p[i].x >> p[i].y >> p[i].z;
            cin >> v[i].x >> v[i].y >> v[i].z;
        }
        double l = 0;
        double r = 3000;
        while(r-l > 0.000001) {
            double m = (l+r)/2;
            if(check(m)) r = m;
            else l = m;
        }
        printf("%.10lf\n", r);
    }
    
}


