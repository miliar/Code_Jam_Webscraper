
#include <bits/stdc++.h>
using namespace std;
#define MOD 1000000007
#define pii pair<int, int>
#define pll pair<long long, long long>
#define vi  vector<int>
#define pb  push_back
#define mp  make_pair
#define ALL(x) x.begin(),x.end()
#define M(a,x) memset(a,x,sizeof(a))
#define sci(x) scanf("%d",&x);
#define scl(x) scanf("%lld",&x);
#define scs(x) scanf("%s",x);
#define print(x) printf("%d",x);
#define nl printf("\n")
#define fr first
#define se second
#define printl(x) printf("%lld",x)
#define F(i,a,n) for(int i=a;i<n;i++)
#define INF 100000000000000000LL
#define LL long long

int main() {
  freopen("lg2.in","r",stdin);
  freopen("lgo2.out","w",stdout);
  int t;
  sci(t);
  int cs = 0;
  while(t--) {
    string s;
    cin >> s;
    int ans = 0;
    int n = s.size();
    while(1) {
      int pos = -1;
      for(int i=n-1;i>=0;i--) {
	if(s[i] == '-') {
	  pos = i;
	  break;
	}
      }
      if(pos == -1) {
	break;
      }
      ans++;
      string temp = "";
      for(int i=0;i<=pos;i++) {
	if(s[i] == '+') {
	  temp[i] = '-';
	}
	else {
	  temp[i] = '+';
	}
      }
      reverse(temp.begin(),temp.end());
      for(int i=0;i<=pos;i++) {
	s[i] = temp[i];
      }
    }
    printf("Case #%d: %d\n",++cs,ans);
  }
}
