#include <iostream>
#include <algorithm>
#include <vector>
#include <array>
#include <sstream>

using std::cin;
using std::cout;
using std::vector;
using std::string;

int main() {
  std::ios::sync_with_stdio(false);

  int tests;
  cin >> tests;
  cin.ignore();
  for (int i = 0; i < tests; ++i) {
    char line[1000];
    cin.getline(line,1000);
    string l(line);
    string result;
    for( auto a:l){
    if(result.empty()){
    result.push_back(a);
    continue;
    }
    if(result.front()<=a){
     result.insert(result.begin(),a);
    } else {
    result.push_back(a);
    }
    }
    cout << "Case #" << i + 1 << ": ";
    cout << result << "\n";
    }
    
    
  }
