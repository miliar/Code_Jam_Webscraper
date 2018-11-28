#include<bits/stdc++.h>
using namespace std;

int main(){
  int t;
  std::cin >> t;
  for (int roop = 0; roop < t; roop++) {
    std::cout << "Case #" << roop + 1 << ": ";
    int n;
    std::cin >> n;
    int ans = 0;
    if(n == 0){
      std::cout << "INSOMNIA" << std::endl;
      continue;
    }
    bool used[10];
    memset(used, false, sizeof(used));
    bool flag = true;
    while(flag){
      ans += n;
      int tmp = ans;
      while(tmp > 0){
        used[tmp%10] = true;
        tmp /= 10;
      }
      flag = false;
      for (int i = 0; i < 10; i++) {
        if(used[i] == false)flag = true;
      }
    }
    std::cout << ans << std::endl;
  }
    
  return 0;
}
