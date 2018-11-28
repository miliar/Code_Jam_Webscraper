#include <bits/stdc++.h>
 
using namespace std;
 
#define INF 1000000007
#define MAX 100010
#define ROOT 100
#define BIG 1010
#define EPS 1e-6
const double pi = 2*acos(0) ;
 
typedef long long ll;
typedef vector<int> vi;
typedef vector<vi> vvi; 
typedef pair<int,int> ii;
typedef vector<ii> vii;
typedef pair<ii,ii> pii;
 
#define set0(a) memset(a,0,sizeof(a));
#define setminus1(a) memset(a,-1,sizeof(a)); 
#define all(x) x.begin(), x.end()
#define tr(x,it) for(auto it = x.begin(); it!=x.end(); ++it)
#define rtr(x,it) for(auto it = x.rbegin(); it!=x.rend(); ++it)
#define sz(a) int((a).size()) 
#define pb push_back 
#define mp make_pair
#define F first
#define S second
#define FOR(i,a,b) for(int i = a; i<=b; ++i)
#define NFOR(i,a,b) for(int i = a; i>=b; --i)
#define fast ios_base::sync_with_stdio(false);cin.tie(0);cout.tie(0)
void solve(){
    string s;
    cin>>s;
    int n= sz(s);
    if(n==1){
      if(s[0]=='+')cout<<0<<"\n";
      else cout<<1<<"\n";
      return;
    }
    int k;
    if(s[0]=='-')k=1;
    else k=0;
    FOR(i,1,n-1){
      if(s[i]=='-'&&s[i-1]=='+')++k;
    }

    if(s[0]=='-')cout<<2*k-1<<"\n";
    else cout<<2*k<<"\n";

}
int main(){
  clock_t tm=clock();
  fast;
  int t=1;
  cin>>t;
  FOR(_t,1,t){
  	cout<<"Case #"<<_t<<": ";solve();
  }	
  tm=clock()-tm;
  cerr<<(float)(tm)/CLOCKS_PER_SEC<<"\n";
  return 0;
} 