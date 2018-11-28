
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

const int N = 1e5+5;
vector<LL> sol,ans;
string  v(LL num) {
  string temp = "";
  while(num) {
    temp+=(num%2+'0');
    num/=2;
  }
  reverse(temp.begin(),temp.end());
  return temp;
}
bool valid(LL num) {
  string temp = v(num);
  int rem1 = 0;
  int rem2 = 0;
  int rem3  = 0;
  int rem4 = 0;
  int rem5 = 0;
  for(int i=0;i<temp.size();i++) {
    rem1=rem1*2+(temp[i]-'0');
    rem1%=3;
    rem2=rem2*4+(temp[i]-'0');
    rem2%=5;
    rem3=rem3*6+(temp[i]-'0');
    rem3%=7;
    rem4=rem4*8+(temp[i]-'0');
    rem4%=3;
    rem5=rem5*10+(temp[i]-'0');
    rem5%=11;
  }
  if(rem1 || rem2 || rem3 || rem4 || rem5)
    return false;
  return true;
}
int cs = 0;
int main() {
  freopen("Big2.in","r",stdin);
  freopen("Lar2.out","w",stdout);
  int t;sci(t);
  while(t--) {
    int n,m;
    cin >> n >> m;
    ans.pb(3);
    ans.pb(2);
    ans.pb(5);
    ans.pb(2);
    ans.pb(7);
    ans.pb(2);
    ans.pb(3);
    ans.pb(2);
    ans.pb(11);
    LL beg = (1LL<<(n-1))+1;
    LL end = (1LL<<(n))-1;
    for(LL i=beg;i<=end;i+=2) {
      if(valid(i)) {
	sol.pb(i);
	if(sol.size()==m) {
	  break;
	}
      }
    }
    printf("Case #%d:\n",++cs);
    for(int i=0;i<sol.size();i++) {
      cout<<v(sol[i])<<" ";
      F(j,0,ans.size()) {
	cout<<ans[j]<<" ";
      }
      nl;
    }
  }
}
