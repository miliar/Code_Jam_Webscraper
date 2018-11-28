#include <iostream>
#include <vector>

using namespace std;

bool isIn(int digit, int num) { //does not work for 0 but that's okay
  if(num == 0) 
    return false;
  return (num % 10 == digit || isIn(digit, num / 10));
}

int loops(int num) {
  if(num == 0) 
    return -1;
  bool test[10]{false};

  int ret = 1;
  int found = 0;
  do{
    for(int i = 0; i < 10; i++) {
      if(!test[i]) {
        if(isIn(i, num * ret)) {
          test[i] = true;
          found++;
        }
      }
    }
    ret++;
  } while(found < 10);
  return (ret-1)* num;

}

int main() {

  // exit(1);
  int numCases;
  cin >> numCases;
  for(int i = 1; i <= numCases; i++) {
    int check;
    cin >> check;
    cout << "Case #" << i << ": ";

    int checked = loops(check);
    if(checked == -1)
      cout << "INSOMNIA" << endl;
    else 
      cout << checked << endl;
  }
}