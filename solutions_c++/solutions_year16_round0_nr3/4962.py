#include <iostream>
#include <algorithm>
#include <vector>
#include <string>

using namespace std;

int n = 16;
int j = 50;

uint64_t bconvert (bool* num, int b) {
  uint64_t res = 0;
  uint64_t cur = 1;
  for (int i = 0; i < n; i++) {
    res += cur * num[n-i-1];
    cur *= b;
  }
  return res;
}

void check (bool* num) {
  if (j == 0) return;
  int factors[9];

  uint64_t t;
  bool good = true;
  for (int i = 2; i <= 10; i++) {
    t = bconvert (num,i);
    good = false;
    for (int k = 2; k * k <= t; k++) {
      if (t % k == 0) {
        factors[i-2] = k;
        good = true;
        break;
      }
    }
    if (!good) break;
  }
  if (good) {
    //cout << "Case #" << 50-j+1 << ": ";
    for (int i =0; i < n; i++) {
      cout << num[i];
    }
    cout << " ";
    for (int i = 0; i < 9; i ++) {
      cout <<factors[i] << " ";
    }
    cout << endl;
    j --;
  }
}

void gen(bool* num, int cur) {
  if (j == 0) return;
  if (cur == n-1) {
    check (num);
  } else {
    num[cur] = 0;
    gen (num,cur+1);
    num[cur] = 1;
    gen(num,cur+1);
  }
}

int main () {
  cout << "Case #1: " << endl;
  bool num[n];
  num[0] = 1;
  num[n-1] = 1;

  gen (num,1);

}
