#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

long int prob(string str) {
  int len = str.size();
  int pflag = 1,running = 0;
  long int result = 0;
  for(int i = 0;i<len;i++) {
    if(str[i] == '+') {
      pflag = 2;
      running = 0;
    }
    if(str[i] == '-' && !running) {
      result += (1*pflag);
      running = 1;
    }
  }
  return result;
}

int main() {
  int T;
  cin>>T;
  int i = 1;
  while(T--) {
    string str;
    long int result;
    cin>>str;
    result = prob(str);
    cout<<"Case #"<<i<<": "<<result<<endl;
    i++;
  }
}
