#include <cstdio>
#include <algorithm>
using namespace std;

int main(){
  
  int T, t, N, M, i, j, maks;
  bool ok;
  scanf ("%d", &T);
  for (t = 1; t <= T; t++){
    scanf("%d %d", &N, &M);
    int tab [N][M];
    bool wyn [N][M];
    
    for (i= 0; i < N; i++)
      for (j = 0; j <M; j++){
        scanf("%d", &tab[i][j]);
        wyn [i][j] = false;
      }
      
     /*for (i= 0; i < N; i++){
      for (j = 0; j <M; j++){
        printf("%d", tab[i][j]);
      }
      printf ("\n");
    }*/
 
      
    for ( i = 0; i < N; i++){
        maks = 0;
      for (j = 0; j <M; j++){
        maks = max(tab[i][j], maks);
      }      
      for (j = 0; j <M; j++){
        if (tab[i][j] == maks){
          wyn[i][j] = true;
        //  printf ("%d %d \n", i, j);
        }
      }    
    }
    
    for ( j = 0; j < M; j++){
        maks = 0;
      for (i = 0; i <N; i++){
        maks = max(tab[i][j], maks);
      }      
      for (i = 0; i <N; i++){
        if (tab[i][j] == maks)
          wyn[i][j] = true;
      }    
    }
    ok = true;
    for (i= 0; i < N; i++)
      for (j = 0; j <M; j++){
        if(!wyn [i][j])
        ok = false;
      }    
    if (ok)
    printf("Case #%d: YES\n", t);
    else
    printf("Case #%d: NO\n", t);
  }
  
  
  return 0;
}
