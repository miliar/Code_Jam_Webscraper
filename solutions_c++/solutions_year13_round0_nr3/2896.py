#include <iostream>

using namespace std;

bool ispalin(int x){
  static int as[4];
  int k = 0;
  while(x > 0){
    as[k++] = x % 10;
    x /= 10;
  }
  for(int i = 0; i < k/2; ++i)
    if(as[i] != as[k-i-1])
      return false;
  return true;
}

int main(void){
  int T, A, B;
  cin >> T;
  for(int t = 0; t < T; ++t){
    cin >> A >> B;

    int res = 0;
    for(int i = 0; i*i <= B; ++i){
      if(i*i < A) continue;
      res += ispalin(i) && ispalin(i*i);
    }

    cout << "Case #" << t+1 << ": " << res << endl;
  }

  return 0;
}
