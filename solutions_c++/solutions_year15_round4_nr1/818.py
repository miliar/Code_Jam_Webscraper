#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef pair<int,int> ii;
#define X first
#define Y second
#define REP(i,a) for(int i=0;i<a;++i)
#define REPP(i,a,b) for(int i=a;i<b;++i)
#define FILL(a,x) memset(a,x,sizeof(a))
#define	foreach( gg,itit )	for( typeof(gg.begin()) itit=gg.begin();itit!=gg.end();itit++ )
#define	mp make_pair
#define	pb push_back
#define sz(a) int((a).size())
#define	debug(ccc)	cout << #ccc << " = " << ccc << endl;
#define present(c,x) ((c).find(x) != (c).end())
const int mod = 1e9+7;

char s[105][105];
ii fa(int i,int j){
  if(s[i][j]=='^') return mp(-1,0);
  else if(s[i][j]=='>') return mp(0,1);
  else if(s[i][j]=='<') return mp(0,-1);
  else return mp(1,0);
}
int main(){
  int t,n,m;
  scanf("%d",&t);
  REP(l,t){
    scanf("%d %d",&n,&m);
    REP(i,n){
      scanf("%s",s[i]);
    }
    int ans=0,g=0;
    REP(i,n) REP(j,m) if(s[i][j]!='.'){
      int f=0;
      ii p=fa(i,j);
    //  printf("%d %d\n",i,j);
      ii q=mp(i+p.X,j+p.Y);
      while((q.X>=0&&q.X<n)&&(q.Y>=0&&q.Y<m)){
        if(s[q.X][q.Y]!='.') {  f=1; break;}
        q=mp(q.X+p.X,q.Y+p.Y);
      }
      if(f==1) continue;

      ii r=mp(1,0);
      if(r!=p){
        q=mp(i+r.X,j+r.Y);
        while((q.X>=0&&q.X<n)&&(q.Y>=0&&q.Y<m)){
          if(s[q.X][q.Y]!='.') {  f=1; break;}
          q=mp(q.X+r.X,q.Y+r.Y);
        }
      }
    //  printf("%d\n",f);
      r=mp(0,1);
      if(r!=p){
        q=mp(i+r.X,j+r.Y);
        while((q.X>=0&&q.X<n)&&(q.Y>=0&&q.Y<m)){
          if(s[q.X][q.Y]!='.') {  f=1; break;}
          q=mp(q.X+r.X,q.Y+r.Y);
        }
      }
    //  printf("%d\n",f);
      r=mp(0,-1);

      if(r!=p){
        q=mp(i+r.X,j+r.Y);
        while((q.X>=0&&q.X<n)&&(q.Y>=0&&q.Y<m)){
          if(s[q.X][q.Y]!='.') {  f=1; break;}
          q=mp(q.X+r.X,q.Y+r.Y);
        }
      }
      //printf("%d\n",f);
      r=mp(-1,0);
      if(r!=p){
        q=mp(i+r.X,j+r.Y);
        while((q.X>=0&&q.X<n)&&(q.Y>=0&&q.Y<m)){
          if(s[q.X][q.Y]!='.') {  f=1; break;}
          q=mp(q.X+r.X,q.Y+r.Y);
        }
      }
      //printf("%d\n",f);
      if(f==1) ans++;
      else g=1;
    }
    if(g==1) printf("Case #%d: IMPOSSIBLE\n",l+1);
    else printf("Case #%d: %d\n",l+1,ans);
  }
  return 0;
}
