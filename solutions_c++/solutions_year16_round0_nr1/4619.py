#include <iostream>
using namespace std;

const int target = (1 << 10) - 1;

int DigMask(long long n){
  int mask = 0;
  while (n){
    mask |= 1 << (n%10);
    n /= 10;
  }
  return mask;
}

int main(){
  int t; cin >> t;
  for (int cas = 1; cas <= t; cas ++){
    long long num, now; cin >> num;
    int mask = 0;
    for (int i = 1; i < 1e7; i++){
      now = num * i;
      mask |= DigMask(now); 
      if (mask == target) break;
    }
    cout << "Case #" << cas << ": ";
    if (mask == target) cout << now << endl;
    else cout << "INSOMNIA" << endl;
  }
  return 0;
}
