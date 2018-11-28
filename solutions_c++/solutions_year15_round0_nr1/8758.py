#include <iostream>

using namespace	std;

int s[1010];

void test(int kase) {
  int Smax;
  cin >> Smax;

  for (int i = 0; i <= Smax; ++i) {
    char c;
    cin >> c;
    s[i] = c -	'0';
  }


  int standing = s[0];
  int maxd = 0;
  for (int i = 1; i <= Smax; ++i) {
    int	d = i -	standing;
    maxd = max(maxd, d);
    standing +=	s[i];
  }

  cout << "Case #" << kase	<< ": " << maxd << endl;
}

int main() {
  int T;
  cin >> T;
  for (int i = 0; i < T; ++i) {
    test(i + 1);
  }
}



