#include <iostream>
#include <set>
#include <vector>
#include <cstdlib>
#include <sstream>

using namespace std;

string BAD = "Bad magician!";
string CHEAT = "Volunteer cheated!";

string solve(){
  int answer;
  cin >> answer;
  set<int> s;
  // fst ans
  for(int i = 0; i < 4; i++){
    for(int j = 0; j < 4; j++){
      int n;
      cin >> n;
      if(answer-1 == i){
        s.insert(n);
      }
    }
  }
  
  cin >> answer;
  // snd ans
  vector<int> res;
  for(int i = 0; i < 4; i++){
    for(int j = 0; j < 4; j++){
      int n;
      cin >> n;
      if(answer-1 == i){
        if(s.find(n) != s.end()){
          res.push_back(n);
        }
      }
    }
  }

  if(res.size() == 1){
    stringstream ss;
    ss << res[0];
    return ss.str();
  }else if(res.size() > 1){
    return BAD;
  }else{
    return CHEAT;
  }
}

int main(){
  int T;
  cin >> T;
  for(int i = 0; i < T; i++){
    cout << "Case #" << i+1 << ": " << solve() << endl;
  }
}
