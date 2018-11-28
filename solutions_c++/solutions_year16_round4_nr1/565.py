#include <cstdio>
#include <cassert>
#include <string>

using namespace std;

struct st {
  st(int r,int p,int s) : r(r),p(p),s(s) {}
  int r,p,s;
  st prev() {
    st ret(r+p,p+s,s+r);
    return ret;
  }
  bool eq(int rr,int pp,int ss) { return rr==r && ss==s && pp==p; }
};

string minS[13],minR[13],minP[13];
void run() {
  int N,R,P,S;
  scanf("%d%d%d%d",&N,&R,&P,&S);
  assert((1<<N)==R+P+S);
  st xr(1,0,0),xp(0,1,0),xs(0,0,1);
  for (int i=0;i<N;++i) {
    xr=xr.prev();
    xp=xp.prev();
    xs=xs.prev();
  }
  if (xr.eq(R,P,S)) printf("%s\n",minR[N].c_str());
  else if (xp.eq(R,P,S)) printf("%s\n",minP[N].c_str());
  else if (xs.eq(R,P,S)) printf("%s\n",minS[N].c_str());
  else printf("IMPOSSIBLE\n");
}

int main() {
  minS[0]="S";
  minR[0]="R";
  minP[0]="P";
  for (int i=1;i<13;++i) {
    if (minS[i-1]<minR[i-1]) minR[i]=minS[i-1]+minR[i-1]; else minR[i]=minR[i-1]+minS[i-1];
    if (minP[i-1]<minS[i-1]) minS[i]=minP[i-1]+minS[i-1]; else minS[i]=minS[i-1]+minP[i-1];
    if (minR[i-1]<minP[i-1]) minP[i]=minR[i-1]+minP[i-1]; else minP[i]=minP[i-1]+minR[i-1];
  }
  int T;
  scanf("%d",&T);
  for (int t=1;t<=T;++t) {
    printf("Case #%d: ",t);
    run();
  }
  return 0;
}
