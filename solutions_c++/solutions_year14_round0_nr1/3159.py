#include <iostream>
#include <set>

#define SIZE 4

using namespace std;
typedef set<int> S;

int main(){
  int T = 0;
  cin >> T;

  for(int t = 0; t < T; ++t){
    int q[2];
    int g[2][4][4];
    S set;
    for(int ch = 0; ch < 2; ++ch){
      cin >> q[ch];
      q[ch]--;
      for(int r = 0; r <SIZE; ++r){
        for(int c = 0; c < SIZE; ++c){
          cin >> g[ch][r][c];
        }
      }
    }
    int ans = 0;
    int prev = 0;
    for(int ch = 0; ch < 2; ++ch){
      for(int c = 0; c < SIZE; ++c){
        set.insert(g[ch][q[ch]][c]);
        if(prev == set.size()){
          ans = g[ch][q[ch]][c];
        }
        prev = set.size();
      }
    }
    int size = set.size();
    if(size == SIZE*2 - 1){
      cout << "Case #" << (t+1) << ": " << ans << endl;
    }else if(size == SIZE*2){
      cout<< "Case #" << (t+1) << ": Volunteer cheated!" << endl;
    }else{
      cout<< "Case #" << (t+1) << ": Bad magician!" << endl;
    }
  }
}
