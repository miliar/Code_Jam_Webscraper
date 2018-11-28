#include <iostream>
#include <vector>
#include <string>

using std::cin;  using std::cout;  using std::endl;
using std::vector; using std::string;

int main() {

  int T;
  cin >> T;

  for (int i=1; i<=T; ++i) {
    int N;
    cin >> N;
    vector<int> senators(26);
    int sum = 0;
    for(int j=0; j<N; ++j) {
      cin >> senators[j];
      sum += senators[j];
    }
    cout << "case #" << i << ":";
    while ( sum > 0) {
      int l = 0;
      for(int j=0; j<N; ++j) {
	if (senators[j]> senators[l]) {
	  l = j;
	}
      }
      int sl;
      if (l == 0)
	sl = 1;
      else
	sl = 0;
      for(int j=0; j<N; ++j) {
	if (j!=l && senators[j]> senators[sl]) {
	  sl = j;
	}
      }
      cout << ' ';
      char L = 'A' + l;
      char SL = 'A' + sl;
      if ( 2*(senators[l]-1) <= sum-1
	   && 2*(senators[sl]) <= sum-1) {
	cout << L;
	--senators[l];
	--sum;
      }
      else {
	cout << L << SL ;
	--senators[l];
	--senators[sl];
	sum -= 2;
      }
    }
    cout << endl;
  }
  return 0;
}

