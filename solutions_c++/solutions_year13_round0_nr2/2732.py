#include <stdio.h>

void fill(int map[][100], int m, int n, int before, int after){
   for(int i = 0; i < m; ++i){
   for(int j = 0; j < n; ++j){
      if(map[i][j] == before) map[i][j] = after;
   }}
   
   /*for(int i = 0; i < m; ++i){
   for(int j = 0; j < n; ++j)
      printf("%d ", map[i][j]);
      puts("");
   }*/
}

bool check(int map[][100], int m, int n, int h){
   bool mask[100][100] = {0};
   for(int i = 0; i < m; ++i){
      if(map[i][0] == h && map[i][n-1] == h){
         int j;
         for(j = 0; j < n; ++j) if(map[i][j] != h) break;
         if(j < n) continue;
         for(j = 0; j < n; ++j) mask[i][j] = true;
      }
   }
   
   for(int j = 0; j < n; ++j){
      if(map[0][j] == h && map[m-1][j] == h){
         int i;
         for(i = 0; i < m; ++i) if(map[i][j] != h) break;
         if(i < m) continue;
         for(i = 0; i < m; ++i) mask[i][j] = true;
      }
   }
   
   for(int i = 0; i < m; ++i){
   for(int j = 0; j < n; ++j){
      if(mask[i][j] && map[i][j] != h) return false;
      if(!mask[i][j] && map[i][j] == h) return false;
   }}
   
   return true;
}

int main(){
   int test, m, n, ti = 1;
   scanf("%d", &test);
   
   while(test-- && scanf("%d%d", &m, &n)){
      bool has[101] = {0};
      int map[100][100];
      
      for(int i = 0; i < m; ++i){
      for(int j = 0; j < n; ++j){
         scanf("%d", &map[i][j]);
         has[ map[i][j] ] = true;
      }}
      
      int last = 0, h;
      for(h = 1; h <= 100; ++h){
         if(last) fill(map, m, n, last, h);
         if(has[h]){
            if( !check(map, m, n, h) ) break;
            last = h;
         }
      }
      
      if(h <= 100) printf("Case #%d: NO\n", ti++);
      else printf("Case #%d: YES\n", ti++);
   }

   return 0;
}
