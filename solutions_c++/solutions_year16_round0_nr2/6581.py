#include <iostream>
#include <string>

using namespace std;

string flip(string s, int p){
  string a = "";
  for(int i = 0; i <= p; i++){
    char c = s[p-i];
    a+= c == '+' ? '-' : '+';
  }
  for(int i = p+1; i < s.length(); i++){
    a+=s[i];
  }
  return a;
}

int main(){
  int t;
  cin >> t;
  for(int i = 0; i < t; i++){
    string s;
    cin >> s;
    bool same = false;
    int flips = 0;
    while(!same){
      char c = s[0];
      same = true;
      for(int i = 1; i < s.size(); i++){
        if(s[i] != c){
          same = false;
          s = flip(s, i-1);
      //    cout << s << endl;
          flips ++;
          break;
        }
      }
    }
    cout << "Case #" << i+1<< ": " << ((s[0] == '+') ? flips : flips + 1) << endl;
  }
  return 0;
}
