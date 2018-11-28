#include<bits/stdc++.h>
using namespace std;
#define SI(x)      scanf("%d", &(x))
#define SII(x,y)   scanf("%d%d",&(x), &(y))
#define SS(x) 	   scanf("%s", &(x))
#define SF(x) 	   scanf("%f", &(x))
#define SFF(x,y)   scanf("%f%f",&(x),&(y))
#define REP(i,n)   for(int i=0; i<(n); i++)
#define FOR(i,a,b) for(int i=(a); i<=(b); i++)
#define SZ(x) ((int)(x).size())
#define MP make_pair
#define PB push_back
#define MINS(x,y,z) min((x), min((y), (z)))
#define MAXS(x,y,z) max((x), max((y), (z)))
#define MOD 1e9+7
#define INF  INT_MAX
#define NINF INT_MIN
#define F first  
#define S second 

typedef long long ll;
typedef vector<int> VI;
typedef vector<ll> VL;
typedef pair<int,int> PII;
typedef pair<ll, ll> PLL;

int main() {
      int t;
      SI(t);
      int n;
      string str;
      FOR(i,1,t) {
	    SI(n);
	    cin >> str;
	    int ans = 0 ;
	    int cur = str[0]-'0';
	    for(int j=1;j<str.size();j++) {
		  if( str[j] > '0' && cur < j ) {
			int nw = (j-cur);
			ans += nw;
			cur += nw;
		  }
		  cur += str[j]-'0';
		  //cout << "here : " << ans << ", j = " << j << endl;
	    }
	    cout << "Case #" << i << ": " << ans << endl;
      }
      return 0;
}

