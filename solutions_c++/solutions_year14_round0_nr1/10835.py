#include <cstdio>
#define sh short int
sh num[17];
inline void solve(sh x) {
  sh  a;
  for (sh i = 1; i <= 4; ++i) {
    for (sh j = 0; j < 4; ++j){
      scanf("%hd",&a);
      if (i == x) {
        ++num[a];
      }
    }
  }
}
inline void find(sh x) {
  printf("Case #%hd: ",x);
  int nr = 0, last = 0;
  for (sh i = 1; i <= 16; ++i) {
    if (num[i] == 2) {
      ++nr;
      last = i;
    }
    num[i] = 0;
  }
  if (nr == 1) {
    printf("%d\n",last);
    return;
  }
  if (nr == 0) {
    printf("Volunteer cheated!\n");
    return;
  }
  printf("Bad magician!\n");

}
int main() {
  sh T;
  freopen("date.in","r",stdin);
  freopen("date.out","w",stdout);
  scanf("%hd",&T);
  for (sh i = 1; i <= T; ++i) {
    sh x;
    scanf("%hd",&x);
    solve(x);
    scanf("%hd",&x);
    solve(x);
    find(i);
  }
  return 0;
}
