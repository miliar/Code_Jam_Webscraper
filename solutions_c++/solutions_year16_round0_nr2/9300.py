#include <iostream>
#include <vector>
#include <string>

using namespace std;

void flip(vector<bool>& v, int e) {
  int s = 0;
  while (s < e) {
    bool tmp = v[s];
    v[s] = !v[e];
    v[e] = !tmp;
    ++s;
    --e;
  }

  if (s == e) {
    v[s] = !v[s];
  }

  //for (auto i: v) {
    //cout << (i? "+" : "-");
  //}
  //cout << endl;

}

int main() {
  int t;
  cin >> t;
  for (int i = 1; i <= t; ++i) {
    string s;
    cin >> s;
    vector<bool> pc(s.size());
    for (int j = 0; j < s.size(); ++j) {
      pc[j] = (s[j] == '+') ? true: false;
    }

    int id = 0;
    bool f = pc[0];
    int flips = 0;
    while (id < s.size()) {
      if (id < s.size()-1 && pc[id+1] == f) {
        ++id;
      } else if (id < s.size()-1 || (id == s.size()-1 && !pc.back())) {
       // cout << "FLIP " << id << endl;
//        flip(pc, id);
        ++flips;
        f = !pc[id];
        if (id == s.size()-1) {break;}
//        f = pc[0];
      } else {
        ++id;
      }
    }

    cout << "Case #" << i << ": " << flips << endl;
  }


}
