#include<iostream>

using namespace std;

int main() {
  int t, T;
  cin>>T;
  for(t=1; t<=T; t++) {
    string str;
    int sum = 0;
    cin>>str;
    int len = str.length();
    int c = 0;
    for(int i=len-1; i>=0; i--) {
      if(c == 0 && str[i] == '-') {
        c++;
	// cout<<"Hello"<<endl;
      } else if(i<len-1 && str[i] != str[i+1]) {
        c++;
	// cout<<"Hi"<<endl;
      }
      // cout<<"Loop"<<endl;
    }
    cout<<"Case #"<<t<<": "<<c<<endl;
  }
  return 0;
}
