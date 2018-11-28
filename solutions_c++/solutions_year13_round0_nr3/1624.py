#include <cstdio>
#include <string.h>
#include <iostream>
#include <vector>
using namespace std;

vector<long long> result;

bool is_palindrome(long long a) {
  char buffer[20];
  sprintf(buffer, "%lld", a);
  int len = strlen(buffer);
  int i, j = len - 1;
  for (i = 0; i < j; ++i, --j) {
    if (buffer[i] != buffer[j]) {
      return false;
    }
  }
  return true;
}

void init() {
  result.clear();
  long long i;
  for (i = 1; i <= 10000000; ++i) {
    if (is_palindrome(i)) {
      if (is_palindrome(i * i)) {
        result.push_back(i * i);
      }
    }
  }
}

int find(long long index) {
  int low = 0;
  int high = result.size() - 1;
  while (low < high - 1) {
    int mid = ((high - low) >> 1) + low;
    if (result[mid] > index) {
      high = mid;
    } else {
      low = mid;
    }
  }
  if (result[low] == index) {
    return low;
  }
  return high;
}

int main() {
  int cases;
  cin >> cases;
  int i;
  long long low, high;
  init();
  for (i = 1; i <= cases; ++i) {
    cin >> low >> high;
    int index_low = find(low);
    int index_high = find(high);
    if (result[index_high] > high) {
      index_high--;
    }
    cout << "Case #" << i << ": " << index_high - index_low + 1 << endl;
  }
  return 0;
}

