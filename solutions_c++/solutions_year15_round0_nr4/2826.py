#include<bits/stdc++.h>
using namespace std;

#define SET(t,v) memset((t), (v), sizeof(t))
#define ALL(x) x.begin(), x.end()
#define UNIQUE(c) (c).resize( unique( ALL(c) ) - (c).begin() )
#define REP(i,n) for(ll i=0;i<n;i++)
#define ItREP(it,c) for(typeof((c).begin()) it = (c).begin(); it!= (c).end(); it++)
#define IREP(in,i,n) for(ll i=in;i<n;i++)
#define IN(a,b) ( (b).find(a) != (b).end())
#define PB push_back
#define FILL(a,v) memset(a, v, sizeof a)
#define MP make_pair

typedef long long ll;
typedef long double LD;
typedef pair<int,int> pii;

#define NDEBUG

#ifdef DEBUG
#define dbg(msg) msg
#define dbgp(msg) cout << msg << endl;
#define var(v) cout << #v << " = " << v << endl;
#else
#define dbg(msg) //msg
#define dbgp(msg) //cout << msg << endl;
#define var(v) //cout << #v << " = " << v << endl;
#endif

using namespace std;

int solve(){
  int X,R,C;
  cin >> X >> R >> C;
  if(X == 1) return true;
  if(C > R){
    swap(C,R);
  }

  if(R == 4){
    if(C == 4){
      if(X == 4) return true;
      if(X == 3) return false;
      if(X == 2) return true;
    }
    if(C == 3){
      if(X == 4) return true;
      if(X == 3) return true;
      if(X == 2) return true;
    }
    if(C == 2){
      if(X == 4) return false;
      if(X == 3) return false;
      if(X == 2) return true;
    }
    if(C == 1){
      if(X == 4) return false;
      if(X == 3) return false;
      if(X == 2) return true;
    }
  }


  if(R == 3){
    if(C == 3){
      if(X == 4) return false;
      if(X == 3) return true;
      if(X == 2) return false;
    }
    if(C == 2){
      if(X == 4) return false;
      if(X == 3) return true;
      if(X == 2) return true;
    }
    if(C == 1){
      if(X == 4) return false;
      if(X == 3) return false;
      if(X == 2) return false;
    }
  }

  if(R == 2){
    if(C == 2){
      if(X == 4) return false;
      if(X == 3) return false;
      if(X == 2) return true;
    }
    if(C == 1){
      return X == 2;
    }
  }

  if(R == 1){
    return false;
  }


}

int main(int argv, char** argc){
  cin.sync_with_stdio(0);

  int T;
  cin >> T;

  REP(i,T){
    if(solve()){
      printf("Case #%d: GABRIEL\n",i+1);
    }else{
      printf("Case #%d: RICHARD\n",i+1);
    }
  }


  

  return 0;
}

