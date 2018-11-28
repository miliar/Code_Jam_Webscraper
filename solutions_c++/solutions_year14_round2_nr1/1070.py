#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <vector>
#include <algorithm>
#include <string>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <climits>
#include <sstream>
#include <functional>
#include <complex>

using namespace std;

#define len(array)  (sizeof (array) / sizeof *(array))
#define rep(i, s, e) for(int i = (s);i < (e);i++)
#define Rep(i, e) for(int i = 0;i < (e);i++)
#define rrep(i, e, s) for(int i = (e);(s) <= i;i--)
#define Rrep(i, e) for(int i = e;0 <= i;i--)
#define mrep(i, e, t1, t2) for(map<t1, t2>::iterator i = e.begin(); i != e.end(); i++)
#define vrange(v) v.begin(), v.end()
#define vrrange(v) v.rbegin(), v.rend()
#define vsort(v) sort(vrange(v))
#define vrsort(v) sort(vrrange(v))
#define arange(a) a, a + len(a)
#define asort(a) sort(arange(a))
#define arsort(a, t) sort(arange(a), greater<t>())
#define afill(a, v) fill(arange(a), v)
#define afill2(a, v, t) fill((t *)(a), (t *)((a) + len(a)), v)
#define fmax(a, b) ((a) < (b)? (b) : (a))
#define fmin(a, b) ((a) > (b)? (b) : (a))
#define fabs(a) ((a) < 0? -(a) : (a))
#define pb push_back
#define fst(e) (e).first
#define snd(e) (e).second
#define rg(e, s, t) (s <= e && e < t)
#define PQDecl(name, tp) priority_queue< tp, vector<tp>, greater<tp> > name
#define dq(q) q.top();q.pop();
#define sz(v) ((int)(v).size())
#define lg(s) ((int)(s).length())
//#define X real()
//#define Y imag()
//typedef unsigned int ui;
typedef long long ll;
typedef unsigned long long ull;
typedef pair<int, int> P;
typedef pair<ll, ll> PL;
//typedef complex<double> p;
const int INF = (int)2e9;
const int MOD = (int)1e9 + 7;
const double EPS = 1e-10;
//const int dx[] = {1, -1, 0, 0, 1, -1, -1, 1};
//const int dy[] = {0, 0, 1, -1, -1, -1, 1, 1};
//const ll weight[] = {1e0,1e1,1e2,1e3,1e4,1e5,1e6,1e7,1e8,1e9,1e10,1e11,1e12,1e13};
typedef struct _Datum {
  int fst,snd,trd;
  _Datum(int arg1 = 0, int arg2 = 0 , int arg3 = 0) {
	fst = arg1; snd = arg2; trd = arg3;
  }
  bool operator <(const struct _Datum &e) const{
    return fst == e.fst? (snd == e.snd? trd < e.trd : snd < e.snd) : fst < e.fst;
  }
  bool operator >(const struct _Datum &e) const{
    return fst == e.fst? (snd == e.snd? trd > e.trd : snd > e.snd) : fst > e.fst;
  }
}datum;


#define MAX_N 100005
int p;
string shrink(string s){
    string ret = "";
    char prev = 'A';
    Rep(i, s.length()){
        if(s[i] != prev){
            prev = s[i];
            ret += s[i];
        }
    }
    return ret;
}
void solve(){
    int n;
    string s[105];
    cin >> n;
    Rep(i, n){
        cin >> s[i];
    }
    string ss = shrink(s[0]);
    int kind = ss.length();
    rep(i, 1, n){
        string tt = shrink(s[i]);
        if(ss != tt){
            printf("Case #%d: Fegla Won\n", p);
            return;
        }
    }
    int freq[105][105]; //[i番目の文字列][i番目の文字]
    afill2(freq, 0, int);
    Rep(i, n){
        char prev = 'A';
        int p = -1;
        Rep(j, s[i].length()){
            if(prev != s[i][j]){
                p++;
                prev = s[i][j];
            }
            freq[i][p]++;
        }
    }
    ll ans = 0, _move, _minimum = INF;; //[i番目の文字]

    Rep(i, kind){ //i番目の文字
        _minimum = INF;
        Rep(j, 102){ //基準
            _move = 0;
            Rep(k, n){ //k番目のs
                _move += abs(j - freq[k][i]);
            }
            // printf("move = %lld, mini = %lld\n", _move, _minimum);
            _minimum = min(_move, _minimum);
        }
        ans += _minimum;
    }
    printf("Case #%d: %lld\n", p, ans);
}

void doIt(){
  int t = 1;
  scanf("%d", &t);
  while(t--){
      p++;
    solve();
  }
}

int main() {
  doIt();
  return 0;
}
