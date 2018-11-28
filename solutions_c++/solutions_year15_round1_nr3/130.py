#ifdef _WIN32
#  define LL "%I64d"
#else
#  define LL "%Ld"
#endif

#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <ctime>
#include <vector>
#include <deque>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <bitset>
#include <string>
#include <algorithm>
#include <complex>
#include <utility>
#include <cassert>
using namespace std;
#define null NULL
#define mp make_pair
#define pb(a) push_back(a)
#define sz(a) ((int)(a).size())
#define all(a) a.begin() , a.end()
#define fi first
#define se second
#define relaxMin(a , b) (a) = min((a),(b))
#define relaxMax(a , b) (a) = max((a),(b))
#define SQR(a) ((a)*(a))
typedef vector<int> vi;
typedef pair<int,int> pii;
typedef long long ll;
// point type
struct point{
  ll x , y;
  point(ll _x = 0 , ll _y = 0){
   x = _x , y = _y;
                              }
  point operator-(const point& w) const{
   return point(x - w.x , y - w.y);
                                       }
  point operator+(const point& w) const{
   return point(x + w.x , y + w.y);
                                       }
  point perp() const{
   return point(-y , x);
                    }
  bool operator==(const point& w) const{
   return x == w.x && y == w.y;
                                       }
  void out(){
   cout<<"("<<x<<','<<y<<")";
            }
};
ll sgn(ll w){
  return w == 0 ? 0 : (w>0 ? 1 : -1);
}
ll sp(const point& f , const point& s){
  return f.x * s.x + f.y * s.y;
}
ll vp(const point& f , const point& s){
  return f.x * s.y - f.y * s.x;
}

// intersections
bool between(const point& f , const point& s ,
             const point& w){
  if(vp(s-f , w-f) != 0) return false;
  return sp(f-w , s-w) <= 0;
}
bool bbox_1d(ll f1 , ll t1 , ll f2 , ll t2){
  return max(f1 , f2) <= min(t1 , t2);
}
bool bbox_2d(const point& f1 , const point& t1,
             const point& f2 , const point& t2){
  return bbox_1d(f1.x , t1.x , f2.x , t2.x) &&
         bbox_1d(f1.y , t1.y , f2.y , t2.y);
}
bool intersects(const point& f1 , const point& t1,
                const point& f2 , const point& t2){
  if(vp(t1 - f1 , f2 - f1) == 0 &&
     vp(t1 - f1 , t2 - f1) == 0)
   return bbox_2d(f1 , t1 , f2 , t2);
  if(between(f1 , t1 , f2) || between(f1 , t1 , t2))
   return true;
  if(between(f2 , t2 , f1) || between(f2 , t2 , t1))
   return true;
  if(sgn(vp(t1 - f1 , f2 - f1)) *
     sgn(vp(t1 - f1 , t2 - f1)) >= 0) return false;
  if(sgn(vp(t2 - f2 , f1 - f2)) *
     sgn(vp(t2 - f2 , t1 - f2)) >= 0) return false;
  return true;
}

// comparable point
struct pointC : point{
  int kv;
  pointC(ll _x = 0 , ll _y = 0) : point(_x , _y){}
  void set_kv(){ // must be called before <
   if(y > 0 || y == 0 && x >= 0) kv = 0;
   else kv = 1;
               }
  bool operator==(const pointC& w) const{
   return x == w.x && y == w.y;
                                        }
  bool operator<(const pointC& w) const{
   if(kv != w.kv) return kv < w.kv;
   return vp(*this , w) > 0;
                                       }
};
// Solution
int N;
vector<point> in;
int solve(int p){
  vector<pointC> C;
  for(int i=0;i<N;++i)
   if(i != p){
    point U = in[i] - in[p];
    C.pb(pointC(U.x , U.y));
    C.back().set_kv();
             }
  sort(all(C));
  int lo = -1 , hi = 0;
  int IL = 0;
  int take = N-1;
  for(int i=0;i<sz(C);++i){
   ++lo;
   for(;;){
    int nxt = hi + 1;
    if(nxt >= sz(C)) nxt = 0;
    if(nxt == lo) break;
    if(vp(C[lo] , C[nxt]) <= 0) break;
    hi = nxt , ++IL;
          }
   relaxMin(take , IL);
   if(hi == lo)
    hi = (lo+1) % sz(C) , IL = 0;
   else
    --IL;
                          }
  return take;
}
void doit(int CASE = 1){
  scanf("%d" , &N);
  //N = 3000;
  in.resize(N);
  for(int i=0;i<N;++i){
   int x , y;
   scanf("%d%d" , &x , &y);
   //x = rand() , y = rand();
   in[i] = point(x , y);
                      }
  vi ans(N , N-1);
  for(int i=0;i<N;++i)
   ans[i] = solve(i);
  cerr<<"Case "<<CASE<<endl;
  printf("Case #%d:\n" , CASE);
  for(int i=0;i<N;++i)
   printf("%d\n" , ans[i]);
}
int main(){
  int Q;
  scanf("%d" , &Q);
  for(int i=1;i<=Q;++i) doit(i);
  return 0;
}
