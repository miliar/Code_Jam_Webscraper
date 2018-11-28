#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef vector<ll> vl;
typedef complex<double> P;
typedef pair<int,int> pii;
#define REP(i,n) for(ll i=0;i<n;++i)
#define REPR(i,n) for(ll i=1;i<n;++i)
#define FOR(i,a,b) for(ll i=a;i<b;++i)

#define DEBUG(x) cout<<#x<<": "<<x<<endl
#define DEBUG_VEC(v) cout<<#v<<":";REP(i,v.size())cout<<" "<<v[i];cout<<endl
#define ALL(a) (a).begin(),(a).end()

#define MOD (ll)(1e9+7)
#define ADD(a,b) a=((a)+(b))%MOD
#define FIX(a) ((a)%MOD+MOD)%MOD

// 捨てます

int dx[4] = {1,0,-1,0};
int dy[4] = {0,1,0,-1};

bool deb;

bool check(int r,int c,int mp[30][30], pii p[30]){
  // 0 : \, 1 : /
  REP(i,r+c){
    int a = p[i].first, b = p[i].second;
    if(deb){
      DEBUG(a);
      DEBUG(b);
    }
    int x=0,y=0;
    int dir = 0;
    if(a<=c){
      x = a, y = 0;
      dir = 1;
    }else if(a<=r+c){
      x = c+1, y = a-c;
      dir = 2;
    }else if(a<=r+2*c){
      x = c+1-(a-(r+c)), y = r+1;
      dir = 3;
    }else{
      x = 0, y = r+1-(a-(r+2*c));
      dir = 0;
    }
    int tox=0,toy=0;
    if(b<=c){
      tox = b, toy = 0;
    }else if(b<=r+c){
      tox = c+1, toy = b-c;
    }else if(b<=r+2*c){
      tox = c+1-(b-(r+c)), toy = r+1;
    }else{
      tox = 0, toy = r+1-(b-(r+2*c));
    }
    if(deb){
      DEBUG(x);
      DEBUG(y);
      DEBUG(tox);
      DEBUG(toy);
    }

    bool flag = true;
    while(true){
      x += dx[dir];
      y += dy[dir];
      if(deb){
        DEBUG(x);
        DEBUG(y);
      }
      if(x==tox && y==toy)break;
      else if(x<=0||y<=0||x>c||y>r){
        flag = false;
        break;
      }
      if(dir%2==1){
        if(mp[y-1][x-1]==1)dir=(dir+1)%4;
        else dir=(dir-1+4)%4;
      }else{
        if(mp[y-1][x-1]==1)dir=(dir-1+4)%4;
        else dir=(dir+1)%4;
      }
    }
    if(!flag)return false;
  }
  return true;
}

void solve(){
  int r,c;
  scanf("%d%d",&r,&c);
  pii p[30];
  REP(i,r+c){
    int x,y;
    scanf("%d%d",&x,&y);
    p[i] = pii(x,y);
  }
  REP(msk,1<<(r*c)){
    // create map
    deb=false;
    int mp[30][30];
    REP(i,r)REP(j,c){
      mp[i][j] = (msk>>(i*c+j))&1;
    }
    if(deb){
      REP(i,r){
        REP(j,c)printf("%c",mp[i][j]==0?'\\':'/');
        printf("\n");
      }
    }
    if(check(r,c,mp,p)){
      // print map
      REP(i,r){
        REP(j,c)printf("%c",mp[i][j]==0?'\\':'/');
        printf("\n");
      }
      return;
    }
  }
  puts("IMPOSSIBLE");
  return;
}

int main(){
  int t;
  scanf("%d",&t);
  REP(i,t){
    printf("Case #%d:\n",i+1);
    solve();
  }
  return 0;
}
