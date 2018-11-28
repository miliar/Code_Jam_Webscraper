#include <bits/stdc++.h>
using namespace std;
#define forn(i, n) for(int i = 0; i < (int) (n); i++)

int tc, n, TC;
bool used[10];

bool add(int v){
  while(v){
    used[(v % 10)] = true;
    v /= 10;
  }
  forn(i, 10){
    if(!used[i]) return false;
  }
  return true;
}

int main(){
  freopen("A-large.in", "r", stdin);
  freopen("A-large.out", "w", stdout);
  scanf("%d", &tc);
  while(tc--){
    ++TC;
    scanf("%d", &n);
    int i; 
    memset(used, false, sizeof used);
    for(i = 1; i < 1000000; i++){
      if(add(n * i)){
        printf("Case #%d: %d\n", TC, n * i);
        break;
      }
    }
    if(i == 1000000){
      printf("Case #%d: INSOMNIA\n", TC);
      if(n) assert(false);
    }
  }
  return 0;
}
