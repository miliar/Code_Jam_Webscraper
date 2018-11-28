#include <bits/stdc++.h>
using namespace std;
#define forn(i, n) for(int i = 0; i < (int) (n); i++)

int tc, TC;
string w;

int main(){
  freopen("B-large.in", "r", stdin);
  freopen("B-large.out", "w", stdout);
  scanf("%d", &tc);
  while(tc--){
    int ans = 0;
    cin >> w;
    w += '+';
    forn(i, w.size() - 1){
      if(w[i] != w[i + 1]) ans++;
    }
    printf("Case #%d: %d\n", ++TC, ans);
  }
  return 0;
}
