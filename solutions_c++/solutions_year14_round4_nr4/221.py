#include<bits/stdc++.h>
#define rep(i,n) for(int i=0;i<(int)(n);i++)
#define rrep(i,n) for(int i=(int)(n)-1;i>=0;i--)
#define all(a) (a).begin(),(a).end()
#define INIT(a) memset((a),0,sizeof(a))
#define fs first
#define sc second
#define pb push_back
#define sz size() 
using namespace std;
typedef long long ll;
typedef double D;
typedef pair<int,int> pii;
typedef vector<int> vi;
typedef vector<string> vs;

const static ll INF = 1e15;
const static D EPS = 1e-8;
const static ll mod = 1e9+7;

int main(){
  int testcase;

  cin >> testcase;
  for(int casenum=1;casenum<=testcase;casenum++){
    int m,n;
    cin >> m >> n;
    string s[1000];
    rep(i,m)cin >> s[i];

    ll nodes = 0, ways = 0;
    rep(bit,1<<(2*m)){
      vs server[100];
      rep(i,m){
	int id = (bit>>(2*i))&3;
	server[id].pb(s[i]);
      }

      bool f = true;
      int sum = 0;
      rep(i,n){
	if(server[i].sz == 0u)f = false;
	sum += server[i].sz;
      }
      if(!f || sum!=m)continue;

      int num = 0;
      rep(i,n){
	vs prefix;
	rep(j,server[i].sz){
	  string tmp = server[i][j];
	  rep(k,tmp.sz){
	    prefix.pb(tmp.substr(0,k+1));
	  }
	}
	sort(all(prefix));
	prefix.erase(unique(all(prefix)),prefix.end());
	num += prefix.sz + 1;
      }

      if(nodes < num){
	nodes = num; ways = 1;
      }else if(nodes == num){
	ways++;
	if(ways==mod)ways = 0;
      }
    }
   
    cout << "Case #" << casenum << ": " << nodes << " " << ways << endl;
  }
}
