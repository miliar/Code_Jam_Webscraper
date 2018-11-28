#include <cstdio>
#include <cstring>
using namespace std;

int ma[200][200];
int mx[120], my[120];
int n, m;

void input(){
  scanf("%d%d", &n, &m);
  memset(mx, 0, sizeof(mx));
  memset(my, 0, sizeof(my));
  for (int i = 0; i < n; ++ i){
    for (int j = 0; j < m; ++ j){
      scanf("%d", &ma[i][j]);
      if (mx[i] < ma[i][j]) mx[i] = ma[i][j];
      if (my[j] < ma[i][j]) my[j] = ma[i][j];
    }
  }
}

char solve(){
  for (int i = 0; i < n; ++ i){
    for (int j = 0; j < m; ++ j){
      if (ma[i][j] < mx[i] && ma[i][j] < my[j]) {
        return 'N';
      }
    }
  }
  return 'Y';
}

int main(){
  int t;
  scanf("%d", &t);
  for (int c = 1; c <= t; ++ c){
    input();
    printf("Case #%d: ", c);
    char r = solve();
    if (r == 'Y')
      puts("YES");
    else
      puts("NO");
  }
  return 0;
}
