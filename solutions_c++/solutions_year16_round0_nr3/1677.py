#include <iostream>
#include <string>

using namespace std;

string tobin(unsigned int what){
  string ret = "";
  while (what != 0){
    if(what % 2 == 0){
      ret.push_back('0');
    } else {
      ret.push_back('1');
    }
    what /= 2;
  }
  std::reverse(ret.begin(), ret.end());
  return ret;
}

unsigned long long int tonum(string what, unsigned int base){
  unsigned long long int ret = 0;
  unsigned long long int curmult = 1;
  for(int i = what.size() - 1; i >= 0; i--){
    ret += curmult * (what[i] - '0');
    curmult *= base;
  }
  return ret;
}

int main(){
  int N,J;
  int T;
  cin >> T;
  for(int k = 0; k < T; k++){
    cin >> N;
    cin >> J;
    unsigned int nextnum = (1 << (N / 2 - 1)) + 1;
    unsigned int div = (1 << (N / 2)) + 1;
    cout << "Case #" << k + 1 << ": " << endl;
    for(int i = 0; i < J; i++){
      cout << tobin(nextnum) << tobin(nextnum) << " ";
      for(unsigned int j = 2; j < 11; j++){
        string tmp = tobin(nextnum) + tobin(nextnum);
        cout << tonum(tobin(div), j) << " ";
      }
      cout << endl;
      nextnum += 2;
    }
  }

}

