#include <bits/stdc++.h>
using namespace std;
const int MX=20200;
int t,tt,n,num,ed,i,r,fi,fr,it,f[200200],pv[MX],pe[MX],q[MX],u[MX];
char s[200200];
string cur;
map<string,int> m;
vector<int> g[MX],e[MX];
void add() {
  int id=-1;
  if (m.count(cur)) id=m[cur]; else {
    m[cur]=id=num;
    num+=2;
  }
  g[i].push_back(id);    e[i].push_back(ed);    f[ed++]=1;
  g[id].push_back(i);    e[id].push_back(ed);   f[ed++]=0;
  g[id].push_back(id+1); e[id].push_back(ed);   f[ed++]=1;
  g[id+1].push_back(id); e[id+1].push_back(ed); f[ed++]=0;
  g[id+1].push_back(i);  e[id+1].push_back(ed); f[ed++]=1;
  g[i].push_back(id+1);  e[i].push_back(ed);    f[ed++]=0;    
  cur="";
}
bool path() {
  q[0]=fi=0; fr=1; u[0]=++it;
  while (fi<fr) {
    i=q[fi++];
    for (int j=0; j<g[i].size(); j++) {
      int k=g[i][j],edg=e[i][j];
      if (f[edg]>0 && u[k]!=it) {
        u[k]=it; pv[k]=i; pe[k]=edg; q[fr++]=k;
      }
    }
    if (u[1]==it) return true;
  }
  return false;
}
int main() {
  freopen("Cs.in","r",stdin);
  freopen("Cs.out","w",stdout);
  scanf("%d",&tt);
  for (t=1; t<=tt; t++) {
    scanf("%d",&n); gets(s);
    m.clear(); num=n; ed=0;
    for (i=0; i<n; i++) {
      gets(s);
      for (int j=0; s[j]; j++) if (s[j]==' ') add(); else cur+=s[j];
      add();
    }
    for (r=0; path(); r++) for (i=1; i!=0; i=pv[i]) {
      f[pe[i]]--;
      f[pe[i]^1]++;
    }
    printf("Case #%d: %d\n",t,r);
    fprintf(stderr,"Case #%d\n",t);
    for (i=0; i<num; i++) {
      g[i].clear();
      e[i].clear();
    }
  }
  return 0;
}
