#include<iostream>


using namespace std;

int solve(string input) {
  bool startWithMinus = false;
  if(input[0] == '-') {
    startWithMinus = true;
  }
  
  int flipCount = 0;
  for(int i= 1; i < input.size(); ++i) {
    if(input[i] == '-' && input[i-1] == '+') {
      flipCount++;
    }
  }
  return startWithMinus ? 1 + 2 * flipCount : 2 * flipCount;
}

int main() {
  int T;
  cin >> T;
  for(int t=0;t < T; ++t) {

    string input;
    cin >> input;
    int result = solve(input);
    cout<<"Case #" << t + 1 << ": " << result <<endl;
  }
}
