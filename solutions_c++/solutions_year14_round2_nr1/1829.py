#include<bits/stdc++.h>

#define REP(i,s,n) for(int i=s;i<n;i++)
#define rep(i,n) REP(i,0,n)

using namespace std;

typedef long long ll;
const int IINF = INT_MAX;
const ll LLINF = LLONG_MAX;

typedef pair<char,int> ci;

int T,n;
string s[1000];
vector<ci> vec[1000];

int calc(int cur){
  int cost = 0;
  rep(i,n){
    if( i == cur ) continue;
    if( vec[i].size() != vec[cur].size() ) return IINF;
    rep(j,vec[i].size()){
      if( vec[i][j].first != vec[cur][j].first ) return IINF;
      cost += abs(vec[i][j].second-vec[cur][j].second);
    }
  }
  return cost;
}

bool check(){
  rep(j,n)REP(i,j+1,n){
    if( vec[i].size() != vec[j].size() ) return false;
    rep(k,vec[i].size()){
      if( vec[i][k].first != vec[j][k].first ) return false;
    }
  }
  return true;
}

int main(){
  int CNT = 1;
  cin >> T;
  while( T-- ){

    cin >> n;
    rep(i,n)vec[i].clear();
    rep(i,n){
      cin >> s[i];
      int cnt = 0;
      rep(j,s[i].size()){
        if( j && s[i][j] != s[i][j-1] ) {
          vec[i].push_back(ci(s[i][j-1],cnt));
          cnt = 1;
        } else cnt++;
      }
      vec[i].push_back(ci(s[i][s[i].size()-1],cnt));
      /*
      rep(j,vec[i].size()){
        cout << "(" << vec[i][j].first << "," << vec[i][j].second << ") ";
      }cout << endl;
      */
    }

    /*
    int ans = IINF;
    rep(i,n){
      ans = min(ans,calc(i));
    }
    */




    cout << "Case #" << CNT++ << ": ";
    if( !check() ) puts("Fegla Won");
    else {

      int len = vec[0].size();
      double ave[len];
      rep(i,len) ave[i] = 0;
      rep(i,n){
        rep(j,vec[i].size()) ave[j] += vec[i][j].second;
      }
      rep(i,len) ave[i] /= (double) n;

      int ans = IINF;
      int cost = 0;
      rep(i,n){
        rep(j,vec[i].size()){
          cost += abs(vec[i][j].second-floor(ave[j]));
        }
      }
      ans = cost;

      cost = 0;
      rep(i,n){
        rep(j,vec[i].size()){
          cost += abs(vec[i][j].second-ceil(ave[j]));
        }
      }
      ans = min(ans,cost);
      cout << ans << endl;
    }

  }
  return 0;
}
