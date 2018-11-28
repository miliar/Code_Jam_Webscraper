#include "iostream"
#include "set"

#define fi first
#define se second
#define sqr(x) ((x)*(x))
#define pb(x) push_back(x)
#define sz(x) (int)x.size()
#define all(x) (x).begin(),(x).end()
#define cs(x) printf("Case #%d: ", x)

using namespace std;
typedef long long ll;
typedef pair <int, int> pii;
template <class T> inline void umax(T &x,T y) {if (y > x) x = y;}
template <class T> inline void umin(T &x,T y) {if (y < x) x = y;}

const int N = 2e5 + 5, B = 0x7fffffff;
int t;

int main(){
  freopen("in", "r", stdin);
  freopen("out", "w", stdout);
  scanf("%d", &t);
  for (int tt = 1; tt <= t; tt++){
    int n;
    multiset <pii> s;
    scanf("%d", &n);
    int pq = 0;
    for (int i = 1, x; i <= n; i++){
      scanf("%d", &x);
      s.insert({x, i});
      pq += x;
    }
    cs(tt);
    while (!s.empty()){
      auto fr = (--s.end());
      auto rf = (--s.end());
      if (sz(s) > 1) rf--;
      if (sz(s) > 1 && (*rf).fi == (*fr).fi && (*rf).se != (*fr).se && pq - 2 != 1){
        pq -= 2;
        if (pq != 0) cout << (char)('A' + (*fr).se - 1) << (char)('A' + (*rf).se - 1) << ' ';
        else cout << (char)('A' + (*fr).se - 1) << (char)('A' + (*rf).se - 1);
        if ((*fr).fi == 1){
          s.erase(*fr);
          s.erase(*rf);
        }
        else{
          s.erase(*fr);
          s.insert({(*fr).fi - 1, (*fr).se});
          s.erase(*rf);
          s.insert({(*rf).fi - 1, (*rf).se});
        }
      }
      else{
        pq--;
        if (pq != 0) cout << (char)('A' + (*fr).se - 1) << ' ';
        else  cout << (char)('A' + (*fr).se - 1);
        if ((*fr).fi == 1) s.erase(fr);
        else{
          s.erase(*fr);
          s.insert({(*fr).fi - 1, (*fr).se});
        }
      }
    }
    puts("");
  }
  return !1;
}
