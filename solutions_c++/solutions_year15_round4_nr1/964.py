#include <stdio.h>

char s[101][101];
int dir[101][101];

int main(){
   int T, n, m;
   int ans;
   bool flg;
   scanf("%d", &T);
   for(int t=1; t<=T; ++t){
      scanf("%d%d", &n, &m);
      for(int i=0; i<n; ++i) scanf("%s", s[i]);
      for(int i=0; i<n; ++i){
         for(int j=0; j<m; ++j) dir[i][j] = 0;
      }

      for(int i=0; i<n; ++i){
         for(int j=0; j<m; ++j){
            if(s[i][j] != '.'){
               dir[i][j] |= 1;
               break;
            }
         }
         for(int j=m-1; j>=0; --j){
            if(s[i][j] != '.'){
               dir[i][j] |= 2;
               break;
            }
         }
      }
      for(int j=0; j<m; ++j){
         for(int i=0; i<n; ++i){
            if(s[i][j] != '.'){
               dir[i][j] |= 4;
               break;
            }
         }
         for(int i=n-1; i>=0; --i){
            if(s[i][j] != '.'){
               dir[i][j] |= 8;
               break;
            }
         }
      }

      ans = 0;
      flg = false;
      for(int i=0; i<n; ++i){
         for(int j=0; j<m; ++j){
            if(dir[i][j] == 15) flg = true;
            if(s[i][j] == '.') continue;
            if(s[i][j] == '<' && (dir[i][j]&1)) ans++;
            if(s[i][j] == '>' && (dir[i][j]&2)) ans++;
            if(s[i][j] == '^' && (dir[i][j]&4)) ans++;
            if(s[i][j] == 'v' && (dir[i][j]&8)) ans++;
         }
      }
      printf("Case #%d: ", t);
      if(flg) printf("IMPOSSIBLE\n");
      else printf("%d\n", ans);
   }

   return 0;
}
