#include<iostream>
#include<string>
using namespace std;

int main(){
  int t;
  std::cin >> t;
  for (int roop = 0; roop < t; roop++) {
    std::cout << "Case #" << roop + 1 << ": ";
    string s;
    std::cin >> s;
    char pancake[2] = {'-', '+'};
    int state = (s[0] == '+'), flip = 0;
    for (int i = 0; i < s.length(); i++) {
      if(s[i] != pancake[state]){
        state ^= 1;
        flip++;
      }
    }
    if(pancake[state] == '-')flip++;
    std::cout << flip << std::endl;
  }

  return 0;
}
