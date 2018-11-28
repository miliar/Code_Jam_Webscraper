#include<bits/stdc++.h>
using namespace std;

#define CLR(a,x) memset(a,x,sizeof(a))
#define PB push_back
#define INF 1000000000
#define MOD 1000000007
#define MP make_pair
#define tr(container , it) for(typeof(container.begin()) it=container.begin() ; it!=container.end() ; it++)
#define FOR(i,a,b) for(i=a;i<b;i++)
#define REP(i,a) FOR(i,0,a)
#define LL long long
#define VI vector < int >
#define PII pair < int , int >

int avail[1024];
int main() {
  int T;
  cin>>T;
  int kase=1;
  while(T--) {
    int D;
    cin>>D;
    for(int i=0;i<D;i++) {
      cin>>avail[i];
    }
    int ans = 1000;
    for(int i=1;i<=1000;i++) {
      int cur = i;
      for(int j=0;j<D;j++) {
        cur += (avail[j]+i-1)/i - 1;
      }
      ans = min(cur, ans);
    }
    cout<<"Case #"<<kase++<<": "<<ans<<endl;
  }
  return 0;
}
