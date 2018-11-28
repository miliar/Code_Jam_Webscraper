#include <cstdio>

int T;
int N, M;
int x;
bool chk[20];
int ct, ans;

int main(){
  int i, j;

  freopen("A-small-attempt0.in", "r", stdin);
  freopen("Magic_trick.txt", "w", stdout);

  scanf("%d", &T);
  for( int tt = 1; tt <= T; tt++){

    ct = 0;
    for( i = 1; i <= 16; i++)
      chk[i] = 0;

    scanf("%d", &N);
    for( i = 1; i <= 4; i++){
      for( j = 1; j <= 4; j++){
	scanf("%d", &x);
	if( i == N)chk[x] = true;
      }
    }

    scanf("%d", &N);
    for( i = 1; i <= 4; i++){
      for( j = 1; j <= 4; j++){
	scanf("%d", &x);
	if( i == N){
	  if( chk[x]){
	    ct++;
	    ans = x;
	  }
	}
      }
    }

    printf("Case #%d: ", tt);
    if( ct == 0)printf("Volunteer cheated!\n");
    else if( ct == 1)printf("%d\n",ans);
    else printf("Bad magician!\n");
  } 
}
