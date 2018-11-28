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

int setter, n, num;

void gosetter(int r){
	int d;
	while(r > 0){
		d = r%10;
		r = r/10;
		setter|=(1<<d);
	}
}

int main() {
  ios::sync_with_stdio(false);cin.tie(0);cout.tie(0);

  int tc, k;
  cin>>tc;
  k = 1;
  while(tc--){
	  cin>>n;
	  if(n == 0){
		  cout<<"Case #"<<(k++)<<": INSOMNIA\n";
		  continue;
	  }
	  setter = 0;
	  num = n;
	  gosetter(num);
	  while( setter != ((1<<10)-1) ){
		  num+=n;
		  gosetter(num);
	  }
	  cout<<"Case #"<<(k++)<<": "<<num<<"\n";
  }
  
  return 0;
}
