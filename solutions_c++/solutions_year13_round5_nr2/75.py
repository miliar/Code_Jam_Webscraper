#include <cstdio>
#include <algorithm>
#include <vector>
#include <cmath>

using namespace std;

typedef long long llint;
typedef pair<llint, llint> point;
#define x first
#define y second

const double eps = 1e-9;

bool eq(double x, double y) { return fabs(x-y) < eps; }

llint dist(const point &a, const point &b) {
  return (b.x-a.x)*(b.x-a.x) + (b.y-a.y)*(b.y-a.y);
}

double dis(const point &a, const point &b) {
  return sqrt(dist(a, b));
}

llint dot(const point &a, const point &b, const point &c) {
  return (b.x-a.x)*(c.x-b.x) + (b.y-a.y)*(c.y-b.y);
} 

llint cross(const point &a, const point &b, const point &c) {
  return a.x*(b.y-c.y) + b.x*(c.y-a.y) + c.x*(a.y-b.y);
}

double dst(const point &A, const point &B, const point &C){
  double dist = cross(A,B,C) / dis(A,B);
  llint dot1 = dot(A,B,C);
  if(dot1 > 0)return dis(B,C);
  llint dot2 = dot(B,A,C);
  if(dot2 > 0)return dis(A,C);
  return fabs(dist);
}

int ccw(const point &a, const point &b, const point &c) {
  llint d = a.x*(b.y-c.y) + b.x*(c.y-a.y) + c.x*(a.y-b.y);
  return d < 0 ? -1 : d > 0;
}

point c;

bool cmp( const point &x, const point &y ) {
  int w = ccw( c, x, y );
  if( w ) return w == -1;
  return dist(c, x) <dist(c, y);
}

vector<point> hull(vector<point> &a) {
  int mini = (min_element( a.begin(), a.end() ) - a.begin() );
  swap(a[0], a[mini]);
  c = a[0];
  sort(a.begin()+1, a.end(), cmp);
  
  vector<point> h(a.size());
  
  int m = 0;
  for( int i = 0; i < (int)a.size(); ++i ) {
    while( m > 1 && ccw( h[m-2], h[m-1], a[i] ) >= 0 ) m--;
    h[m++] = a[i];
  }
  h.resize( m );
  return h;
}

llint area(vector<point> h) {
  llint a = 0;
  for( int i = 0; i < (int)h.size(); ++i ) {
    point p = h[(i+1)%h.size()];
    a += h[i].x*p.y - h[i].y*p.x;
  }
  return a < 0 ? -a : a;
}

bool intersect(point &a, point &b, point &c, point &d) {
  int c1 = ccw(a, b, c);
  int c2 = ccw(a, b, d);
  int c3 = ccw(c, d, a);
  int c4 = ccw(c, d, b);
  // printf("%d %d %d %d\n",c1, c2, c3, c4);
  if(c1 == 0 && c2 == 0) {
    double dac = dis(a, c), dbc = dis(b, c);
    double dad = dis(a, d), dbd = dis(b, d);
    if(dac > eps && dbc > eps && eq(dac+dbc, dis(a, b))) return true;
    if(dad > eps && dbd > eps && eq(dad+dbd, dis(a, b))) return true;
    if(dac > eps && dad > eps && eq(dac+dad, dis(c, d))) return true;
    if(dbc > eps && dbd > eps && eq(dbc+dbd, dis(c, d))) return true;
    return false;
  }
  if(c1 != c2) {
    if(c3 && c3 == -c4) return true;
  }
  if(c3 != c4) {
    if(c1 && c1 == -c2) return true;
  }
  return (c1 != 0 && c1 == -c2 && c3 != 0 && c3 == -c4);
}

vector<point> v, h, w;
point a[1000];
int b[1000], bio[1000];
int n;
bool ok;
llint ar;

bool check(vector<point> w) {
  for(int i = 0; i < n; ++i)
    for(int j = i+1; j < n; ++j)
      if(intersect(w[i], w[(i+1)%n], w[j], w[(j+1)%n])) return false;
  return 2*area(w) > ar;
}

int main(void) {
  int t;
  scanf("%d", &t);
  for(int c = 1; c <= t; ++c) {
    scanf("%d", &n);
    v.resize(n);
    for(int i = 0; i < n; ++i) {
      int x, y;
      scanf("%d %d", &x, &y);
      v[i] = make_pair(x, y);
    }
    
    vector<point> vv=v;
    w = hull(vv);
    ar = area(w);

    for(int j = 0; j < n; ++j) {
      bio[j] = 0;
      for(int i = 0; i < w.size(); ++i)
        if(w[i] == v[j]) bio[j] = 1;
    }

    for(int j = 0; j < n; ++j)
      if(!bio[j]) {
        int sz = w.size();
        int best = -1;
        double dd = 1e18;
        
        vector< pair<double, int> >ww;
        for(int i = 0; i < sz; ++i) {
          int k = (i+1)%sz;
          ww.push_back(make_pair(dst(w[i], w[k], v[j]), i));
        }
        sort(ww.begin(), ww.end());
        
        
        for(int p = 0; p < sz; ++p) {
          int i = ww[p].y;
          int k = (i+1)%sz;
          bool ok = true;
          for(int l = 0; l < sz; ++l)
            if(l != i && (intersect(w[l], w[(l+1)%sz], v[j], w[i]) || intersect(w[l], w[(l+1)%sz], v[j], w[k]))) { ok = false; break; }
          if(ok) { best = i; break; }
        }
        if(best == -1) { puts("fail"); break; }
        w.insert(w.begin()+best+1, v[j]);
      }
    
    for(int i = 0; i < n; ++i)
      for(int j = 0; j < n; ++j)
        if(w[i] == v[j]) b[i] = j;
    if(!check(w)) puts("fail");
    printf("Case #%d:", c);
    for(int i = 0; i < n; ++i)
      printf(" %d", b[i]);
    putchar('\n');
  }
  return 0;
}
