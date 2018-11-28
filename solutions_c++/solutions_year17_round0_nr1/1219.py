#include <bits/stdc++.h>
using namespace std;
#define pb push_back
#define fi first
#define se second
#define mp make_pair
#define SZ(x) ((int)(x.size()))
#define FOI(i,a,n) for(int (i)=int(a);(i)<=int(n);++(i))
#define FOD(i,a,n) for(int (i)=int(a);(i)>=int(n);--(i))
#define IN(x,y) ((y).find((x))!=(y).end())
#define ALL(t) t.begin(),t.end()
#define MSET(tabl,i) memset(tabl, i, sizeof(tabl))
#define PSET(x,y) fixed<<setprecision(y)<<lf(x)
#define DBG(c) cout << #c << " = " << c << endl;
#define RTIME ((double)clock()/(double)CLOCKS_PER_SEC)

template<typename T,typename S>inline bool REMIN(T&a,const S&b){return a>b?a=b,1:0;}
template<typename T,typename S>inline bool REMAX(T&a,const S&b){return a<b?a=b,1:0;}

typedef long long ll;
typedef long double lf;
typedef pair<int, int> pi;
typedef vector<pi> vpi;
typedef vector<int> vi;
typedef vector<vi> vvi;

int toint(const string &s) { stringstream ss; ss << s; int x; ss >> x; return x; }
string tostring ( int number ){  stringstream ss; ss<< number; return ss.str();}
int bit(ll x, int pos){ return ((1ll<<pos)&x) ? 1 : 0; }

const int INF = 1e9;
const int NMAX = 1e3+5;
const ll MOD = 1000000007;
const lf PI = 2*acos(0);

ll power(ll base, ll exp, ll c = MOD) { if(!exp) return 1; ll r = power(base, exp/2, c); r=(r*r)%c; if(exp&1) r=(r*base)%c; return r; }

int T,N,M;  
int a,b,c;
string s1, s2;

void nope(int dec = 0){
      if(!dec) cout<<"NO";
      exit(0);
}

struct node{
      int lazy = 0;
      int up = 0;
      int down = 0;
};

struct stree{

      node seg[4 * NMAX], empt;

      node combine(node a, node b){
            node c;
            c.lazy = 0;
            c.up = a.up + b.up;
            c.down = a.down + b.down;
            return c;
      }

      void apply(int idx, int v){
            seg[idx].lazy ^= v;
      }

      void down(int idx, int l, int r){
            if(seg[idx].lazy){
                  if(l!=r){
                        apply(idx<<1, seg[idx].lazy);
                        apply((idx<<1)|1, seg[idx].lazy);
                  }
                  seg[idx].lazy = 0;
                  swap(seg[idx].up, seg[idx].down);
            }
      }

      void build(int idx, int begin, int end) {
            if(begin==end) {
                  seg[idx].lazy = seg[idx].up = seg[idx].down = 0;
                  if(s1[begin] == '+') {
                        seg[idx].up = 1;
                  }
                  else
                        seg[idx].down = 1;
            }
            else{
                  int mid=(begin+end)>>1;
                  build(idx<<1, begin, mid);
                  build((idx<<1)+1, mid+1, end);
                  seg[idx]=combine(seg[idx<<1], seg[(idx<<1)+1]);
            }
      }

      void update(int idx, int begin, int end, int l, int r, int v){
            down(idx, begin, end);
            if(r<begin || end<l)
                  return;
            if(l<=begin && end<=r){
                  apply(idx, v);
                  down(idx, begin, end);
            }
            else{
                  int mid=(begin+end)>>1;
                  update(idx<<1, begin, mid, l, r, v);
                  update((idx<<1)|1, mid+1, end, l, r, v);
                  seg[idx]=combine(seg[idx<<1], seg[(idx<<1)|1]);
            }
      }

      node query(int idx, int begin, int end, int l, int r)
      {
            if(r<begin || end<l)
                  return empt;
            down(idx, begin, end);
            if(l<=begin && end<=r) {
                  return seg[idx];
            }
            int mid=(begin+end)>>1;
            return combine(query(idx<<1, begin, mid, l, r),
                                 query((idx<<1)|1, mid+1, end, l, r));
      }
} ST;

int main(){
      ios_base::sync_with_stdio(false); cin.tie(0);
      
      cin >> T;
      FOI(test, 1, T) {
            cin >> s1 >> M;
            N = s1.length();
            ST.build(1, 0, N - 1);
            int cn = 0;
            FOI(i, 0, N - M) {
                  if(ST.query(1, 0, N - 1, i, i).down) {
                        cn ++;
                        ST.update(1, 0, N - 1, i, i + M - 1, 1);
                  }
            }
            if(ST.query(1, 0, N - 1, 0, N - 1).up == N)
                  cout << "Case #" << test << ": " << cn << '\n';
            else
                  cout << "Case #" << test << ": " << "IMPOSSIBLE" << '\n';
      }
      
      return 0;
}

