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
int lol[20];
void solve(){
    int n;
    cin>>n;
    if(n==0){
      cout<<"INSOMNIA\n";
      return;
    }
    int N=1;
    set0(lol);
    while(1){
      int temp=N*n;
      while(temp!=0){
        lol[temp%10]=1;
        temp/=10;
      }
      int flag=1;
      FOR(j,0,9){
        if(lol[j]!=1){flag=0;break;}
      }
      if(flag){
        break;
      }
      N++;
    }
    cout<<N*n<<"\n";

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