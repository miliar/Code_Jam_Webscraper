#include <iostream>
#include <string>
using namespace std;

int compute(string pancakes) {
  int count = 0;
  char previous = pancakes[0];
  for (int i=1; i<pancakes.length(); i++) {
    if (previous != pancakes[i]) {
      count++;
      previous = pancakes[i];
    }
  }
  if (pancakes[pancakes.length()-1] != '+')
    count++;
  return count;
}

int main(int argc, char **argv) {
  
    int t;
    std::cin >> t;
    
    string pancakes;
    
    for (int i = 1; i <= t; i++) {
      cin >> pancakes;
      
      cout << "Case #" << i << ": ";
      cout << compute(pancakes) << endl;
      
    }
    
    return 0;
}
