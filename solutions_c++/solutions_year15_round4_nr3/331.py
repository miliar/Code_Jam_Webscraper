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

const static int INF = 1e8;
const static D EPS = 1e-8;

int main(){
  int testcase;

  cin >> testcase;
  for(int casenum=1;casenum<=testcase;casenum++){
    int n;
    cin >> n;
    vector< vs > words(n);
    cin.ignore();
    rep(i,n){
      string s;
      getline(cin,s);
      stringstream ss(s);
      while(ss >> s)words[i].pb(s);
    }

    int num = 0;
    map<string,int> id;
    rep(i,n){
      for(string w : words[i]){
	if(id.count(w) == 0)id[w] = num++;
      }
    }

    vector<vi> vid(n);
    rep(i,n){
      for(string w : words[i])vid[i].pb(id[w]);
    }
    
    int res = INF;
    rep(bit,1<<(n-2)){
      vi use1(num,0), use2(num,0);
      for(int a : vid[0])use1[a] = 1;
      for(int a : vid[1])use2[a] = 1;

      rep(i,n-2){
	if( (bit>>i)&1 ){
	  for(int a : vid[i+2])use1[a] = 1;
	}else{
	  for(int a : vid[i+2])use2[a] = 1;
	}
      }

      int sum = 0;
      rep(i,num){
	if(use1[i] && use2[i])sum++;
      }
      res = min(res, sum);
    }

    cout << "Case #" << casenum << ": " << res << endl;
  }
}
