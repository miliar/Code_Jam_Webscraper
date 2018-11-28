#include<iostream>
#include<string>
using namespace std;

int main() {
  int t;
  cin>>t;
  string str;
  getline(cin,str);
  for (int i=0; i!=t; i++) {
    getline(cin,str);
    int cnt=0;
    bool last=(str[0]=='+');
    for (int j=0;j!=str.length();j++) {
      if (last != (str[j]=='+')) {
	cnt++;
	last=!last;
      }
    }
    if (!last) cnt++;
    cout<<"Case #"<<i+1<<": "<<cnt<<endl;
  }
  return 0;
}
      
