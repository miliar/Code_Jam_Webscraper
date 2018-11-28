#include <iostream>
#define ui unsigned long int

using namespace std;

int check(ui n){
  int flag = 0;
  if(n == 0){
    return -1;
  }
  ui m = n;
  while(1){
    ui l = m;
    while(l != 0){
      flag |= 1 << (l % 10);
      l /= 10;
    }
    if(flag == 0b1111111111){
      return m;
    }
    m += n;
  }
}

int main(){
  int t;
  cin >> t;
  for(int i = 0; i < t; i++){
    ui n;
    cin >> n;
    int answer = check(n);
    cout << "Case #" << i + 1 << ": ";
    if(answer == -1){
      cout << "INSOMNIA";
    }else{
      cout << answer;
    }
    cout << '\n';
  }
  return 0;
}
