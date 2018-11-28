#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <deque>

using namespace std;

string s;

string gao(string s){
  string ret;
  for (char i = 'Z'; i >= 'A'; i--){
    int cnt = 0, pre = 0;
    string tmp;
    for (int j = 0; j < s.size(); j++){
      if (s[j] == i){
        cnt ++;
        if (cnt == 1){
            tmp += gao(s.substr(pre, j - pre));
        }
        else{
            tmp += s.substr(pre, j - pre);
        }
        pre = j + 1;
      }
    }
    if (cnt){
      for (int j = 0; j < cnt; j++) ret += i;
      ret += tmp;
      if (pre < s.size()) ret += s.substr(pre);
      break;
    }
  }
  return ret;
}

int main(){
  int t; cin >> t;
  for (int cas = 1; cas <= t; cas++){
    cin >> s;
    cout << "Case #" << cas << ": " << gao(s) << endl;
  } 
  return 0;
}
