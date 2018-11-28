#include <cstdio>
#include <cstring>
#include <iostream>
#include <stack>

using namespace std;

int row1, row2;
int gaze1[5][5];
int gaze2[5][5];

void input(){
   scanf("%d", &row1);
    for(int i = 1; i <= 4; i ++){
      for(int j = 1; j <= 4; j ++){
        scanf("%d", &gaze1[i][j]);
      }
    }
    scanf("%d", &row2);
    for(int i = 1; i <= 4; i ++){
      for(int j = 1; j <= 4; j ++){
        scanf("%d", &gaze2[i][j]);
      }
    }
}

int main()
{
  int t, flag;
  flag = 1;
  //freopen("in.txt", "r", stdin);
  scanf("%d", &t);
  while(t--){
    input();
    int cnt[17];
    memset(cnt, 0, sizeof(cnt));
    for(int i = 1; i <= 4; i ++){
      for(int j = 1; j <= 4; j ++)
      if(gaze1[row1][i] == gaze2[row2][j]){
        cnt[gaze1[row1][i]] ++;
      }
    }
    int ans, num;
    ans = num = 0;
    for(int i = 1; i <= 16; i ++){
      if(cnt[i] == 1) {
          ans = i;
          num ++;
      }
    }
    printf("Case #%d: ", flag ++);
    //cout << "x" << ans << " " << num << endl;
    if(num == 0) printf("Volunteer cheated!\n");
    else if(num == 1) printf("%d\n", ans);
    else printf("Bad magician!\n");
  }
  return 0;
}
