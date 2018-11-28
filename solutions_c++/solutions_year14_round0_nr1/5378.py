#include<bits/stdc++.h>

#define REP(i,s,n) for(int i=s;i<n;i++)
#define rep(i,n) REP(i,0,n)

using namespace std;

int main(){
  int T,r,tmp,CNT=1;
  cin >> T;
  while(T--){
    cin >> r;
    bool selected[17];
    rep(i,17) selected[i] = false;
    rep(i,4)rep(j,4){
      cin >> tmp;
      if( i+1 == r ) selected[tmp] = true;
    }

    cin >> r;
    vector<int> ans;
    rep(i,4)rep(j,4){
      cin >> tmp;
      if( i+1 == r ){
	if( selected[tmp] ) ans.push_back(tmp);
      }
    }

    cout << "Case #" << CNT++ <<": ";
    if( ans.size() == 1 ) cout << ans.back() << endl;
    else if( ans.empty() ) cout << "Volunteer cheated!" << endl;
    else cout << "Bad magician!" << endl;

  }
  return 0;
}
