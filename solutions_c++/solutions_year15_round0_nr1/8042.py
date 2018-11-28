#include <iostream>
#include <string>
using namespace std;

int atoi(int in){
  return in-48;
}

int compute(int max, string si) {
  int before = atoi(si[0]);
  int needed = 0;
  int actual = 0;
  for (int i = 1; i <= max; i++) {
    actual = (i - before);
    if (actual > 0) {
      needed += actual;
      before += actual;
    }
    before += atoi(si[i]);
  }
  return needed;
}

int main(int argc, char **argv) {
  
    int t;
    std::cin >> t;
    
    int max;
    string si;
    
    for (int i = 1; i <= t; i++) {
      cin >> max;
      cin >> si;
      cout << "Case #" << i << ": ";
      cout << compute(max, si) << endl;
      
    }
    
    return 0;
}
