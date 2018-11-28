#include <cstdio>
#include <cassert>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

#define REMOVE_REDUNDANT

typedef double T;
const T EPS = 1e-7;
struct PT {
  T x, y;
  PT() {}
  PT(T x, T y) : x(x), y(y) {}
  bool operator<(const PT &rhs) const { return make_pair(y,x) < make_pair(rhs.y,rhs.x); }
  bool operator==(const PT &rhs) const { return make_pair(y,x) == make_pair(rhs.y,rhs.x); }
  PT operator + (const PT &p)  const { return PT(x+p.x, y+p.y); }
  PT operator - (const PT &p)  const { return PT(x-p.x, y-p.y); }
  PT operator * (double c)     const { return PT(x*c,   y*c  ); }
  PT operator / (double c)     const { return PT(x/c,   y/c  ); }
};

T cross(PT p, PT q) { return p.x*q.y-p.y*q.x; }
T area2(PT a, PT b, PT c) { return cross(a,b) + cross(b,c) + cross(c,a); }

#ifdef REMOVE_REDUNDANT
bool between(const PT &a, const PT &b, const PT &c) {
  return (fabs(area2(a,b,c)) < EPS && (a.x-b.x)*(c.x-b.x) <= 0 && (a.y-b.y)*(c.y-b.y) <= 0);
}
#endif

void ConvexHull(vector<PT> &pts) {
  sort(pts.begin(), pts.end());
  pts.erase(unique(pts.begin(), pts.end()), pts.end());
  vector<PT> up, dn;
  for (int i = 0; i < pts.size(); i++) {
    while (up.size() > 1 && area2(up[up.size()-2], up.back(), pts[i]) >= 0) up.pop_back();
    while (dn.size() > 1 && area2(dn[dn.size()-2], dn.back(), pts[i]) <= 0) dn.pop_back();
    up.push_back(pts[i]);
    dn.push_back(pts[i]);
  }
  pts = dn;
  for (int i = (int) up.size() - 2; i >= 1; i--) pts.push_back(up[i]);

#ifdef REMOVE_REDUNDANT
  if (pts.size() <= 2) return;
  dn.clear();
  dn.push_back(pts[0]);
  dn.push_back(pts[1]);
  for (int i = 2; i < pts.size(); i++) {
    if (between(dn[dn.size()-2], dn[dn.size()-1], pts[i])) dn.pop_back();
    dn.push_back(pts[i]);
  }
  if (dn.size() >= 3 && between(dn.back(), dn[0], dn[1])) {
    dn[0] = dn.back();
    dn.pop_back();
  }
  pts = dn;
#endif
}

double dot(PT p, PT q)     { return p.x*q.x+p.y*q.y; }
double dist2(PT p, PT q)   { return dot(p-q,p-q); }
bool LinesParallel(PT a, PT b, PT c, PT d) {
  return fabs(cross(b-a, c-d)) < EPS;
}
bool LinesCollinear(PT a, PT b, PT c, PT d) {
  return LinesParallel(a, b, c, d)
      && fabs(cross(a-b, a-c)) < EPS
      && fabs(cross(c-d, c-a)) < EPS;
}
bool SegmentsIntersect(PT a, PT b, PT c, PT d) {
  if (LinesCollinear(a, b, c, d)) {
    if (dist2(a, c) < EPS || dist2(a, d) < EPS ||
      dist2(b, c) < EPS || dist2(b, d) < EPS) return true;
    if (dot(c-a, c-b) > 0 && dot(d-a, d-b) > 0 && dot(c-b, d-b) > 0)
      return false;
    return true;
  }
  if (cross(d-a, b-a) * cross(c-a, b-a) > 0) return false;
  if (cross(a-c, d-c) * cross(b-c, d-c) > 0) return false;
  return true;
}
bool SegmentsIntersect2(PT a, PT b, PT c, PT d) {
  if (LinesCollinear(a, b, c, d)) {
    if (dist2(a, c) < EPS || dist2(a, d) < EPS ||
       dist2(b, d) < EPS) return true;
    if (dot(c-a, c-b) > 0 && dot(d-a, d-b) > 0 && dot(c-b, d-b) > 0)
      return false;
    return true;
  }
  if (cross(d-a, b-a) * cross(c-a, b-a) > 0) return false;
  if (cross(a-c, d-c) * cross(b-c, d-c) > 0) return false;
  return true;
}
double computeArea(vector<PT> v){
    double ret=0;
    for(int i=0;i<v.size();i++){
        ret+=cross(v[i],v[(i+1)%v.size()]);
    }
    return ret/2;
}
bool okay(PT  a ,PT b, PT c){
    if(dist2(a,b) < dist2 ( a,c) && dist2 (b,c) < dist2(a,c))return true;
    return false;
}
void solve(){
    int n;
    scanf("%d",&n);
    vector<PT> v;
    for(int i=0;i<n;i++){
        int x,y;
        scanf("%d %d",&x,&y);
        v.push_back(PT(x,y));
    }
    vector<PT> convex = v;
    ConvexHull(convex);
    /*for(int i=0;i<convex.size();i++){
        printf("%lf %lf\n",convex[i].x,convex[i].y);
    }*/
    double cArea=computeArea(convex);
    //printf("cArea = %lf\n",cArea);
    vector<int> perm;
    for(int i=0;i<n;i++)perm.push_back(i);
    do{
        bool ok=true;
        for(int j=1;ok&&j<n;j++){
            for(int k=j-2;ok&&k>=0;k--){
                if(j+1==n&&k==0)continue;
                if(SegmentsIntersect(v[perm[(n+k-1)%n]],v[perm[k]],v[perm[j-1]],v[perm[j]])){
                    if(k==j-1){
                        if(okay(v[perm[(n+k-1)%n]],v[perm[k]],v[perm[j]])){
                            continue;
                        }
                    }
                    ok=false;
                }
            }
        }
        if(ok){
            vector<PT> newOne;
            for(int i=0;i<n;i++){
                newOne.push_back(v[perm[i]]);
            }
            double p=computeArea(newOne);
            //printf("p = %lf\n",p);
            if(p*2>=cArea){
                for(int i=0;i<n;i++)printf("%d%c",perm[i],i+1==n?'\n':' ');
                return;
            }
        }
    }while(next_permutation(perm.begin(),perm.end()));
}
int main(){
    freopen("B-small-attempt1.in","r",stdin);
    freopen("B-small.out","w",stdout);
    int t;
    scanf("%d",&t);
    for(int i=1;i<=t;i++){
        printf("Case #%d: ",i);
        solve();
    }
}
