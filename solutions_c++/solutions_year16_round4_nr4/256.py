#include <iostream>
#include <algorithm>
#include <cstring>
using namespace std;

int N;
string G[100];
int ret;
int t[100];
int ord[100];
bool used[100];
bool rec2(int cur = 0) {
  if(cur == N) return true;
  bool ret = false;
  bool ret2 = true;
  for(int j = 0; j < N; j++) {
    if(used[j])continue;
    if(G[ord[cur]][j] == '1') {
      used[j] = true;
      if(!rec2(cur + 1)) {
        ret2 = false;
      }else{
        ret = true;
      }
      used[j] = false;
    }
  }
  return ret && ret2;
}
bool all() {
  memset(used, 0, sizeof(used));
  for(int i = 0; i < N; i++) ord[i] = i;
  do{
    if(!rec2(0))return false;
  }while(next_permutation(ord, ord + N));
  return true;
}

void rec(int x, int y, int cnt) {
  int nx = x + 1, ny = y;
  if(y == N) {
    if(all()) ret = 1;
    return;
  }
  if(ret) return;
  if(nx == N) {nx = 0;ny++;}
  if(G[x][y] == '1') {
    rec(nx, ny, cnt);
  }else{
    if(cnt > 0) {G[x][y] = '1';
      rec(nx, ny, cnt - 1);
      G[x][y] = '0';
    }
    rec(nx, ny, cnt);
  }
}
// 教えるパターンを全列挙
bool check(int cnt) {
  ret = 0;
  rec(0, 0, cnt);
  if(ret == 1)return true;
  return false;
}
void solve(){
  for(int add = 0; add <= N * N; add++) {
    if(check(add)){
      cout << add << endl;
      break;
    }
  }
}
int main() {
  int T;
  cin>>T;
  for(int tc= 1;tc<=T;tc++) {
    cout << "Case #" << tc << ": ";
    cin >> N;
    for(int i = 0; i < N; i++)cin >> G[i];
    ret = 0;
    solve();
  }

}
