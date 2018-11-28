#include <bits/stdc++.h>
#define MAXN 105
#define EPS 1e-8
using namespace std;

typedef double LF;
typedef pair<int,int> pii;
int testcase, R, C,B[10][10];
set <string> S;
int dir[4][2] = {{1,0},{0,1},{-1,0},{0,-1}};
int blah = 0;
map <pii,int> ans;

bool can(int x,int y) {
  //if (blah) printf("it is %d\n",B[x][y]);
  if (x < 0 || x > R) return 1;
  if (B[x][y] == -1) return 1;
  int ok = 1, sum = 0;
  for (int k=0;k<4;++k) {
    int a = x + dir[k][0];
    if (a < 0 || a >= R) continue;
    int b = y + dir[k][1] + C;//) % C;
    while (b >= C) b -= C;
    if (a == x && b == y) continue;
    if (B[a][b] == -1) {
     // if (blah) printf("aww (%d,%d)\n",a,b);
      ok = 0;
    }
    if (B[a][b] == B[x][y]) ++sum;
  }
 // if (blah) printf("(%d,%d), %d: sum = %d, ok = %d\n",x,y,B[x][y],sum,ok);
  if (ok && sum != B[x][y]) {
   // if (blah) printf("Y NO FAIL?\n");
    return 0;
  }
  return 1;
}

void recurse(int x,int y) {
  if (y >= C) recurse(x+1,0);
  else if (x >= R) {
    for (int i=0;i<R;++i)
      for (int j=0;j<C;++j)
        if (!can(i,j)) return;
    string t = "", cur;
    for (int k=0;k<C;++k) {
      cur = "";
      for (int j=0;j<C;++j)
        for (int i=0;i<R;++i) {
          cur += '0' + B[i][(j+k)%C];
        }
      if (t == "" || cur < t) t = cur;
    }
  //  for (int i=0;i<R;++i,printf("\n"))
  //    for (int j=0;j<C;++j) printf("%d",B[i][j]);
  //  printf("\n");
    S.insert(t);
  }
  else {
    for (int i=1;i<=4;++i) {
      B[x][y] = i;
      if (can(x-1,y)) recurse(x,y+1);
    }
    B[x][y] = -1;
  }
}

int main () {
  scanf("%d",&testcase);
  for (int TC=1;TC<=testcase;++TC) {
    scanf("%d%d",&R,&C);
    if (ans.find(pii(R,C)) == ans.end()) {
      memset(B,-1,sizeof(B));
      S.clear();
      recurse(0,0);
      ans[pii(R,C)] = (int)S.size();
    }
    printf("Case #%d: %d\n",TC,ans[pii(R,C)]);
  }
}
