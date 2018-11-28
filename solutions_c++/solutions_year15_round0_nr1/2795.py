#include <iostream>
using namespace std;

int main() {

  int nc;
  cin >> nc;
  for (int c=0;c<nc;c++) {
    int nmax;
    cin >> nmax;
    
    string shy;
    cin >> shy;

    int res = 0;
    int count = 0;

    for (int i=0;i<=nmax;i++) {
      if (shy[i] == '0') continue;
      if (count < i) {
	res += i-count;
	count = i;
      }
      count += shy[i]-'0';
    }

    cout << "Case #" << c+1 << ": "<< res << endl;

  }

  return 0;

}
