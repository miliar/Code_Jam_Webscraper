#include <iostream>
#include <string>
#include <algorithm>
#define ui unsigned long int

using namespace std;

int main(){
  int t;
  cin >> t;
  for(int i = 0; i < t; i++){
    string s;
    cin >> s;
    ui answer = 0;
    char p = '+';
    for (auto j = s.rbegin(); j < s.rend(); j++){
      if(p != *j) answer++;
      p = *j;
    }
    cout << "Case #" << i + 1 << ": ";
    cout << answer;
    cout << '\n';
  }
  return 0;
}
