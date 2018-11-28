#include <cstdio>
#include <set>
#include <string>
//#include <algorithm>
#include <vector>

using namespace std;
//--common
#define forr(i,f,t) for (int i = (f); i <= (t); i++)
#define fori(i,t) for (int i = 0; i < (t); i++)
#define forc(i,c) for (int i = 0; i < (c).size(); i++)
#define forit(it,c) for (auto it = (c).begin(), end = (c).end(); it != end; ++it)

template <typename C> void rerase(C& s, const typename C::const_reverse_iterator &it ) { s.erase(s.find(*it)); }
template <typename T> vector<T>& operator<<(vector<T>& v, const T& t) { v.push_back(t); return v; }
template <typename T> set<T>& operator<<(set<T>& v, const T& t) { v.insert(t); return v; }
//--end common


int main(int argc, char *argv[])
{
     int T;
     scanf("%i", &T);
     forr (tt, 1, T) {
          int n;
          double res;
          double v, x;
          double r[200], c[200];
          scanf("%i %lf %lf\n", &n, &v, &x);
          if (v == 0) res = 0;
          else {
          fori(i, n)
                    scanf("%lf %lf\n", &r[i],&c[i]);
          if (n == 1) {
               if (c[0] == x) res = v / r[0];
               else res = -1;
          } else if (c[0] == x) {
               if (c[1] == x) res = v / (r[0] + r[1]);
               else res = v / r[0];
          } else if (c[1] == x) {
               res = v / (r[1]);
          } else {
               double t[200];
               t[0] = v*x / (r[0]*c[0] - r[0]*(c[0] - x) * c[1] / ((c[1]-x)) );
               t[1] = - t[0] * r[0]*(c[0] - x) / (r[1]*(c[1]-x));
               if (t[0] < 0 || t[1] < 0) res = -1;
               else res = max(t[0], t[1]);
               //printf("        ------  %lf %lf\n", t[0], t[1]);
          }
          }

          if (res >= 0) printf("Case #%i: %.10lf\n", tt, res);
          else printf("Case #%i: IMPOSSIBLE\n", tt);


     }
}
