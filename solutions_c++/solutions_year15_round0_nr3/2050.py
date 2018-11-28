#include <bits/stdc++.h>

#define FOR(i,a,b) for(int i=(a);i<(b);++i)
#define FORD(i, a, b) for(int i = (a); i >= (b); --i)
#define VAR(v, i) __typeof(i) v=(i)
#define FORE(i, c) for(VAR(i, (c).begin()); i != (c).end(); ++i)
#define all(v) (v).begin(),(v).end()

#define VI vector<int>
#define PII pair<int,int>
#define st first
#define nd second
#define mp make_pair
#define pb push_back
#define lint long long int

#define debug(x) {cerr <<#x <<" = " <<x <<endl; }
#define debug2(x,y) {cerr <<#x <<" = " <<x << ", "<<#y<<" = "<< y <<endl; } 
#define debug3(x,y,z) {cerr <<#x <<" = " <<x << ", "<<#y<<" = "<< y << ", " << #z << " = " << z <<endl; } 
#define debugv(x) {{cerr <<#x <<" = "; FORE(itt, (x)) cerr <<*itt <<", "; cerr <<endl; }}
#define debugt(t,n) {{cerr <<#t <<" = "; FOR(it,0,(n)) cerr <<t[it] <<", "; cerr <<endl; }}

#define make( x) int (x); scanf("%d",&(x));
#define make2( x, y) int (x), (y); scanf("%d%d",&(x),&(y));
#define make3(x, y, z) int (x), (y), (z); scanf("%d%d%d",&(x),&(y),&(z));
#define make4(x, y, z, t) int (x), (y), (z), (t); scanf("%d%d%d%d",&(x),&(y),&(z),&(t));
#define makev(v,n) VI (v); FOR(i,0,(n)) { make(a); (v).pb(a);} 
#define IOS ios_base::sync_with_stdio(0)
#define HEAP priority_queue

#define read( x) scanf("%d",&(x));
#define read2( x, y) scanf("%d%d",&(x),&(y));
#define read3(x, y, z) scanf("%d%d%d",&(x),&(y),&(z));
#define read4(x, y, z, t) scanf("%d%d%d%d",&(x),&(y),&(z),&(t));
#define readv(v,n) FOR(i,0,(n)) { make(a); (v).pb(a);}

using namespace std;

#define max_n 100005

int q[8][8];
int pref[max_n];
int suf[max_n];
char s[max_n];

int qq[4][4]={{0,1,2,3},{1,4,3,6},{2,7,4,1},{3,2,5,4}};

void init(){
  FOR(i,0,4) FOR(j,0,4) q[i][j] = qq[i][j];
  FOR(i,4,8) FOR(j,4,8) q[i][j] = qq[i-4][j-4];
  FOR(i,0,4) FOR(j,4,8) q[i][j] = ((qq[i][j-4])+4)%8;
  FOR(i,4,8) FOR(j,0,4) q[i][j] = ((qq[i-4][j])+4)%8;
}

int dupa(char c){
  if(c=='i') return 1;
  if(c=='j') return 2;
  if(c=='k') return 3;
}

void solve(){
  //FOR(i,0,8) debugt(q[i],8);
  make2(l,k);
  scanf("%s",s);
  pref[0] = dupa(s[0]);
  suf[l-1] = dupa(s[l-1]);
  FOR(i,1,l) pref[i] = q[pref[i-1]][dupa(s[i])];
  FORD(i,l-2,0) suf[i] = q[dupa(s[i])][suf[i+1]];
//  debugt(pref,l);
//  debugt(suf,l);
  int u = 0;
  FOR(i,0,k%4){
//    debug2(u,pref[l-1]);
    u = q[pref[l-1]][u];
    //debug(u);
  }
  if(u!=4){
    printf("NO\n");
    return;
  }
  int mini = 1e9;
  int cyc = 0;
  FOR(j,0,4){
    FOR(i,0,l){
      int act = q[cyc][pref[i]];
      if(act==1) mini = min(mini,j*l+i);
    }
    cyc = q[cyc][pref[l-1]];
  }
  int mini2 = 1e9;
  cyc = 0;
  FOR(j,0,4){
    FORD(i,l-1,0){
      int act = q[suf[i]][cyc];
      if(act==3) mini2 = min(j*l+(l-1-i),mini2);
    }
    cyc = q[cyc][suf[0]];
  }
  //debug2(mini,mini2);
  if(mini ==1e9 || mini2 == 1e9){
    printf("NO\n"); return;
  }
  if(mini+1+mini2+1<l*1LL*k){
    printf("YES\n");
  }
  else printf("NO\n");

}

int main(){
  init();
  make(z);
  FOR(tt,1,z+1){
    printf("Case #%d: ",tt);
    solve();
  }
}
