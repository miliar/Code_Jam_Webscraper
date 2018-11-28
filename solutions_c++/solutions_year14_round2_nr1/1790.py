#include <iostream>
#include <cstdio>
#include <string>
#include <algorithm>
#include <vector>


using namespace std;


string unique(string s) {
  string res;

  for(int i = 0; i < s.size(); i++) {
    if (res.size() == 0 || res[res.size()-1] != s[i]) res.push_back(s[i]);
  }
  return res;
}

vector<int> count(string s){
  vector<int> res;
  for(int i = 0; i < s.size(); i++) {
    if(i == 0 || s[i-1] != s[i]){
      res.push_back(0);
    }
    res[res.size()-1]++;
  }

  return res;
}

int main(void){
  int T; 
  cin >> T;

  for(int cas = 1; cas <= T; cas++) {
    int n;
    vector<string> words;

      string w1, w2;
      cin >> n;
      cin >> w1;
      cin >> w2;
    if(unique(w1) != unique(w2)) {
      cout << "Case #" << cas << ": Fegla Won" << endl;
      continue;
    }

    vector<int> v1 = count(w1), v2 = count(w2);

    int steps = 0;

    for(int i = 0; i < v1.size(); i++) steps += abs(v1[i] - v2[i]);

    
    cout << "Case #" << cas << ": " << steps << endl;

  }

  return 0;
}





