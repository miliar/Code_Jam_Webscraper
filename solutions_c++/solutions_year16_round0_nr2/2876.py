#include <iostream>
#include <unordered_set>
#include <unordered_map>
using namespace std;

bool happy(const string& s) {
  return s == string(s.length(), '+');
}

string flip(const string& s, int pos) {
  string o = s;
  for(int i=0;i<=pos;++i) {
    o[i] = s[pos-i];
    o[i] = o[i] == '+' ? '-' : '+';
  }
  return o;
}

void dfs(const string& s, unordered_map<string, int>& v, int d, int max_d, bool& found) {
  if(happy(s)) {
    found = true;
    return;
  }

  if(d>=max_d || found) return;

  for(int i=0;i<s.length();++i) {
    string o = flip(s, i);
    if(v.count(o) && v[o] < d) continue;
    v[o] = d;    
    dfs(o, v, d+1, max_d, found);
  }
}

int main() {
  int T;
  cin>>T;
  string s;
  std::getline(cin, s);


  for(int t=1;t<=T;++t){
    bool found = false;
    int d = 0;
    
    std::getline(cin, s);

    while(true) {
      unordered_map<string, int> v;
      dfs(s, v, 0, d, found);
      if(found) break;
      d++;
    }

    cout<<"Case #"<<t<<": "<<d<<endl;    
  }
  return 0;
}