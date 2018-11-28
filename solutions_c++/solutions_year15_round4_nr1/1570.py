#include <cstdio>

int D[4][2] = {{-1, 0}, {0, -1}, {1, 0}, {0, 1}};
int T;
int R, C;
int ans;
char table[128][128];
bool chk[128][128];
bool imp;

int convert(char dir){
  if(dir == '^')return 0;
  if(dir == '<')return 1;
  if(dir == 'v')return 2;
  if(dir == '>')return 3;
}

void walk(int r, int c){
  //printf("__%d %d\n", r, c);
  int i, k;
  int dir = convert(table[r][c]);

  if(chk[r][c] == 1)return;
  chk[r][c] = 1;

  for(k = 0; k < 4; k++){
    //printf("%d %d %d\n", k, r, c);
    i = 1;
    while(0 <= r + D[(dir + k) % 4][0]*i && r + D[(dir + k) % 4][0]*i < R && 0 <= c + D[(dir + k) % 4][1]*i && c + D[(dir + k) % 4][1]*i < C){
      if(table[r + D[(dir + k) % 4][0]*i][c + D[(dir + k) % 4][1]*i] != '.'){
	walk(r + D[(dir + k) % 4][0]*i, c + D[(dir + k) % 4][1]*i);
	if(k > 0)
	  ans++;
	return;
      }
      i++;
    }
  }

  imp = true;
}

int main(){
  int i, j;

  scanf("%d", &T);
  
  for(int tt = 1; tt <= T; tt++){
    scanf("%d %d", &R, &C);
    for(i = 0; i < R; i++)
      scanf("%s", table[i]);

    ans = 0;
    for(i = 0; i < R; i++)
      for(j = 0; j < C; j++)
	chk[i][j] = 0;
    imp = false;
    
    for(i = 0; i < R; i++)
      for(j = 0; j < C; j++)
	if(table[i][j] != '.')
	  walk(i, j);
    
    printf("Case #%d: ", tt);
    if(imp)printf("IMPOSSIBLE\n");
    else printf("%d\n", ans);
  }
}
