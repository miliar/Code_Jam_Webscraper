#include <iostream>
using namespace std;

int main() {
  int t;
  cin >> t;
  for(int caseno = 1; caseno <= t; caseno++) {
    cout << "Case #" << caseno << ":";

    long long k, c, s;
    cin >> k >> c >> s;
    if((k+c-1)/c > s)
      cout << " IMPOSSIBLE" << endl;
    else {
      long long cur = 0;
      long long ktoc = 1;
      for(int i = 0; i < c; i++) ktoc *= k;
      while(cur < k) {
	long long loc = 0;
	long long shift = ktoc/k;
	long long finish = min(cur + c, k);
	while(cur < finish) {
	  loc += cur*shift; 
	  cur++;
	  shift /= k;
	}
	cout << " " << (loc+1);
      }
      cout << endl;
    }
  }
  return 0;
}
