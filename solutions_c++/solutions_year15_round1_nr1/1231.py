#include <bits/stdc++.h>
using namespace std;
#define all(c) (c).begin(),(c).end()
#define rrep(i,n) for(int i=(int)(n)-1;i>=0;i--)
#define REP(i,m,n) for(int i=(int)(m);i<(int)(n);i++)
#define rep(i,n) REP(i,0,n)
#define iter(c) __typeof((c).begin())
#define tr(it,c) for(iter(c) it=(c).begin();it!=(c).end();it++)
#define pb(a) push_back(a)
#define pr(a) cout<<(a)<<endl
#define PR(a,b) cout<<(a)<<" "<<(b)<<endl
#define R cin>>
#define F first
#define S second
#define ll long long
bool check(int n,int m,int x,int y){return x>=0&&x<n&&y>=0&&y<m;}
const ll MAX=1000000007,MAXL=1LL<<60,dx[4]={-1,0,1,0},dy[4]={0,1,0,-1};
typedef pair<int,int> P;

int main() {
  int T,t=1;
  R T;
  while(T--) {
    int n;
    R n;
    int a[n];
    rep(i,n) R a[i];
    int x=0,y=0,M=0;
    REP(i,1,n) {
      if(a[i-1]>a[i]) {
	x+=a[i-1]-a[i];
	M=max(M,a[i-1]-a[i]);
      }
    }
    REP(i,1,n) {
      y+=max(min(M,a[i-1]),a[i-1]-a[i]);
    }
    cout << "Case #" << t++ << ": ";
    PR(x,y);
  }
  return 0;
}
