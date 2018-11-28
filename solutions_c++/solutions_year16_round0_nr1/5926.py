#include <iostream>

using namespace std;

int main() {
  int t;
  cin >> t;


  for (int i = 0; i < t; i++) {
    int n;
    cin >> n;
    if (n==0) {
      cout << "Case #" << (i+1) << ": INSOMNIA" << endl;
      continue;
    }

    int cur = n;
    int count = 0;
    int seen[10] = {0,0,0,0,0,0,0,0,0,0};
    while(count < 10) {
      int temp = cur;
      while (temp > 0) {
        int mod = temp % 10;
        if (seen[mod] == 0) {
          seen[mod] = 1;
          count += 1;
        }
        temp /= 10;
      }
      cur += n;
    }

    cout << "Case #" << (i+1) << ": " << (cur - n) << endl; 
  }
}
