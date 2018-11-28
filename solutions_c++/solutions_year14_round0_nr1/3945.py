#include <stdio.h>
#include <string.h>

int t1[4][4], t2[4][4], chk[17];

int main(){
  
  int t, T, ans1, ans2, i, j, ok, ans;

  scanf("%d", &T);
  for(t=1; t<=T; t++){
    scanf("%d", &ans1);
    for(i=0; i<4; i++) for(j=0; j<4; j++) scanf("%d", &t1[i][j]);
    scanf("%d", &ans2);
    for(i=0; i<4; i++) for(j=0; j<4; j++) scanf("%d", &t2[i][j]);
    memset(chk, 0, sizeof(chk));
    for(i=0; i<4; i++) chk[t1[ans1-1][i]]++;
    for(i=0; i<4; i++) chk[t2[ans2-1][i]]++;
    ans=-1;
    for(i=0; i<4; i++){
      if(chk[t1[ans1-1][i]] == 2 && ans == -1) ans=t1[ans1-1][i];
      else if(chk[t1[ans1-1][i]] == 2 && ans != -1){ ans=-1; break; }
    }
    printf("Case #%d: ", t);
    if(ans != -1) printf("%d\n", ans);
    else if(i<4) puts("Bad magician!");
    else puts("Volunteer cheated!");
  }
  
  return 0;
}
