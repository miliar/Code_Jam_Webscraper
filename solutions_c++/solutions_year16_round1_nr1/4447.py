#include<iostream>
#include<vector>
#include<string>
using namespace std;

int main() {
  int T;
  string S;
  cin >> T;
  for(int x=1; x<=T; ++x){
    cin >> S;
    vector<char> v;
    v.push_back(S[0]);

    for(int i=1; i<S.length(); ++i) {
      if (S[i] < v[0]) {
        v.push_back(S[i]);
      } else {
        auto it = v.begin();
        v.insert(it, S[i]);
      }
    }
    cout << "Case #" << x << ": ";
    for(char c : v) {
      cout << c;
    }
    cout << endl;
  }
  return 0;
}
