#include <iostream>
#include <string>

using namespace std;

int getReq(string shy, int len) {
  int req = 0;
  int stood = 0;
  for (int i=0; i<=len; i++) {
    int sh = shy[i]-'0';
    if (sh != 0) {
      if (stood >= i) {
        stood += sh;
      }
      else {
        req += i-stood;
        stood += (i-stood) + sh;
      }
    }
  }
  return req;
}

int main(int agrc, char *argv[]) {
  int tests;
  cin>>tests;
  int index = 1;
  while (index <= tests) {
    int len;
    string shyness;
    cin>>len;
    cin>>shyness;
    int req = getReq(shyness, len);
    cout<<"Case #"<<index<<": "<<req<<endl;
    index++;
  }
  return 0;
}
