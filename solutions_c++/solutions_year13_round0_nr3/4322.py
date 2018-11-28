#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <cmath>

using namespace std;

#define show(x)   cout << #x << " = " << x << endl

bool ispalindrome(long long x) {
  char buf[100];
  sprintf(buf, "%lld", x);
  int len = strlen(buf);
  for(int i = 0; i < len; ++i)
    if(buf[i] != buf[len-1-i])
      return false;
  return true;
  /*ostringstream oss;
  oss << x;
  string s = oss.str();
  string r = s;
  reverse(r.begin(), r.end());
  return s == r;
  */
}

bool palin[10000010];
int main () {
  for(int i = 0; i <= 10000000; ++i)
    palin[i] = ispalindrome(i);

	int T;
	cin >> T;

  vector<string> b(4);
	for(int t = 0; t < T; ++t) {
    long long a, b;
    cin >> a >> b;

    int start = sqrt(a) - 10; if(start < 0) start = 0;
    int end =  sqrt(b) + 10;
    int fc = 0;
    for(long long x = start; x <= end; ++x) {
      if(x*x < a || x*x > b)
        continue;

      //if(!ispalindrome(x))
      if(!palin[x])
        continue;

      if(!ispalindrome(x*x))
        continue;
      fc++;
    }
    cout << "Case #" << t+1 << ": " << fc << endl;
	}
	return 0;
}
