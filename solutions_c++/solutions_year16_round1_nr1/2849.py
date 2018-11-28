#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
using namespace std;

int main(){
  int n;
  cin >> n;
  for(int i = 0; i < n; i++){
    string s;
    cin >> s;
    string a = "";
    a += s[0];
    for(int j = 1; j < s.length(); j++){
      if(s[j] >= a[0]){
        string x = "";
        x += s[j];
        x+= a;
        a = x;
      } 
      else{
        a += s[j];
      }
    }
    cout << "Case #" << i+1 << ": " << a << endl;
  }
  return 0;
}
