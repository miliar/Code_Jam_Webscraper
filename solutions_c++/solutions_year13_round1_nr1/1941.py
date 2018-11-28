#include <iostream>

using namespace std;

int
main() {
  int T;
  
  cin >> T;
  
  for(int i = 1; i <= T; i++) {
    long long r, t;
    
    cin >> r >> t;
    
    int n = 0;
    int req = 2*r+1;
    while(t >= req) {
      t -= req;
      n++;
      r +=2;
      req = 2*r+1;
//      cout << t << " - req: " << req << endl;
    }
    
    cout << "Case #"<< i << ": " << n << endl;
  }
  
  return 0;
}
