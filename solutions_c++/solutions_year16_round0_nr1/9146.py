#include <iostream>
#include <string>
#include <set>

using namespace std;
set<int> lookup;

string count_sheep(int n) {
  if(!n) return "INSOMNIA";
  int count = 1;
  int m = n;
  while(lookup.size() < 10) {
    m = n*(count++);
    int temp = m;
    while(temp > 0) {
      (temp < 10)? lookup.insert(temp) : lookup.insert(temp%10);
      temp /= 10;
    }
  }
  lookup.clear();
  return to_string(m);
}

int main() {
  int t, n;
  cin >> t;
  for(int i = 0; i < t; ++i) {
    cin >> n;
    cout << "Case #" << i+1  << ": " << count_sheep(n)<<endl;
  }
  return 0;
}
    
  
    
    
