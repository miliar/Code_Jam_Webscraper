#include <bits/stdc++.h>
using namespace std;
#define forn(i, n) for(int i = 0; i < (int) (n); i++)
typedef long long tint;
const int N = 60;

int tc, TC, grid[N][N];
tint m, n;

int main(){
  freopen("in.in", "r", stdin);
  freopen("out.out", "w", stdout);
  scanf("%d", &tc);
  while(tc--){
    memset(grid, 0, sizeof grid);
    
    cin >> n >> m;
    
    tint k = (1LL << (n - 2LL));
    
    if(k < m){
      printf("Case #%d: IMPOSSIBLE\n", ++TC);
      continue;
    }
    
    printf("Case #%d: POSSIBLE\n", ++TC);
    forn(i, n - 1LL){
      forn(j, n - 1LL){
        if( i < j ) grid[i][j] = 1;
      }
    }
    
    forn(i, N){
      if( m & (1LL << i) ){
        if(i + 1 == n - 1){
          forn(j, n - 1){
            grid[j][ n - 1 ] = 1;
          }
        }
        else grid[i + 1][ n - 1 ] = 1;
      }
    }
    
    forn(i, n){
      forn(j, n){
        printf("%d", grid[i][j]);
      }
      puts("");
    }
    
  }
  return 0;
}
