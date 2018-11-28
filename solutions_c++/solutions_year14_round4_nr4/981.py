#include <iostream>
#include <set>
using namespace std;

int N, M;

string a[10];

int r[10];
int res, cnt;

void scan(){
  cin >> N >> M;
  
  for(int i = 0; i < N; ++i){
    cin >> a[i];
  }
}


void check(){
  set<string> st[4];
  for(int i = 0; i < M; ++i){
    int ok = 0;
    st[i].insert("");
    for(int j = 0; j < N; ++j){
      if(r[j] == i){
	for(int k = 0; k <= a[j].size(); ++k)
	  st[i].insert(a[j].substr(0, k));
	ok = 1;
      }
    }
    if(!ok)
      return;
  }
  
  int cur = st[0].size() + st[1].size() + st[2].size() + st[3].size();
  
  if(cur == res){
    cnt++;
  }
  if(cur > res){
    res = cur;
    cnt = 1;
  }
}

void go(int idx){
  if(idx == N){
    check();
    return;
  }
 // cout << idx << endl;
  
  for(int i = 0; i < M; ++i){
    r[idx] = i;
    go(idx + 1);
  }
  
}
void solve(int q){
  cout << "Case #" << q << ": ";
  res = cnt = 0;
  go(0);
  
  cout << res << " " << cnt << endl;
}

int main(){
  int tests;
  
  cin >> tests;
  
  for(int i = 1; i <= tests; ++i){
    scan();
    solve(i);
  }
}
