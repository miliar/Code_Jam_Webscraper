//
//  main.cpp
//  bsuir2016
//
//  Created by Artjom Bastun on 3/28/16.
//  Copyright © 2016 Artjom Bastun. All rights reserved.
//

#include <iostream>
#include <string.h>
#include <algorithm>

using namespace std;

bool isAllDigitsThere(int d[10]) {
  for (int i = 0; i <= 9; ++i) {
    if (d[i] == 0) {
      return false;
    }
  }
  return true;
}

int count_ans(int x) {
  int digits[10];
  for (int i = 0; i <=9; i++) {
    digits[i] = 0;
  }
  int ans = 0;
  do {
    ans++;
    int num = x * ans;
    while (num > 0) {
      digits[num % 10] = 1;
      num /= 10;
    }
  } while (!isAllDigitsThere(digits));
  return x * ans;
}

int main(int argc, const char * argv[]) {
  freopen("/Users/stunba/Projects/bsuir2016/bsuir2016/input.txt", "r", stdin);
  freopen("/Users/stunba/Projects/bsuir2016/bsuir2016/output.txt", "w", stdout);
  int n;
  cin >> n;
  
  int x = 0;
  for (int i = 0; i < n; i++) {
    cin >> x;
    cout << "Case #" << i+1 << ": ";
    if (x == 0) {
      cout << "INSOMNIA" << endl;
    }
    else {
      cout << count_ans(x) << endl;
    }
  }
  
  return 0;
}
