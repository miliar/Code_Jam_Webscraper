#include<stdio.h>
#include<vector>
#include<algorithm>
#include<string>
#include<queue>
#include<map>
#include<set>
using namespace std;
int R,C;
int l[200],r[200];
int maze;
int get(int i, int j) {
  return (maze & (1 << (i * C + j))) ? 1 : 0;
}
void lookup(int a, int& i, int& j, int& up) {
  if (a<=C) {
    up=1;
    i=0;
    j=a-1;
  }else if(a<=C+R) {
    i=a-C-1;
    j=C-1;
    up=get(i,j) ? 1 : 0;
  }else if (a<=C+R+C) {
    i=R-1;
    j=(C-1) - (a-C-R-1);
    up=0;
  }else{
    i=(R-1) - (a-C-R-C-1);
    j=0;
    up=get(i,j) ? 0:1;
  }
}
bool vis[100][100][2];
bool dfs(int ai,int aj, int au, int bi, int bj, int bu) {
  if (ai==bi && aj==bj && au==bu)return true;
  vis[ai][aj][au]=true;
  if (au && ai>0) {
    int ci=ai-1,cj=aj, cu=0;
    if (!vis[ci][cj][cu]) {
      if (dfs(ci,cj,cu,bi,bj,bu))return true;
    }
  }
  if (!au && ai <R-1) {
    int ci=ai+1,cj=aj, cu=1;
    if (!vis[ci][cj][cu]) {
      if (dfs(ci,cj,cu,bi,bj,bu))return true;
    }
  }
  if(aj<C-1) {
    if((get(ai,aj) && au) || (!get(ai,aj) && !au)) {
      int ci=ai,cj=aj+1, cu;
      cu = get(ci,cj) ? 0 : 1;
      if (!vis[ci][cj][cu]) {
        if (dfs(ci,cj,cu,bi,bj,bu))return true;
      }
    }
  }
  if(aj>0) {
    if((get(ai,aj) && !au) || (!get(ai,aj) && au)) {
      int ci=ai,cj=aj-1, cu;
      cu = get(ci,cj) ? 1 : 0;
      if (!vis[ci][cj][cu]) {
        if (dfs(ci,cj,cu,bi,bj,bu))return true;
      }
    }
  }
  return false;
}
bool con(int a, int b) {
  int ai,aj,au,bi,bj,bu;
  lookup(a,ai,aj,au);
  lookup(b,bi,bj,bu);
  memset(vis,0,sizeof(vis));
  return dfs(ai,aj,au,bi,bj,bu);
}
bool valid() {
  for (int i=0;i<R+C;i++) {
    if (!con(l[i], r[i])) return false;
  }
  return true;
}
int main() {
  int T;
  scanf("%d",&T);
  for(int tn=1;tn<=T;tn++){
    scanf("%d%d", &R,&C);
    for(int i=0;i<R+C;i++) {
      scanf("%d%d",l+i,r+i);
    }
    double res = 0;
    for (maze = 0; maze < (1 << (R*C));maze++) {
      if(valid())break;
    }
    if(maze == 1<<(R*C))
      printf("Case #%d:\nIMPOSSIBLE\n", tn);
    else {
      printf("Case #%d:\n", tn);
      for (int i=0;i<R;i++){
        for (int j=0;j<C;j++) {
          putchar(get(i,j) ? '\\' : '/');
        }
        putchar(10);
      }
    }
  }
  return 0;
}
