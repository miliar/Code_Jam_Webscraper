#include <iostream>
#include <vector>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <unordered_map>
#include <queue>

#define max(a, b) ((a) > (b) ? (a) : (b))
#define min(a, b) ((a) < (b) ? (a) : (b))
#define MAX_N 401

using namespace std;

string a;

char reverse(char ch) {
  return ch == '+' ? '-' : '+';
}

void rotate(int pos) {
  for (int i = 0; i <= pos / 2; ++i) {
    char tmp = a[i];
    a[i] = reverse(a[pos - i]);
    if (i != pos - i) {
      a[pos - i] = reverse(tmp);
    }
  }
}

int transform(int n) {
  if (n == 1) {
    return a[0] == '+' ? 0 : 1;
  }
  int end = n - 1;
  while(a[end] == '+' && end >= 0) {
    end--;
  }
  if (end == -1) { // 说明全部是笑脸朝上
    return 0;
  }

  int pos = 0;
  while (a[pos] == '+' && pos <= end) {
    pos++;
  }
  int rotateCount = 0;
  if (pos > 0) {
    rotate(pos - 1);
    rotateCount++;
  }
  rotate(end);
  rotateCount++;
  return transform(end + 1 - pos) + rotateCount;
}

int main() {
  int T;
  cin >> T;
  for (int cnt = 1; cnt <= T; ++cnt) {
    cin >> a;
    int len = a.length();
    printf("Case #%d: %d\n", cnt, transform(len));
  }
  return 0;
}
