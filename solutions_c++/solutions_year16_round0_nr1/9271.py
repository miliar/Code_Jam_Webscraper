#include <iostream>
#include <vector>
#include <string>

using std::cin;  using std::cout;  using std::endl;
using std::vector; using std::string;

vector<bool> seen(10);

bool allseen() {
  for(int i=0;i<10;++i)
    if (!seen[i])
      return false;
  return true;
}

int main() {

  int T;
  cin >> T;

  long N, currentN, cN;

  for (int i=1; i<=T; ++i) {
    cin >> N;

    for(int j=0;j<10;++j)
      seen[j] = false;

    if ( N == 0 ) {
      cout << "case #" << i << ": INSOMNIA" << endl;
      continue;
    }

    currentN = N;
    bool done = false;
    while ( !done ) {
      cN = currentN;
      while (cN > 0) {
	seen[ cN % 10 ] = true;
	cN = cN / 10;
      }
      if ( allseen() ) {
	cout << "case #" << i << ": " << currentN << endl;
	done = true;
      }
      currentN += N;
    }

  }

  return 0;
}
