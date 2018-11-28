#include<iostream>


using namespace std;

int solve(int n) {
  bool digits[10];        
  if(n == 0) return -1;
  int cur = n;
  while(1) {
    bool isCompleted = true;
    int temp = cur;
    while(temp > 0) {
      int digit = temp % 10;
      digits[digit] = true;
      temp /= 10;
    }
    for(int i=0; i < 10; ++i) {
      if(digits[i] == false) {
        isCompleted = false;
        break;
      }
    }
    if(isCompleted) return cur; 
    cur += n;
  }
}

int main() {
  int T;
  int N;
  cin >> T;
  for(int t=0;t < T; ++t) {
    cin >> N;
    int result = solve(N);
    if(result == -1) {
      cout<<"Case #" << t + 1 << ": " << "INSOMNIA"<<endl;
    } else {
      cout<<"Case #" << t + 1 << ": " << result <<endl;
    }
  }
}
