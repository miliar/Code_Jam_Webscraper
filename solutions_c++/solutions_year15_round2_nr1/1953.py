#include<bits/stdc++.h>
using namespace std;
#define IO ios_base::sync_with_stdio(false);cin.tie(NULL);

#define endl '\n'
#define D(x) cout << #x << " = " << (x) << endl;
#define rep(i,a,b) for(int (i)=(a);(i)<(b);(i)++)
#define repd(i,a,b) for(int (i)=(b)-1;(i)>=(a);(i)--)
#define REP(i,n) rep(i,0,n)
#define REPD(i,n) repd(i,0,n)
#define pb push_back
#define mp make_pair
#define countbits(x) __builtin_popcount(x)
#define countbitslld(x) __builtin_popcountll(x)

typedef long long int lld;
typedef vector<int> vi;
typedef vector<lld> vlld;
typedef vector<string> vs;
typedef pair<int,int> pii;
typedef vector<pii> vpii;

const int maxn = 10000005;

int rev(int n){
  int x = 0;
  while(n){
    int d = n % 10;
    n /= 10;
    x = 10 * x + d;
  }
  return x;
}

int main(){ IO;
  vi v(maxn);
  v[1] = 1;
  queue<int> Q;
  Q.push(1);
  while(!Q.empty()){
    int cur = Q.front(); Q.pop();
    int cnt = v[cur] + 1;
    {
      int next = cur + 1;
      if(next < maxn and !v[next]){
	v[next] = cnt;
	Q.push(next);
      }
    }
    {
      int next = rev(cur);
      if(next < maxn and !v[next]){
	v[next] = cnt;
	Q.push(next);
      }
    }
  }


  int t;
  cin >> t;

  rep(ncase,1,t+1){
    cout << "Case #" << ncase << ": ";

    int n;
    cin >> n;
    cout << v[n] << endl;
  }

  return 0;
}
