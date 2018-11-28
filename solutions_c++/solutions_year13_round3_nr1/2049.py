#include <iostream>
#include <vector>

using namespace std;

vector<string> all_substrings(string s, int min_n) {
  vector<string> r;
  for (int l=min_n; l<=s.length(); ++l) {
    for (int ip=0; ip<=s.length()-l; ++ip) {
      string ss=s.substr(ip, l);
      r.push_back(ss);
    }
    
  }
  return r;
}
bool consonant(char c) {
  return (c!='a' && c!='e' && c!='i' && c!='o' && c!='u');
}

bool n_consecutive(string s, int n) {
  int nc=0;
  for (int p=0; p<s.size(); ++p) {
    if (consonant(s[p])) nc++;
    else nc=0;
    if (nc==n) return true;
  }
  return false;
}

int n_value(string name, int n) {
  int nv=0;
  
  vector<string> substrs =  all_substrings(name, n);

  for (int i = 0; i < substrs.size(); ++i) {
    string substr=substrs[i];
    nv+=(int)n_consecutive(substr, n);
  }
  return nv;
}


int main() {
  int T;
  string name;
  int n;

  cin >> T;

  for (int t=1; t<=T; ++t) {
    cin >> name >> n;


    cout << "Case #" << t << ": " << n_value(name, n) << endl;
  }

}
