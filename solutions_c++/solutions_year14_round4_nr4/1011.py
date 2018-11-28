#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <climits>
#include <cfloat>
#include <map>
#include <utility>
#include <set>
#include <iostream>
#include <memory>
#include <string>
#include <vector>
#include <algorithm>
#include <functional>
#include <sstream>
#include <complex>
#include <stack>
#include <queue>
#include <cstring>


using namespace std;

int main(){
  int n_case;
  cin >> n_case;
  for( int loop = 0 ; loop < n_case ; loop++ ){
    int M,N;
    cin >> M >> N;
    string S[M];
    for( int i = 0 ; i < M; i++ ){
      cin >> S[i];
    }
    map<int,int> cnt;
    int maxInd=0;
    for( int mask = 0 ; mask < (1<<(2*M)); mask++){
      vector<string> maps[4];
      for( int i = 0 ; i < 4; i++ ) maps[i].clear();
      bool ok = true;
      int tmpMask = mask;
      for( int i = 0 ; i < M ; i++ ){
        if( (tmpMask%4) < N ){
          maps[tmpMask%4].push_back( S[i] );
        }
        else{
          ok = false;
        }
        tmpMask /=4;
      }
      for( int i = 0 ; i < N ; i++ ){
        if( maps[i].size() == 0 ) ok = false;
      }
      if( !ok ) continue;
      int score = 0;
      for( int i = 0 ; i < N; i++ ){
        set<string> S;
        for( int j = 0 ; j < (int)maps[i].size(); j++){
          string s = maps[i][j];
          //cout <<s<<"...";
          for( int k = 0 ; k <= (int)s.size(); k++ ){
            //cout << s.substr(0,k)<<", "<<endl;
            S.insert(s.substr(0,k));
          }
        }
        //cout<<endl;
        score += S.size();
      }
      //cout << endl;
      cnt[score]++;
      if(maxInd < score ) maxInd=score;
    }
    cout << "Case #" << loop+1 << ": "<<maxInd<<" " <<cnt[maxInd]<< endl;
  }
  return 0;
}
