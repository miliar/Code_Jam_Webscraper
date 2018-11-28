#include <bits/stdc++.h>

#define F first
#define S second
#define llong long long
#define ullong unsigned long long
#define mp make_pair
#define pb push_back

using namespace std;

const int INF = (int)1e9 + 7;
const int MXN = (int)1e6 + 10;
const double EPS = (double)1e-9;

int n, T;
vector <int> v;
map <ullong, int> mem;

void Erase(vector <int> &v, int x){
  for(int i = 0; i < v.size(); ++i){
    if(v[i] == x){
      v.erase(v.begin() + i);
      return;
    }
  }
}

llong encode(const vector <int> &v){
  ullong h = 0LL, p = 1LL;
  for(int i = 0; i < v.size(); ++i){
    h += v[i] * 1LL * p;
    p *= 10LL;
  }
  return h;
}

vector <int> decode(ullong h){
  vector <int> tmp;
  while(h){
    tmp.pb(h % 10LL);
    h /= 10LL;
  }
  return tmp;
}

void rec(ullong h){
  if(mem.count(h))
    return;
  vector <int> v = decode(h);
  //assert(h > 0);
  //for(int i = 0; i < v.size(); ++i)
  //  assert(v[i] > 0);
  //cerr << h << "\n";
  if(v.back() <= 3){
    mem[h] = v.back();
    return;
  }
  vector <int> tmp;
  for(int i = 0; i < v.size(); ++i){
    if(v[i] > 1)
      tmp.pb(v[i] - 1);
  }
  ullong hh = encode(tmp);
  rec(hh);
  mem[h] = mem[hh] + 1;
  int mx = v.back();
  for(int i = 1; i <= mx / 2; ++i){
    v.pop_back();
    v.pb(i);
    v.pb(mx - i);
    sort(v.begin(), v.end());
    hh = encode(v);
    rec(hh);
    mem[h] = min(mem[h], mem[hh] + 1);
    Erase(v, i);
    Erase(v, mx - i);
    v.pb(mx);
    sort(v.begin(), v.end());
  }
}

int main(){
  #ifdef LOCAL
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
  #endif
  scanf("%d", &T);
  for(int test = 1; test <= T; ++test){
    scanf("%d", &n);
    v.resize(n);
    for(int i = 0; i < n; ++i)
      scanf("%d", &v[i]);
    sort(v.begin(), v.end());
    rec(encode(v));
    printf("Case #%d: %d\n", test, mem[encode(v)]);
  }
  return 0;
}
