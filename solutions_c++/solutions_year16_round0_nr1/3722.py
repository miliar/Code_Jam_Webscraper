/*
	Alexandre Borgo - Google Code Jam - 2016 - A. Counting Sheep
*/

#include <iostream>

using namespace std;

bool allNumbers(bool numbers[10]) {
    for(int i = 0 ; i < 10 ; i++) {
        if(!numbers[i]) return false;
    }
    return true;
}

int main() {
  int T;
  int n;
  int n_tmp;
  int number;

  cin >> T;

  for(int i = 1 ; i <= T ; i++) {
    cin >> n;
    int j = 0;
    bool numbers[10] = {  false };

    for(j = 1 ; ; j++) {
        n_tmp = j*n;

        while(n_tmp >= 1) {
            numbers[n_tmp%10] = true;
            n_tmp /= 10;
        }

        if(allNumbers(numbers)) break;

        if(n==0) break;
    }
    if(n==0) cout << "Case #" << i << ": " << "INSOMNIA" << endl;
    else cout << "Case #" << i << ": " << j*n << endl;
  }

  return 0;
}
