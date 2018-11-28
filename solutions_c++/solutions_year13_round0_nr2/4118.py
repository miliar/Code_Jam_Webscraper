#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;
int f[100][100];
int h,w;
bool solve(){
  for(int i=0;i<h;++i){
    for(int j=0;j<w;++j){
      int a = f[i][j];
      bool flgc = true,flgr = true;
      for(int y=0;y<h;++y){
	if(a < f[y][j]){
	  flgc = false;
	  break;
	}
      }
      for(int x=0;x<w;++x){
	if(a < f[i][x]){
	  flgr = false;
	  break;
	}
      }
      if(!flgr && !flgc) return false;
    }
  }
  return true;
}
int main(){
  int T;
  scanf("%d",&T);
  for(int t=1;t<=T;++t){
    scanf("%d%d",&h,&w);
    for(int i=0;i<h;++i) for(int j=0;j<w;++j) scanf("%d",&f[i][j]);
    printf("Case #%d: ",t);
    if(solve()) printf("YES\n");
    else printf("NO\n");
  }
  return 0;
}
