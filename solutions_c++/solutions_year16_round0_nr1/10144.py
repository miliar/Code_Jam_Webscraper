#include <iostream>
using namespace std;

int main() {
  long long int t, a[200];
  bool num[10], out = false;
  cin >> t;
  for(int i = 0 ; i < t; i++)
  {
    cin >> a[i];
    out = false;
    for(int j = 0; j < 10; j++) num[j] = false;

    if(a[i] == 0) {
      cout << "Case #" << i+1 << ": INSOMNIA\n";
      continue;
    } else {
      long long int sum = 0;
      while(!out) {
        sum += a[i];
        long long int tmp = sum;
        while(tmp) {
          int k = tmp % 10;
          num[k] = true;
          tmp /= 10;
        }
        int j;
        for(j = 0; j < 10; j++) {
          if(num[j] != true) break;
        }
        if(j == 10) out = true;
      }
      cout << "Case #" << i+1 << ": " << sum << endl;
    }
  }

}
