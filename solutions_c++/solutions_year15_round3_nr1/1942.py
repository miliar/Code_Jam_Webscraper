#include <cstdio>
#include <vector>
#include <cassert>
#include <algorithm>

using namespace std;

int run() {
  int R,C,W;
  scanf("%d%d%d",&R,&C,&W);
  if (W==1) return R*C;
  int g=(C+W-1)/W;
  int sol=g*R-1+W;
  int h=C-(g-1)*W;
  if (h>W) ++sol;
  return sol;
}

int main() {
  int T;
  scanf("%d",&T);
  for (int t=1;t<=T;++t) {
    printf("Case #%d: %d\n",t,run());
  }
  return 0;
}

/*
  if (W==1) return R*C;
  if (W==C) return R+C-1;
  int g=(C+2*W-2)/(2*W-1);
  if (g==1) return R+W;
  int sol=g*R-1;
  int h=C-(2*W-1)*(g-1);
  assert(h>0);
  if (g>1) h+=W-1;
  sol+=W;
  if (W<h) ++sol;
*/
