#include <algorithm>
#include <assert.h>
#include <climits>
#include <cstring>
#include <string>
#include <vector>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <list>
#include <cmath>
#include <ext/hash_map>
#include <ext/hash_set>
#include <fstream>
#include <iostream>
#include <sstream>
#include <numeric>
#include <limits>
#include <iomanip>
using namespace std;

namespace __gnu_cxx {
template<> struct hash< std::string > {
  size_t operator()( const std::string& x ) const {
    return hash< const char* >()( x.c_str() );
  }
};
}

using __gnu_cxx::hash_map;

#define sz(a) ((int)a.size())
#define all(a) a.begin(), a.end()
#define LL long long
#define LD long double
#define vi vector<int>
#define vl vector<LL>
#define vs vector<string>
#define vb vector<bool>
#define ii pair<int, int>
#define vii vector<ii>
#define SET(v, i) (v | (1 << i))
#define CLEAR(v, i) (v & (1 << i))
#define TOGGLE(v, i) (v ^ (1 << i))

template <typename T, template<typename ELEM, typename ALLOC=std::allocator<ELEM> > class Container>
void Print(const Container<T>& v, const string& delimeter = " ") {
  for (typename Container<T>::const_iterator it = v.begin(); it != v.end(); ++it) {
    cout << *it << delimeter;
  }

  cout << endl;
}

template <class T>
void Print(const T& v, const string& delimeter = "\n") {
  cout << v << delimeter;
}
vl nums;

bool Pal(LL num) {
  char arr[20];
  sprintf(arr, "%lld", num);
  int n = strlen(arr);
  for (int i = 0; i < n / 2; ++i) {
    if (arr[i] != arr[n - 1 - i])
      return false;
  }

  return true;
}

void Generate() {
  for (LL i = 1; i <= 10 * 1000 * 1000; ++i) {
    if (Pal(i) && Pal(i * i))
      nums.push_back(i * i);
  }
}

LL Solve(LL a, LL b) {
  LL ret = 0;
  for (int i = 0; i < sz(nums); ++i) {
    //if (nums[i] > b) break;
    //if (nums[i] < a) continue;
    if (nums[i] >= a && nums[i] <= b)
      ++ret;
  }

  return ret;
}

int main() {
  int t;
  LL a, b;
  Generate();
  scanf("%d", &t);
  for (int cases = 1; cases <= t; ++cases) {
    scanf("%lld %lld", &a, &b);
    printf("Case #%d: %lld\n", cases, Solve(a, b));
  }
  return 0;
}
