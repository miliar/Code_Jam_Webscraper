#include <iostream>
#include <string>
using namespace std;

int main() {

  long long int t;
  cin >> t;

  for ( long long int tt = 0; tt < t; tt++ ) {

    cout << "Case #" << tt+1 << ": ";


    string in;
    cin >> in;

    bool f[1001] = {};

    long long int n = in.size();
    long long int e = n - 1;

    while( e >= 0 ) {

      long long int ne = e;

      for ( long long int i = e - 1; i >= 0; i-- ) {
	if ( in[i] > in[ne] ) {
	  ne = i;
	}
      }

      f[ne] = true;
      e = ne - 1;

    }

    string ans = "";

    for ( long long int i = 0; i < n; i++ ) {

      if ( f[i] == true ) {
	ans = in[i] + ans;
      }else {
	ans = ans + in[i];
      }

    }

    cout << ans << endl;

  }

  return 0;

}
