#include <cstdio>
#include <cmath>
#include <cstring>
#include <cstdlib>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <queue>
#include <algorithm>
#include <limits>
#include <iostream>
#include <utility>

using namespace std;

#define TRACE(x...) x
#define WATCH(x) TRACE(cout << #x" = " << x << endl)
#define PRINT(x...) TRACE(printf(x); fflush(stdout))

#define gc getchar  //unlocked linux
#define all(v) (v).begin(), (v).end()
#define FU(i, a, b) for(decltype(b) i = (a); i < (b); ++i)
#define fu(i, n) FU(i, 0, n)
#define FD(i, a, b) for (decltype(b) i = (b)-1; i >= a; --i)
#define fd(i, n) FD(i, 0, n)
#define mod(a, b) ((((a)%(b))+(b))%(b))
#define pb push_back
#define sz(c) int((c).size())
#define mk make_pair

const int INF = 0x3F3F3F3F; const int NEGINF = 0xC0C0C0C0;

const double EPS = 1e-8;

typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<double> vd;
typedef long long ll;
typedef vector<ll> vll;
typedef vector<vll> vvll;

int cmp_double(double a, double b, double eps = 1e-9){
  return a + eps > b ? b + eps > a ? 0 : 1 : -1;  //0 = iguais, 1 = a maior
}

inline void scanint(int &x){
  register int c = gc();
  x = 0;
  int neg = 0;
  for(;((c<48 || c>57) && c != '-');c = gc());
  if(c=='-') {neg=1;c=gc();}
  for(;c>47 && c<58;c = gc()) {x = (x<<1) + (x<<3) + c - 48;}
  if(neg) x=-x;
}

int conta(int v, string& s, vi& mark){
  int tam = s.size();
  int cnt = 0;
  if (v == 0){
    for (int i = 0; i < tam; i++){
      if (mark[i]) continue;
      if (s[i] == 'Z') cnt++;
    }
  } else if (v == 2){
    for (int i = 0; i < tam; i++){
      if (mark[i]) continue;
      if (s[i] == 'W') cnt++;
    }
  } else if (v == 4){
    for (int i = 0; i < tam; i++){
      if (mark[i]) continue;
      if (s[i] == 'U') cnt++;
    }
  } else if (v == 6){
    for (int i = 0; i < tam; i++){
      if (mark[i]) continue;
      if (s[i] == 'X') cnt++;
    }
  } else if (v == 1){
    for (int i = 0; i < tam; i++){
      if (mark[i]) continue;
      if (s[i] == 'O') cnt++;
    }
  } else if (v == 3){
    for (int i = 0; i < tam; i++){
      if (mark[i]) continue;
      if (s[i] == 'R') cnt++;
    }
  } else if (v == 8){
    for (int i = 0; i < tam; i++){
      if (mark[i]) continue;
      if (s[i] == 'H') cnt++;
    }
  } else if (v == 7){
    for (int i = 0; i < tam; i++){
      if (mark[i]) continue;
      if (s[i] == 'S') cnt++;
    }
  } else if (v == 5){
    for (int i = 0; i < tam; i++){
      if (mark[i]) continue;
      if (s[i] == 'F') cnt++;
    }
  } else if (v == 9){
    for (int i = 0; i < tam; i++){
      if (mark[i]) continue;
      if (s[i] == 'I') cnt++;
    }
  }
  return cnt;
}

void del_aux(string& s, int cnt, string& aux, vi& mark, int tam){
  map<char, int> m;
  for (auto & x : aux) m[x] = cnt;
  for (int i = 0; i < tam; i++){
    if (mark[i]) continue;
    if (m[s[i]] != 0){
      mark[i] = 1;
      m[s[i]]--;
    }
  }
}

int deleta(int v, string& s, vi& mark, int cnt){
  int tam = s.size();
  string aux = "";
  if (v == 0){
    aux = "ZERO";
  } else if (v == 2){
    aux = "TWO";
  } else if (v == 4){
    aux = "FOUR";
  } else if (v == 6){
    aux = "SIX";
  } else if (v == 1){
    aux = "ONE";
  } else if (v == 3){
    aux = "THREE";
  } else if (v == 8){
    aux = "EIGHT";
  } else if (v == 7){
    aux = "SEVEN";
  } else if (v == 5){
    aux = "FIVE";
  } else if (v == 9){
    aux = "NINE";
  }
  del_aux(s, cnt, aux, mark, tam);
}

int main(){
  int T;
  int casos = 1;
  cin >> T;
  while(T--){
    printf("Case #%d: ", casos++);
    string s;
    cin >> s;
    int tam = s.size();
    vi mark(tam+10, 0);

    vi ans;
    vi n ({0, 2, 4, 6, 1, 3, 8, 7, 5, 9});
    for (int i = 0; i < 10; i++){
      int num = n[i];
      int cnt = conta(num, s, mark);
      deleta(num, s, mark, cnt);
      while(cnt--) ans.pb(num);
    }
    sort(ans.begin(), ans.end());
    for(auto& x : ans) printf("%d", x);
    cout << endl;
  }
  return 0;
}
