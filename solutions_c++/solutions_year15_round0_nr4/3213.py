#include <iostream>
#include <limits>
#include <algorithm>
#include <cassert>
using namespace std;

#define YES "GABRIEL"
#define NO  "RICHARD"

size_t minlength(size_t x){
  switch (x){
    case 1U: case 2U: return 1U;
    case 3U: case 4U: return 2U;
    default:          assert(!!!"value of x not handled by minlength");
  }
}

size_t holesize(size_t x){
  switch (x){
    case 1U: case 2U: case 3U: return 0U;
    case 4U:                   return 2U;
    default:                   assert(!!!"value of x not handled by holesize");
  }
}

const char* possible(size_t x, size_t r, size_t c){
  if (r * c % x) return NO;
  size_t m = min(r, c);
  if (m < minlength(x)) return NO;
  if (m <= holesize(x)) return NO;
  return YES;
}

int main(){
  size_t T; cin >> T;
  for (size_t i = 1; i <= T; ++i){
    size_t X, R, C; cin >> X >> R >> C;

    cout << "Case #" << i << ": " << possible(X, R, C) << endl;
  }
}
