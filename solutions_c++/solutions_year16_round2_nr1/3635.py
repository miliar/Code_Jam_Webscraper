#include <vector>
#include <string>
#include <iostream>
#include <map>
#include <set>
using namespace std;

set<pair<vector<int>,int> > seen;

int doit2(vector<int> &freq, vector<int> &ret, int idx) {
  if(idx==10) {
    for(int i=0;i<128;i++) if(freq[i]>0) return 0;
    for(int i=0;i<10;i++) for(int j=0;j<ret[i];j++) cout<<i;
    return 1;
  }
  string digits[10]={"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};
  for(int i=0;;i++) {
    if(doit2(freq,ret,idx+1)) break;
    bool ok=true;
    ret[idx]++;
    for(int j=0;j<digits[idx].size();j++) {
      freq[digits[idx][j]]--;
      if(freq[digits[idx][j]]<0) ok=false;
    }
    if(!ok) {
      ret[idx]=0;
      for(int j=0;j<digits[idx].size();j++) {
        freq[digits[idx][j]]+=i+1;
      }
      break;
    }
  }
  return 0;
}

string doit(string s) {
  vector<int> freq(128),ret(10);
  for(int i=0;i<s.size();i++) freq[s[i]]++;
  doit2(freq,ret,0);
  return "";
}

int main() {
  int tests;
  cin>>tests;
  for(int i=0;i<tests;i++) {
    string s;
    cin>>s;
    cout<<"Case #"<<(i+1)<<": ";
    doit(s);
    cout<<endl;
  }
  return 0;
}
