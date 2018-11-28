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

int main(int argc, const char * argv[]) {
  freopen("/Users/stunba/Projects/bsuir2016/bsuir2016/input.txt", "r", stdin);
  freopen("/Users/stunba/Projects/bsuir2016/bsuir2016/output.txt", "w", stdout);
  int t;
  cin >> t;
  
  for (int tc = 0; tc < t; ++tc) {
    char str[1002], ans[2002];
    cin >> str;
    printf("Case #%d: ", tc+1);
    int l = strlen(str);
    int r = l;
    ans[l] = str[0];
    for (int i = 1; i < strlen(str); ++i) {
      if (str[i] >= ans[l]) {
        ans[--l] = str[i];
      }
      else {
        ans[++r] = str[i];
      }
    }
    for (int i = l; i <= r; ++i) {
      cout << ans[i];
    }
    cout << endl;
  }
  
  return 0;
}