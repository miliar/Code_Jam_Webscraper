#include <bits/stdc++.h>
#define mp make_pair
#define pb push_back

using namespace std;

#define TASKNAME "A"
#define TASKMOD "small"
#define MAXN int(100)

typedef long long ll;
typedef long double ld;
int testNum;

int mat[5][5], mat1[5][5];

void solve(){
  int ans1 = 0 , ans2 = 0, used[MAXN];
  for(int i = 0; i < MAXN; i++)
    used[i] = 0;
  scanf("%d", &ans1);
  for (int i = 0; i < 4; i++)
    for (int j = 0; j < 4; j++){       
      scanf(" %d",&mat[i][j]);
      if(i == ans1 - 1)
        used[mat[i][j]]++;
    }

  scanf("%d", &ans2);
  for (int i = 0; i < 4; i++)
    for (int j = 0; j < 4; j++){       
      scanf(" %d",&mat[i][j]);
      if(i == ans2 - 1)
        used[mat[i][j]]++;
    }
  int ans = 0, index = -1;
  for(int  i = 1; i <= 16; i++)
    if(used[i] > 1){
      ans++;
      index = i;
    }
  if(ans == 1)
    printf("%d\n", index);
  else if(ans == 0)
    printf("Volunteer cheated!\n");
  else
    printf("Bad magician!\n");
                     
}


int main(){
  freopen(TASKNAME"-"TASKMOD".in","r",stdin);
  freopen(TASKNAME"-"TASKMOD".out","w",stdout);
  scanf("%d", &testNum);
  for (int testId = 1; testId <= testNum; testId++){
    printf("Case #%d: ",testId);
    solve();
  }
  return 0;  
}