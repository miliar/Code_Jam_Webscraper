#include<bits/stdc++.h>
#define rep(i,n) for(int i=0;i<(int)(n);i++)
#define rrep(i,n) for(int i=(int)(n)-1;i>=0;i--)
#define all(a) (a).begin(),(a).end()
#define INIT(a) memset((a),0,sizeof(a))
#define chmin(a,b) ((a) = min((a),(b)))
#define chmax(a,b) ((a) = max((a),(b)))
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

const static int INF = 1e8;
const static D EPS = 1e-8;

int main(){
  map<char,int> dy,dx;
  dy['^'] = -1, dy['v'] = 1;
  dx['<'] = -1, dx['>'] = 1;

  int testcase;

  cin >> testcase;
  for(int casenum=1;casenum<=testcase;casenum++){
    int h,w;
    cin >> h >> w;
    vs g(h);
    rep(i,h)cin >> g[i];

    int res = 0, ok = 1;
    rep(i,h)rep(j,w){
      if(g[i][j] != '.'){
	int y = i, x = j, f = 0;
	for(;;){
	  y += dy[g[i][j]]; x += dx[g[i][j]];
	  if(y<0 || x<0 || y>=h || x>=w)break;

	  if(g[y][x] != '.'){
	    f = 1; break;
	  }
	}
	if(!f){
	  string dir = "^>v<";
	  rep(k,4){
	    y = i, x = j;
	    for(;;){
	      y += dy[dir[k]]; x += dx[dir[k]];
	      if(y<0 || x<0 || y>=h || x>=w)break;
	      
	      if(g[y][x] != '.'){
		f = 1; break;
	      }
	    }
	  }
	  if(!f)ok = 0;
	  else res++;
	}
      }
    }

    cout << "Case #" << casenum << ": ";
    if(ok)cout << res << endl;
    else cout << "IMPOSSIBLE" << endl;
  }
}
