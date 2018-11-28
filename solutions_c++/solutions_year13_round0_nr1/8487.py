#include <fstream>
#include <queue>
using namespace std; ifstream f("A-small-attempt0.in"); ofstream g("output");
char v[6][6];
queue <int> lx,cx,lo,co;

int main() { int N,q;
  f>>N;
  for (q=1;q<=N;q++) { char k,s; bool okx=0,oko=0,okp=0,okt=0; int i,j,x,y,nr=1,xt,yt;
    for (i=1;i<=4;i++) for (j=1;j<=4;j++) {f>>k; v[i][j]=k; if (k=='X') {lx.push(i); cx.push(j);} else {if (k=='O') {lo.push(i); co.push(j);} else {if (k=='.') {okp=1;} else {if ((k=='T') && ((i==1 && j>=1) || (i>1 && j==1))) {okt=1; xt=i; yt=j;};};};};};
    while (lx.empty()==false) { i=lx.front(); j=cx.front(); lx.pop(); cx.pop();
      if (i==1 && j==1) {x=i; y=j; while (v[x][y+1]=='X' || v[x][y+1]=='T') {nr++; if (nr==4) {okx=1; break;}; y++;}; nr=1;
                         x=i; y=j; while (v[x+1][y]=='X' || v[x+1][y]=='T') {nr++; if (nr==4) {okx=1; break;}; x++;}; nr=1;
                         while (v[i+1][j+1]=='X' || v[i+1][j+1]=='T') {nr++; if (nr==4) {okx=1; break;}; i++; j++;}; nr=1;};
      if (i==1 && j>1) {while (v[i+1][j]=='X' || v[i+1][j]=='T') {nr++; if (nr==4) {okx=1; break;}; i++;}; nr=1;};
      if (i>1 && j==1) {if (i==4) {x=i; y=j; while (v[x-1][y+1]=='X' || v[x-1][y+1]=='T') {nr++; if (nr==4) {okx=1; break;}; x--; y++;}; nr=1;
                                 while (v[i][j+1]=='X' || v[i][j+1]=='T') {nr++; if (nr==4) {okx=1; break;}; j++;}; nr=1;}
                       else {while (v[i][j+1]=='X' || v[i][j+1]=='T') {nr++; if (nr==4) {okx=1; break;}; j++;}; nr=1;};};};
    nr=1;
    while (lo.empty()==false) { i=lo.front(); j=co.front(); lo.pop(); co.pop();
      if (i==1 && j==1) {x=i; y=j; while (v[x][y+1]=='O' || v[x][y+1]=='T') {nr++; if (nr==4) {oko=1; break;}; y++;}; nr=1;
                         x=i; y=j; while (v[x+1][y]=='O' || v[x+1][y]=='T') {nr++; if (nr==4) {oko=1; break;}; x++;}; nr=1;
                         while (v[i+1][j+1]=='O' || v[i+1][j+1]=='T') {nr++; if (nr==4) {oko=1; break;}; i++; j++;}; nr=1;};
      if (i==1 && j>1) {while (v[i+1][j]=='O' || v[i+1][j]=='T') {nr++; if (nr==4) {oko=1; break;}; i++;}; nr=1;};
      if (i>1 && j==1) {if (i==4) {x=i; y=j; while (v[x-1][y+1]=='O' || v[x-1][y+1]=='T') {nr++; if (nr==4) {oko=1; break;}; x--; y++;}; nr=1;
                                 while (v[i][j+1]=='O' || v[i][j+1]=='T') {nr++; if (nr==4) {oko=1; break;}; j++;}; nr=1;}
                       else {while (v[i][j+1]=='O' || v[i][j+1]=='T') {nr++; if (nr==4) {oko=1; break;}; j++;}; nr=1;};};};
    nr=1;
    if (okt==1) {if (xt==1 && yt==1) {if (v[xt+1][yt+1]=='X' || v[xt+1][yt+1]=='O') {i=x; j=yt; nr++; s=v[i+1][j+1]; i++; j++; while (v[i+1][j+1]==s) {nr++; if (nr==4) {if (s=='X') {okx=1;} else {oko=1;}; break;}; i++; j++;};}; nr=1;
                                      if (v[xt][yt+1]=='X' || v[xt][yt+1]=='O') {i=xt; j=yt; nr++; s=v[i][j+1]; j++; while (v[i][j+1]==s) {nr++; if (nr==4) {if (s=='X') {okx=1;} else {oko=1;}; break;} j++;};}; nr=1;
                                      if (v[xt+1][yt]=='X' || v[xt+1][yt]=='O') {nr++; s=v[xt+1][yt]; xt++; while (v[xt+1][yt]==s) {nr++; if (nr==4) {if (s=='X') {okx=1;} else {oko=1;}; break;}; xt++;};};}
                 else {if (xt==1) {if (v[xt+1][yt]=='X' || v[xt+1][yt]=='O') {nr++; s=v[xt+1][yt]; xt++; while (v[xt+1][yt]==s) {nr++; if (nr==4) {if (s=='X') {okx=1;} else {oko=1;}; break;}; xt++;};};}
                       else {if (yt==1) {if (xt==4) {if (v[xt-1][yt+1]=='X' || v[xt-1][yt+1]=='O') {i=xt; j=yt; nr++; s=v[i-1][j+1]; i--; j++; while (v[i-1][j+1]==s) {nr++; if (nr==4) {if (s=='X') {okx=1;} else {oko=1;}; break;}; i--; j++;};}; nr=1;
                                                     if (v[xt][yt+1]=='X' || v[xt][yt+1]=='O') {nr++; s=v[xt][yt+1]; yt++; while (v[xt][yt+1]==s) {nr++; if (nr==4) {if (s=='X') {okx=1;} else {oko=1;};}; yt++;};};}
                                         else {if (v[xt][yt+1]=='X' || v[xt][yt+1]=='O') {nr++; s=v[xt][yt+1]; yt++; while (v[xt][yt+1]==s) {nr++; if (nr==4) {if (s=='X') {okx=1;} else {oko=1;}; break;}; yt++;};};};};};};};
    g<<"Case #"<<q<<": ";
    if (okx==1 && oko==0) {g<<"X won"<<'\n';}
    else {if (okx==0 && oko==1) {g<<"O won"<<'\n';}
          else {if ((okx==1 && oko==1) || (okp==0)) {g<<"Draw"<<'\n';}
                else {if (okp==1) {g<<"Game has not completed"<<'\n';};};};};};
  return 0;}
