#include <bits/stdc++.h>

#define rep(i,a,b) for(int i=(a);i<(b);i++)
#define INF 2147483647
#define pi acos(-1.0)
#define EPS 1e-9
#define INF_LONG 9223372036854775807LL
#define Set(a, s) memset (a, s, sizeof (a))
#define trace(s,v) printf("%s => %d\n",s,v)
#define SSTR( x ) dynamic_cast< std::ostringstream & > (( std::ostringstream() << std::dec << x )).str()
#define debug(t,n) cout<<">"<<(t)<<"="<<(n)<<"\n";
#define b(x) cout<<(x)<<endl;

using namespace std;

typedef long long ll;
typedef pair<int,int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;

int tc, n;
int nmenos;

string compressing(string s){
	string y = "";
	char cur = s[0];
	rep(i,1,n){
		if(s[i]!=cur){
			y+=cur;
			if(cur == '-') nmenos++;
			cur = s[i];
		}
	}
	y+=cur;
	if(cur == '-') nmenos++;
	return y;
}

int main() {
  ios::sync_with_stdio(false);cin.tie(0);cout.tie(0);

  cin>>tc;
  string s;
  int k = 1;
  while(tc--){
	  cin>>s;
	  n = s.length();
	  nmenos = 0;
	  s = compressing(s);
	  nmenos*=2;
	  if(s[0] == '-') nmenos--;
	  cout<<"Case #"<<(k++)<<": "<<nmenos<<"\n";
  }
  
  return 0;
}
