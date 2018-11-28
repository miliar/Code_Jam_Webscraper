#include<stdio.h>
#include<string>
using namespace std;

void solve(int t) {
  int N,R,P,S;
  scanf("%d %d %d %d",&N,&R,&P,&S);
  
  string sR = "R";
  string sP = "P";
  string sS = "S";
  
  for(int n = N-1;n>=0;n--) {
    string nR = (sR < sS)?sR+sS:sS+sR;
    string nP = (sR < sP)?sR+sP:sP+sR;
    string nS = (sP < sS)?sP+sS:sS+sP;
    sR = nR; sP = nP; sS = nS;
    
    int ok = 0;
    for(int r=0;r<=R && r<=S;r++) {
      int s = S - r;
      int p = R - r;
      if(p>P) continue;
      if(r+p+s != (1<<n)) continue;
      R = r; P = p; S = s;
      ok = 1;
      break;
    }
    if(!ok) {
      printf("Case #%d: IMPOSSIBLE\n",t);
      return;
    }
  }
  if(R == 1) printf("Case #%d: %s\n",t,sR.c_str());
  if(P == 1) printf("Case #%d: %s\n",t,sP.c_str());
  if(S == 1) printf("Case #%d: %s\n",t,sS.c_str());
}

int main() {
  int t,T;
  scanf("%d",&T);
  for(t=1;t<=T;t++) solve(t);
  return 0;
}