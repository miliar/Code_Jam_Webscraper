#include <bits/stdc++.h>
using namespace std;
typedef pair<int,int> pii;
const int M=10000;
int t,tt,n,i,j,jj,nj,k,kk,pa,pb,pc,qa,qb,qc,a[3][3];
string sa,sb,sc;
map<pii, string> m[14][3];
vector<pii> f[14][3];
pii p,q;
int main() {
  freopen("Al.in","r",stdin);
  freopen("Al.out","w",stdout);
  a[0][1]=0;
  a[1][2]=1;
  a[0][2]=2;
  p=make_pair(1,0); f[0][0].push_back(p); m[0][0][p]="P";
  p=make_pair(0,M); f[0][1].push_back(p); m[0][1][p]="R";
  p=make_pair(0,1); f[0][2].push_back(p); m[0][2][p]="S";
  for (i=0; i<12; i++) for (j=0; j<3; j++) for (jj=0; jj<f[i][j].size(); jj++) {
    p=f[i][j][jj];
    sa=m[i][j][p];
    pa=p.first;
    pb=p.second/M;
    pc=p.second%M;
    for (k=j+1; k<3; k++) for (kk=0; kk<f[i][k].size(); kk++) {
      p=f[i][k][kk];
      sb=m[i][k][p];
      qa=p.first;
      qb=p.second/M;
      qc=p.second%M;
      q=make_pair(pa+qa,(pb+qb)*M+pc+qc);
      sc=min(sa+sb,sb+sa);
      nj=a[j][k];
      if (m[i+1][nj].count(q)) {
        m[i+1][nj][q]=min(m[i+1][nj][q],sc);
      } else {
        f[i+1][nj].push_back(q);
        m[i+1][nj][q]=sc;
      }
    }
  }
  scanf("%d",&tt);
  for (t=1; t<=tt; t++) {
    scanf("%d%d%d%d",&n,&pb,&pa,&pc);
    sc="Z";
    p=make_pair(pa,pb*M+pc);
    for (i=0; i<3; i++) if (m[n][i].count(p)) sc=min(sc,m[n][i][p]);
    printf("Case #%d: %s\n",t,(sc=="Z")?"IMPOSSIBLE":sc.c_str());
  }
  return 0;
}
