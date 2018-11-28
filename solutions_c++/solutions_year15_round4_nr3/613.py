//bcw0x1bd2 {{{
#include<bits/stdc++.h>
using namespace std;
#define FZ(n) memset((n),0,sizeof(n))
#define FMO(n) memset((n),-1,sizeof(n))
#define MC(n,m) memcpy((n),(m),sizeof(n))
#define F first
#define S second
#define MP make_pair
#define PB push_back
#define FOR(x,y) for(__typeof(y.begin())x=y.begin();x!=y.end();x++)
#define IOS ios_base::sync_with_stdio(0); cin.tie(0);
#ifdef ONLINE_JUDGE
#define FILEIO(name) \
  freopen(name".in", "r", stdin); \
  freopen(name".out", "w", stdout);
#else
#define FILEIO(name)
#endif

void RI() {}

template<typename... T>
void RI( int& head, T&... tail ) {
	    scanf("%d",&head);
			    RI(tail...);
}

mt19937 rng(0x5EED);
int randint(int lb, int ub) {
    return uniform_int_distribution<int>(lb, ub)(rng);
}
// Let's Fight! }}}

int N;
vector<int> sent[205];
map<string,int> idx;
int app1[5000],app2[5000],app3[5000],app4[5000];


void input(){
  idx.clear();
  int nID = 0;
  cin >> N;
  string str;
  getline(cin,str);
  for (int i=0; i<N; i++){
    sent[i].clear();
    getline(cin,str);
    string tmp;
    tmp = "";
    for (int j=0; j<(int)str.length(); j++){
      if ('a' <= str[j] && str[j] <= 'z'){
        tmp += str[j];
      } else {
        if (tmp != ""){
          if (!idx.count(tmp)) idx[tmp] = nID++;
          sent[i].PB(idx[tmp]);
        }
        tmp = "";
      }
    }
    if (tmp != ""){
      if (!idx.count(tmp)) idx[tmp] = nID++;
      sent[i].PB(idx[tmp]);
    }
    sort(sent[i].begin(), sent[i].end());
    sent[i].resize(unique(sent[i].begin(),sent[i].end())-sent[i].begin());
  }
}
void solve(int t){
  FZ(app1);
  FZ(app2);
  FZ(app3);
  FZ(app4);
  int dft = 0;
  set<int> s0,s1;
  for (auto it : sent[0])
    app1[it] = 1;
  for (auto it : sent[1]){
    if (app1[it]) dft++;
    app2[it] = 1;
  }
  int ans = 2147483647;
  if (N == 2) ans = dft;
  for (int i=0; i<(1<<(N-2)); i++){
    int tmp = dft;
    vector<int> s2,s3;
    for (int j=0; j<N-2; j++){
      if (i & (1<<j)){ // j+2 English
        for (auto it : sent[j+2]){
          if (!app1[it] && !app3[it]){
            app3[it] = 1;
            s2.PB(it);
          }
        }
      } else { // j+2 French
        for (auto it : sent[j+2]){
          if (!app2[it] && !app4[it]){
            app4[it] = 1;
            s3.PB(it);
          }
        }
      }
    }
    for (auto it : s2){
      if (app2[it]) tmp++;
      if (app4[it]) tmp++;
    }
    for (auto it : s3){
      if (app1[it]) tmp++;
    }
    ans = min(ans,tmp);
    for (int j=0; j<N-2; j++){
      if (i & (1<<j)){ // j+2 English
        for (auto it : sent[j+2]){
          app3[it] = 0;
        }
      } else { // j+2 French
        for (auto it : sent[j+2]){
          app4[it] = 0;
        }
      }
    }
  }
  cout << "Case #" << t << ": " << ans << endl;
}
int main(){
  IOS;
  cout << fixed;
  cout << setprecision(15);
  int nT;
  cin >> nT;
  for (int _t=1; _t<=nT; _t++){
    fprintf(stderr, "%d\n", _t);
    input();
    solve(_t);
  }

  return 0;
}

