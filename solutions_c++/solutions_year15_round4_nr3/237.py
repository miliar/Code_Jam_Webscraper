#include <iostream>
#include <cstdlib>
#include <sstream>
#include <vector>
#include <set>
#include <map>
using namespace std;

vector<int> pos;
int solve(vector<vector<int> > &in, int cur) {
  if(in.size() == cur) {
    int ans = 0;
    for(int v: pos) {
      if(v == 3)ans++;
    }
    return ans;
  }else{
    int ans = 999999999;
    if(cur != 0) {
      vector<int> back = pos;
      for(int v: in[cur]) {
        pos[v] |= 1;
      }
      ans = solve(in, cur+1);
      pos = back;
    }
    if(cur != 1) {
      vector<int> back = pos;
      for(int v: in[cur]) {
        pos[v] |= 2;
      }
      ans = min(ans, solve(in, cur+1));
      pos = back;
    }
    return ans;
  }
}
int main() {
  string line;
  getline(cin, line);
  int T = atoi(line.c_str());
  for(int tc = 1; tc <= T; tc++) {
    int N;
    getline(cin, line);
    N = atoi(line.c_str());
    vector<vector<int> > in(N);
    map<string,int> mp;
    for(int i = 0; i <  N; i++) {
      getline(cin, line);
      stringstream ss(line);
      string word;
      while(ss >> word) {
        if(mp.count(word) == 0) {
          int v = mp.size();
          mp[word] = v;
        }
        in[i].push_back(mp[word]);
      }
    }
    pos = vector<int>(mp.size());
    cout << "Case #" << tc << ": " <<solve(in, 0) << endl;
  }
}
