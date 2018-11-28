#include <bits/stdc++.h>
using namespace std;

int t, a[4][4], b[4][4], row_1, row_2, x[17];
vector <int> ans;

int main(){

  scanf("%d", &t);
  for(int ct = 1; ct <= t; ct ++){

    scanf("%d", &row_1);
    for(int i = 0; i < 4; i ++)
      for(int j = 0; j < 4; j ++)
        scanf("%d", &a[i][j]);

    scanf("%d", &row_2);
    for(int i = 0; i < 4; i ++)
      for(int j = 0; j < 4; j ++)
        scanf("%d", &b[i][j]);

    memset(x, 0, sizeof x);
    for(int i = 0; i < 4; i ++){
      x[a[row_1-1][i]] ++;
      x[b[row_2-1][i]] ++;
    }
    
    ans.clear();
    for(int i = 1; i <= 16; i ++)
      if(x[i] == 2)
        ans.push_back(i);

    if((int)ans.size() == 0)
      printf("Case #%d: Volunteer cheated!\n", ct);
    else if((int)ans.size() == 1)
      printf("Case #%d: %d\n", ct, ans[0]);
    else
      printf("Case #%d: Bad magician!\n", ct);
      
  }

  return 0;
}
