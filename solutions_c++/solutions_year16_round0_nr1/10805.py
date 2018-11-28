#include <iostream>
#include <utility>
#include <vector>
#include <math.h>       /* pow */

using namespace std;

int main() {
  int t; //number of test cases
  cin >> t;
  vector<int> numbers;
  vector<int> solution(t);

  for (int i = 0; i < t; i++) {
    int x;
    cin >> x;
    numbers.push_back(x);
  }

  for (int i = 0; i < t; i++) {
    if(numbers[i] != 0){
      int original = numbers[i];
      int number = 0;    
      int asleep = 0;
      bool seen[10] = {false, false, false, false, false, false, false, false, false, false};
      while(asleep < 10){
        number += original;
        int k = 10;
        int old = 0;
        while(number > old) {
          int aux = number % k;
          int _new = aux;
          aux -= old;
          aux = aux/(k/10);
          if(!seen[aux]){
            seen[aux] = true;
            asleep++;
          }

          k = k*10;
          old = _new;
        }   
      }
      solution[i] = number;
    }
  }

  for (int i = 0; i < t; i++) {
    if(numbers[i] != 0) 
      cout << "Case #" << i+1 << ": " << solution[i] << endl;
    else
      cout << "Case #" << i+1 << ": INSOMNIA" << endl;
  }

  return 0;
}