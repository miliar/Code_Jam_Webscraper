#include <iostream>  // includes cin to read from stdin and cout to write to stdout
#include <list>
using namespace std;  // since cin and cout are both in namespace std, this saves some text

int main() {
  int T,N;
  cin >> T;
  for (int i = 0; i < T; ++i) {
    cout << "Case #" << i+1 << ": ";
    cin >> N;
    if(N == 0 ){
      cout << "INSOMNIA"<<endl;
    }else{
      int n,r,tmp;
      n=N;
      //list of digits
      list<int> digits;
      for (int j=0;j<10;++j){
        digits.push_back(j);
      }

      while(!digits.empty()){
        tmp =n ;
        do{
          r = tmp % 10 ;
          digits.remove(r);
          tmp = tmp / 10;
        }while(tmp > 0);
        n = N + n;
      }

      cout << n - N  << endl;
    }
  }
  return 0;
}
