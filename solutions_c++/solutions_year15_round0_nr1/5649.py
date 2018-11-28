#include <iostream>
#include <cstdlib>
#include <cstdio>
using namespace std;

int main()
{
  int t, caseN = 1, s;
  string aud;
  cin >> t;
  while (t--) {
    cin >> s >> aud;

    int sum = (aud[0]-'0'), count = 0;
    for (int i = 1; i <= s; i++) {
      if (sum < i) {
	count += i - sum;
	sum += i - sum;
      }
      sum += (aud[i] - '0');
    }

    printf("Case #%d: %d\n", caseN++, count);
  }

  return 0;
}
