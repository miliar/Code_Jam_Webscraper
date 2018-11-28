#include<iostream>
#include<string>
using namespace std;

int main() {
  int Z;
  cin >> Z;

  for(int z=1; z<=Z; z++) {
    string s;
    cin >> s;
    cout << "Case #" << z << ": ";
    int result = 0;

    for(int i=1; i<s.size(); i++) {
      if(s[i]!=s[i-1]) {
        result++;
      }
    }

    if(s[s.size()-1]=='-') {
      result++;
    }

    cout << result << endl;
  }

return 0;
}
