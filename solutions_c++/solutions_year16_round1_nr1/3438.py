#include<iostream>
#include<string>
using namespace std;

int main() {
  int T;
  cin >> T;
  for (int i = 0; i < T; i++) {
    string in;
    cin >> in;

    string res="";
    for( int j = 0; j < in.length(); j++){
      if ( j== 0)
            res = string(1,in[j]);
      else {
            if ( in[j]>=res[0])
                res = string(1,in[j]) + res;
            else
                res = res + string(1, in[j]);
      }
    }


    cout << "Case #"<< i + 1 << ": " << res<<endl;;
  }
}
