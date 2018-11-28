
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
int cs;
int main() {
  freopen("111.in","r",stdin);
  freopen("333.out","w",stdout);
	int t;
	sci(t);
	while(t--){
	  deque<char> q;
	  string s;
	  cin >> s;
	  q.push_front(s[0]);
	  for(int i=1;i<s.size();i++){
	  	char last = q.front();
	  	if(s[i]>=last){
	  		q.push_front(s[i]);
	  	}
	  	else {
	  		q.push_back(s[i]);
	  	}
		last = q.front();
	  }
	  printf("Case #%d: ",++cs);
	  while(!q.empty()){
	  	cout<<q.front();
		q.pop_front();
	  }
	  nl;
	}
}
