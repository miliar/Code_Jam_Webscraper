#include <iostream>
#include <vector>

using namespace std;
int main()
{
  int T;
  cin >> T;
  for(int i = 1; i <= T; ++i) {
      size_t N, n = 0;
    cin >> N;

    cout << "Case #" << i << ": ";
    if(N == 0)
      cout << "INSOMNIA" << endl;
    else {
      vector<bool> vSeen(10, false);
      short nb = 0;
      while(nb != 10) {
        n += N;
      	string s = to_string(n);
        for(auto c: s) {
      	 if(!vSeen[c]) {
      	    ++nb;
      	    vSeen[c] = true;
      	  }
      	}
      }
      cout << n << endl;
    }
  }
}
