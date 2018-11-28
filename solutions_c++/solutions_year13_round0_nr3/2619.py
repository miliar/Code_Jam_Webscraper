#include <iostream>
#include <map>
#include <vector>
#include <list>
#include <cmath>
#include <cstring>

using namespace std;

bool isFair(unsigned i)
{
  char str[16];
  sprintf(str, "%d", i);
  int n = strlen(str);
  
  for (int a = 0; a <= n/2; a++) {
    if (str[a] != str[n-1-a]) {
      return false;
    }
  }

  return true;
}

int main(int argc, char* argv[])
{
  unsigned T;
  cin >> T;

  for (auto t = 1; t <= T; t++) {
    unsigned A, B;
    cin >> A >> B;
    
    // Squares end in 0, 1, 4, 5, 6 or 9
    // We don't care about the ones ending in 0 (not fair)

    unsigned min = sqrt(A);
    if (min*min < A) {
      min++;
    }
    unsigned max = sqrt(B);
    
    unsigned result = 0;
    for (auto i = min; i <= max; i++) {
      if (isFair(i) && isFair(i*i)) {
	result++;
      }
    }

    cout << "Case #" << t << ": " << result << endl;
  }

  return 0;
}
