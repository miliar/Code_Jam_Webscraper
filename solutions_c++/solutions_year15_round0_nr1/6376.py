#include <iostream>
#include <string>
using namespace std;

size_t add(const string& S){
  size_t sum = 0, ret = 0;
  for (size_t i = 0; i < S.length(); ++i){
    size_t n = S[i] - '0';
    if (sum < i){
      ret += i - sum;
      sum = i;
    }
    sum += n;
  }
  return ret;
}

int main(){
  int T; cin >> T;
  for (size_t i = 1; i <= T; ++i){
    int N; cin >> N;
    string S; cin >> S;

    cout << "Case #" << i << ": " << add(S) << endl;
  }
}
