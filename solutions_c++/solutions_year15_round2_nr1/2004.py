#include<bits/stdc++.h>
using namespace std;

#define SET(t,v) memset((t), (v), sizeof(t))
#define ALL(x) x.begin(), x.end()
#define UNIQUE(c) (c).resize( unique( ALL(c) ) - (c).begin() )
#define REP(i,n) for(ll i=0;i<n;i++)

#if __cplusplus > 199711L
#define ItREP(it,c) for(auto it = (c).begin(); it!= (c).end(); it++)
#else
#define ItREP(it,c) for(typeof((c).begin()) it = (c).begin(); it!= (c).end(); it++)
#endif

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

ll reverse(ll n){
  int digits[50];
  int length = 0;
  while(n>0){
    digits[length++] = n%10;
    n/=10;
  }

  reverse(digits,digits+length);
  ll newnum = 0;
  ll base = 1;
  REP(i,length){
    int cur = digits[i];
    newnum += cur*base;
    base*=10;
  }

  return newnum;
}

ll solve(){
  ll N;
  cin >> N;

  map<ll,ll> depth;
  queue<ll> qu;

  depth[1] = 1;
  qu.push(1);

  while(qu.size()){
    ll cur = qu.front();qu.pop();
    if(cur == N){
      return depth[cur];
    }

    ll next = cur+1;
    if(!IN(next,depth)){
      depth[next] = depth[cur]+1;
      qu.push(next);
    }
    
    next = reverse(cur);
    if(!IN(next,depth)){
      depth[next] = depth[cur]+1;
      qu.push(next);
    }
  }

  assert(false);
}

int main(int argv, char** argc){
  cin.sync_with_stdio(0);

  assert(reverse(10) == 1);
  assert(reverse(123) == 321);

  int T;
  cin >> T;
  REP(i,T){
    cout << "Case #" << i+1 << ": " << solve() << endl;
  }
  
  return 0;
}

