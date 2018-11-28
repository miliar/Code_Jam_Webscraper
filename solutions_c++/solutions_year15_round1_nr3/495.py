

#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <cassert>

#define rep(i,n) for (int i=0; i<(n); i++)
#define repf(i,a,b) for (int i=(a); i<=(b); i++)
#define repb(i,a,b) for (int i=(a); i>=(b); i--)

#define D(x) cout << #x << " = " << x << endl;
#define endl '\n'

using namespace std;

typedef long long int LL;

template<class T>
ostream& operator<<(ostream& a, const vector<T>& v) {
    a << "{";
    if (v.size()>0) a << v[0];
    for (int i=1; i<v.size(); i++) a << ", " << v[i];
    a << "}";
    return a;
}

/*
 * This is my implementation of Graham Scan taking into acount colinar special cases.
 * The implementation assumes that the given points are unique, and I have tested.
 */

typedef array<double,2> vec;
const double my_inf = 1e100;
const double eps = 1e-8;

vec operator+(const vec& a, const vec& b) {
  vec ans;
  rep(i,2) ans[i] = a[i] + b[i];
  return ans;
}

vec operator-(const vec& a, const vec& b) {
  vec ans;
  rep(i,2) ans[i] = a[i] - b[i];
  return ans;
}

vec operator*(double a, const vec& b) {
  vec ans;
  rep(i,2) ans[i] = a * b[i];
  return ans;
}

vec operator*(const vec& a, double b) {return b*a;}

ostream& operator<<(ostream& a, const vec& v) {
  a << "{" << v[0] << ", " << v[1] << "}";
  return a;
}

double dot(const vec& a, const vec& b) {
  double ans = 0;
  rep(i,2) ans += a[i]*b[i];
  return ans;
}

double norm(const vec& a) {
  return sqrt(dot(a,a));
}

double cross(const vec& a, const vec&b) {
  return a[0]*b[1] - a[1]*b[0];
}

bool db_eq(double a, double b) {
  return fabs(a-b) < eps;
}

bool db_leq(double a, double b) {
  return db_eq(a,b) || (a<b);
}

vector<vec> chull(vector<vec>& pts, bool& ok) {
  vector<vec> ans;
  vec lowerLeft{my_inf, my_inf};
  for (auto& p : pts) {
    vec tmp = p - lowerLeft;
    if ( fabs(tmp[1]) < eps ) {
      if (tmp[0] < 0) lowerLeft = p;
    } else {
      if (tmp[1] < 0) lowerLeft = p;
    }
  }
  auto cmp = [lowerLeft](const vec& a, const vec& b) {
    if ( dot(a - lowerLeft, a - lowerLeft) < eps) return true;
    if ( dot(b - lowerLeft, b - lowerLeft) < eps) return false;
    double cp = cross(a-lowerLeft, b-lowerLeft);
    if (db_eq(cp,0)) {
      double normA = norm(a-lowerLeft), normB = norm(b-lowerLeft);
      return normA > normB;
    }
    if (cp > 0) return true; //less than
    else return false; //greater than
  };
  sort(pts.begin(), pts.end(), cmp);

  ans.push_back(pts[0]);
  ans.push_back(pts[1]);
  for (int i=2; i<pts.size(); i++) {
    int n = ans.size();
    bool insertMe = true;
    while ( true ) {
      double cp = cross(ans[n-1]-ans[n-2], pts[i]-ans[n-1]);
      double dp = dot(ans[n-2]-ans[n-1], pts[i]-ans[n-1]);
      if (db_eq(cp, 0)) {
        if (dp > 0) {insertMe = false; break;}
        else {ans.pop_back(); n--;}
      } else if (cp < 0) {
        ans.pop_back(); 
        n--;
      } else {
        break;
      }
      assert(n>=2);
    }
    if (insertMe) ans.push_back(pts[i]);
  }
  int n = ans.size();
  while ( db_leq(cross(ans[n-1]-ans[n-2], ans[0]-ans[n-1]), 0) ) {
    ans.pop_back(); 
    n--;
    if (n<3) {
      ok = false;
      return pts;
    }
    assert(n>=3);
  }
  ok = true;
  return ans;
}

/** End of library Implementation **/

int bitcnt(int mask) {
  int ans=0;
  while (mask) {
    if (mask & 1) ans++;
    mask >>= 1;
  }
  return ans;
}

int main() {
    cin.sync_with_stdio(false);
    cout.sync_with_stdio(false);
    cin.tie(NULL);
    int TC, N;
    bool ok;
    cin >> TC;
    for (int tc=1; tc<=TC; tc++) {
      cin >> N;
      vector<vec> points(N);
      vector<int> ans(N,1000000);
      rep(i,N) {
        cin >> points[i][0] >> points[i][1];
      }
      for (int bitmask=7; bitmask<(1<<N); bitmask++) {
        if (bitcnt(bitmask) < 3) continue;
        vector<vec> newset;
        for (int i=0; i<N; i++) {
          if ((1<<i) & bitmask) {
            newset.push_back(points[i]);
          }
        }
        if (newset.size() >= 3) {
          newset = chull(newset, ok);
          if (!ok) continue;
        } 
        int inside=0, border=0;
        for (int i=0; i<N; i++) {
          bool is_inside=true, is_border=false;
          for (int j=0; j<newset.size(); j++) {
            vec a = newset[(j+1) % newset.size()] - newset[j];
            vec b = points[i] - newset[j];
            double det = cross(a,b);
            if (db_eq(det,0)) {
              is_border = true;
            } else if (det < 0) {
              is_inside = false;
            }
          }
          if (is_inside) {
            inside |= (1 << i);
            if (is_border) border |= (1 << i);
          }
        }
        int removed = N - bitcnt(inside);
        for (int i=0; i<N; i++) {
          if (border & (1<<i)) {
            ans[i] = min(ans[i], removed);
          }
        }
      }
      cout << "Case #" << tc << ": " << endl;
      for (int i=0; i<N; i++) {
        cout << ( (ans[i]==1000000) ? 0 : ans[i] ) << endl;
      }
    }
}
