#include <iostream>
#include <sstream>
using namespace std;

int main() {
  int T;
  std::ios_base::sync_with_stdio(false);
  cin.tie(0);
  cin >> T;
  for(int cn = 1; cn <= T; ++cn) {
    int K, C, S;
	cin >> K >> C >> S;
cerr << cn << " of " << T << '\n';
	cout << "Case #" << cn << ':';
	for(int i = 1; i <= S; ++i) cout << ' ' << i;
	cout << '\n';
  }
}
