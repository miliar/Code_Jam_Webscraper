#include <algorithm>
#include <bitset>
#include <cassert>
#include <cctype>
#include <cmath>
#include <complex>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <deque>
#include <exception>
#include <fstream>
#include <functional>
#include <iomanip>
#include <iostream>
#include <limits>
#include <list>
#include <locale>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <string>
#include <typeinfo>
#include <utility>
#include <vector>

using namespace std; 

int main(){
  int n;
  cin >> n;
  for (int i = 1; i <=   n; ++i) {
    int m;
    cin >> m;
    if (m == 0) {
      printf("Case #%d: INSOMNIA\n", i);
      continue;
    }
    int a[10];
    for (int j = 0; j < 10; ++j) {
      a[j] = 0;
    }
    for (int j = 1;; ++j) {
      int temp = j * m;
      while (temp) {
        a[temp % 10] = 1;
        temp /= 10;
      }
      bool done = true;
      for (int k = 0; k < 10; ++k) {
        if (a[k] == 0) {
          done = false;
          break;
        }
      }
      if (done) {
        printf("Case #%d: %d\n", i, j * m);
        break;
      }
    }
  }
  return 0;
}
