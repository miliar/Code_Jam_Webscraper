#include <iostream>
#include <sstream>
using namespace std;

static long long int getlimit(long long int N) {
  stringstream ss;
  long long int NN;
  ss << N << N;
  ss >> NN;
  return (NN + 1);
}

int main() {
  int T;
  std::ios_base::sync_with_stdio(false);
  cin.tie(0);
  cin >> T;
  for(int cn = 1; cn <= T; ++cn) {
cerr << cn << " of " << T << '\n';
    long long int N;
	bool seen[10] = {0};
	cin >> N;
    //const long long int limit = getlimit(N);
	int s = 0;
	long long int a;
	//for(a = N; N && (a < limit) && (s < 10); a += N) {
	if(N) for(a = N; s < 10; a += N) {
	  long long int ac = a;
	  do {
	    const int d = (int)(ac % 10);
		if(!seen[d]) {
		  seen[d] = true;
		  if(++s == 10) break;
		}
	    ac /= 10;
	  } while(ac);
	}
	cout << "Case #" << cn << ": ";
	if(s == 10) cout << (a - N) << '\n';
	else cout << "INSOMNIA\n";
  }
}
