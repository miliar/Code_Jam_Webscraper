#include<cstring>
#include<cstdio>
#include<algorithm>
#include<cmath>
#include<vector>
#include<numeric>
#include<map>
#include<set>
#include<cstdlib>
#include<string>
#include<cassert>
#include<iostream>
using namespace std;
typedef vector<int> vi;
typedef long long int64;
#define FOR(i,n)for(int i=0;i<(int)(n);i++)
void solve(){
  int n,m,t[210][210];
  scanf("%d %d",&n,&m);
  FOR(i,n)FOR(j,m)scanf("%d",&t[i][j]);
  bool ok=true;
  FOR(i,n)FOR(j,m)if(t[i][j]<100){
    bool found=true;
    FOR(k,m)found&=t[i][k]<=t[i][j];
    if(found)continue;
    found=true;
    FOR(k,n)found&=t[k][j]<=t[i][j];
    if(found)continue;
    ok=false;
  }
  puts(ok?"YES":"NO");
}
main(){
  char in[100],out[100],*pos;
  strcpy(in,__FILE__);
  strcpy(out,__FILE__);
  pos=in;
  while(*pos!='.')pos++;
  strcpy(pos,".in");
  pos=out;
  while(*pos!='.')pos++;
  strcpy(pos,".out");
  freopen(in,"r",stdin);
  freopen(out,"w",stdout);
  int t;
  scanf("%d",&t);
  for(int tt=1;tt<=t;tt++){
    fprintf(stderr,"processing case %d\n",tt);
    printf("Case #%d: ",tt);
    solve();
    fflush(stdout);
  }
  freopen(out,"r",stdin);
  char c;while((c=getc(stdin))!=EOF)putc(c,stderr);
}

