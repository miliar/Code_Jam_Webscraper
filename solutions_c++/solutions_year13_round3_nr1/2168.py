#include <cstdio>
#include <iostream>
#include <algorithm>
#include <string>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <gmpxx.h>

#define LEN 1000005

using namespace std;

bool T[26] = {true, false, false, false, true, false, false, false, true, false, false, false, false, false, true, false, false, false, false, false, true, false, false, false, false, false};

void alg() {
  string L;
  int n, result(0);
  
  int beg = -1, last(0);
  
  cin >> L >> n;
  
  for (int i(0); i < L.size(); i++) {
    /**/
    if (!T[L[i] - 'a']) {
      if (-1 == beg) {
	beg = i;
      }
    }
    else if (-1 != beg) {
      if (n <= i - beg) {
	result += (beg - last + 1)*(L.size() - beg - n + 1);
	result += (i - beg - n)*(L.size() - i + 1);
	result += (i - beg - n)*(i - beg - n - 1)/2;
	last = i - n + 1;
      }
      beg = -1;
    }
    /**/
  } 
  
  int i(L.size());
  if (-1 != beg && n <= i - beg) {
    result += (beg - last + 1)*(L.size() - beg - n + 1);
    result += (i - beg - n);
    result += (i - beg - n)*(i - beg - n - 1)/2;
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
