#include<bits/stdc++.h>
#define rep(i,n) for(int i=0;i<(int)(n);i++)
#define rrep(i,n) for(int i=(int)(n)-1;i>=0;i--)
#define all(a) (a).begin(),(a).end()
#define INIT(a) memset((a),0,sizeof(a))
#define EQ(a,b) (abs((a)-(b))<EPS)
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
  cout << fixed << setprecision(10);

  int testcase;

  cin >> testcase;
  for(int casenum=1;casenum<=testcase;casenum++){
    int n;
    D v,x;
    cin >> n >> v >> x;
    vector<D> r(n), c(n);
    rep(i,n)cin >> r[i] >> c[i];

    cout << "Case #" << casenum << ": ";
    if(n==1){
      if(EQ(x,c[0])){
	cout << v/r[0] << endl;
      }else{
	cout << "IMPOSSIBLE" << endl;
      }
    }else if(n==2){
      if(EQ(c[0],c[1])){
	if(EQ(c[0],x)){
	  cout << v/(r[0]+r[1]) << endl;
	}else{
	cout << "IMPOSSIBLE" << endl;
      }
      }else{
	D v0 = (v*x-v*c[1])/(c[0]-c[1]), v1 = v-v0;
	if(v0 < -EPS || v+EPS < v0){
	  cout << "IMPOSSIBLE" << endl;
	  continue;
	}
	if(v1 < -EPS || v+EPS < v1){
	  cout << "IMPOSSIBLE" << endl;
	  continue;
	}
	cout << max(v0/r[0],v1/r[1]) << endl;
      }
    }else{
      cout << "IMPOSSIBLE" << endl;
    }
  }
}
