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
bool g(int64 x){
  static char buf[100];
  sprintf(buf,"%lld",x);
  int n=strlen(buf);
  bool ok=true;
  FOR(i,n)ok&=buf[i]==buf[n-1-i];
//  cout<<x<<" "<<ok<<endl;
  return ok;
}
vector<int64> s;
void pre(){
  for(int64 y=1;y<11000000;y++)if(g(y)&&g(y*y))s.push_back(y*y);
}
int64 f(int64 x){
  int64 ans=0;
  for(int i=0;i<s.size();i++)ans+=s[i]<x;
  return ans;
}
void solve(){
  int64 A,B;
  scanf("%lld %lld",&A,&B);
  printf("%lld\n",f(B+1)-f(A));
}
main(){
  pre();
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

