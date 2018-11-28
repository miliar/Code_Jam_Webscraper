#include<iostream>
#include<set>
using namespace std;

const int CHEAT = -1;
const int BAD = -2;

int func(){
  int a;
  cin >> a;
  a--;

  set<int>st;
  for(int i = 0 ; i < 4 ; i++){
    int e;
    for(int j = 0 ; j < 4 ; j++){
      cin >> e;
      if(a == i)st.insert(e);
    }
  }

  cin >> a;
  a--;
  int ret = CHEAT;

  for(int i = 0 ; i < 4 ; i++){
    int e;
    for(int j = 0 ; j < 4 ; j++){
      cin >> e;
      if(a == i && st.count(e)){
	if(ret == CHEAT){
	  ret = e;
	}
	else {
	  ret = BAD;
	}
      }
    }
  }
  return ret;
}

int main(){
  int T;
  cin >> T;
  for(int i = 0 ; i < T ; i++){
    cout << "Case #" << i+1 << ": ";
    int ans = func();
    if(ans == CHEAT)cout << "Volunteer cheated!";
    else if(ans == BAD)cout << "Bad magician!";
    else cout << ans;
    cout << endl;
  }
  return 0;
}
