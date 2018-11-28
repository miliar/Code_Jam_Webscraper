#include <cstdio>
#include <iostream>
#include <algorithm>
#include <string>
#include <cmath>
#include <cstdlib>
#include <cstring>

#define TYPE long long

using namespace std;

bool is_pal(TYPE n) {
  int l = floor(log10(n)) + 1;
  TYPE d = 1, f = pow(10, l - 1);
  
  for (int i = 0; i <= l/2; i++) {
    if ((n/d)%10 != (n/f)%10) {
      return false;
    }

    d *= 10;
    f /= 10;
  }
  
  return true;
}

void alg() {
  TYPE A, B;
  TYPE a, b;
  TYPE result = 0;

  cin >> A >> B;
  a = ceil(sqrt(A));
  b = floor(sqrt(B));
  
  for (int i = a; i <= b; i++) {
    if (is_pal(i))
      if (is_pal(i*i)) {
	result++;
      }
  }
    
  cout << result << endl;
}

int main() {
    int n_cases;
    cin >> n_cases;
    
    for (int test_case = 1; test_case <= n_cases; test_case++) {
      cout << "Case #" << test_case << ": ";
      alg();
    }

    return EXIT_SUCCESS;
}
