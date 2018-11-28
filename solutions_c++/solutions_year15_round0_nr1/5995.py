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


void solve(int d){
  int sm;
  cin >> sm;
  string test;
  cin >> test;

  int acount = 0;
  int count = 0;
  REP(i,test.size()){
    int cur = test[i]-'0';
    acount+=cur;
    if(acount < (i+1)){
      count+=i-acount+1;
      acount+=i-acount+1;
    }
  }

  cout << "Case #" << d << ": " << count << endl;
}

int main(int argv, char** argc){
  cin.sync_with_stdio(0);

  int T;
  cin >> T;

  REP(i,T){
    solve(i+1);
  }
  
  return 0;
}

