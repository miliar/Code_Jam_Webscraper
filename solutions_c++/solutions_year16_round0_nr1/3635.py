#include <iostream>

using namespace std;

int main() {
  int T;
  cin >> T;
  long long N, M;
  for(int i = 1; i <= T; ++i) {
    cin >> N;
    cout << "Case #" << i << ": ";
    if(N != 0) {
      long long j = 1;
      int c = 0;
      while(true) {
	M = N*j;
	do {
	  c |= 1 << (M%10);
	}while(M/=10);
	if(c == 1023) {
	  cout << N*j;
	  break;
	}
	++j;
      }
    }     
    else 
      cout <<"INSOMNIA";
    cout << endl; 
  }
}
