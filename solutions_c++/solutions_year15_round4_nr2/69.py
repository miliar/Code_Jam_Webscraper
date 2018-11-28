#include <iostream>
#include <complex>
#include <vector>
#define X real()
#define Y imag()
using namespace std;
typedef long double lld;
lld eps=1e-8;
typedef complex<lld> point;
point read_point(){
  lld x, y;
  cin>>x>>y;
  return point(x, y);
}
int n;
point q;
point p[100];
bool comp(const point& p, const point& q){
  return p.Y<q.Y;
}
point combine(const point& p, const point& q){
  return point(p.X+q.X, (p.X*p.Y+q.X*q.Y)/(p.X+q.X));
}
point decombine(const point& p, const point& q){
  return point(p.X-q.X, (p.X*p.Y-q.X*q.Y)/(p.X-q.X));
}
int main(){
  cout<<fixed;
  cout.precision(9);
  int tnum;cin>>tnum;
  int tcou=0;
  while (tnum--){
    cin>>n;
    q = read_point();
    lld min_t=200.0, max_t=-100.0;
    for (int i=0;i<n;++i){
      p[i] = read_point();
      min_t = min(min_t, p[i].Y);
      max_t = max(max_t, p[i].Y);
    }
    if (q.Y<min_t-eps || q.Y>max_t+eps){
      cout<<"Case #"<<++tcou<<": IMPOSSIBLE"<<endl;
      continue;
    }
    sort(p, p+n, comp);
    vector<point> pp;
    for (int i=0;i<n;++i){
      point u(0., p[i].Y);
      int j=i;
      while (j<n && p[j].Y<p[i].Y+eps){
        u = point(u.X+p[j].X, u.Y);
        ++j;
      }
      pp.push_back(u);
      i = j-1;
    }
    n = pp.size();
    for (int i=0;i<n;++i)
      p[i] = pp[i];
    bool found = false;
    point f(0., 0.);
    point r(0., 0.);
    for (int i=0;i<n;++i){
      point next_r = combine(p[i], r);
      if (next_r.Y<q.Y-eps){
        r = next_r;
        continue;
      }
      lld l=0., u=1.;
      if (i==0)
        l = 1.;
      for (int j=0;j<200;++j){
        lld mid = (l+u)/2.;
        if (combine(point(p[i].X*mid, p[i].Y), r).Y<q.Y)
          l = mid;
        else
          u = mid;
      }
      f=combine(point(p[i].X*l, p[i].Y), r);
      found = true;
      break;
    }
    if (!found){
      for (int i=0;i+1<n;++i){
        if (i+2<n){
          point next_r = decombine(r, p[i]);
          if (next_r.Y<q.Y-eps){
            r = next_r;
            continue;
          }
        }
        lld l=0., u=1.;
        for (int j=0;j<200;++j){
          lld mid = (l+u)/2.;
          if (decombine(r, point(p[i].X*mid, p[i].Y)).Y<q.Y)
            l = mid;
          else
            u = mid;
        }
        f = decombine(r, point(p[i].X*l, p[i].Y));
        found = true;
        break;
      }
    }
    lld ans = q.X/f.X;
    cout<<"Case #"<<++tcou<<": "<<ans<<endl;
  }
  return 0;
}
