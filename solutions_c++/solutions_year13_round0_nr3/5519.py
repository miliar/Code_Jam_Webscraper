#include <iostream>
#include <vector>
#include <math.h>

using namespace std;

#define for0(i, n) for(int (i) = 0; (i) < (n); (i)++)
#define sz size()
#define pb push_back
#define ep 1E-7

bool is_pal(int n) {
  vector<int> l;
  while(n > 0) {
    l.pb(n % 10);
    n /= 10;
  }
  
  for (int i = 0; i < ((int)l.sz) / 2; i++) {
    if (l[i] != l[l.sz - 1 - i]) {
      return false;
    }
  }
  return true;

}

int main() {
 int T = 0;
  cin >> T;
  for0(t, T) {
    int A = 0; int B = 0;
    cin >> A >> B;
    
    int count = 0;
    for (int i = A; i <= B; i++) {
      if (!is_pal(i)) {
        continue;
      }
      for (int j = 1; j <= i; j++) {
        if (j*j != i) {
          continue;
        }
        if (is_pal(j)) {
          count++;
          break;
        }      
      }
    }
    cout << "Case #" << t + 1 << ": " << count << endl;
  }
  return 0;
}