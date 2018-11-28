//
//  standing_ovation.cpp
//  test
//
//  Created by Anıl Anar on 11.04.2015.
//  Copyright (c) 2015 Videa. All rights reserved.
//

#include <cstdio>

using namespace std;

int test_cases, length;
char str[1001];
int s[1001];

void fill_s() {
  for(int i = 0; i < length; i++) {
    s[i] = str[i] - '0';
  }
}

void solve(int c) {
  int num = 0;
  int required = 0;
  for (int i = 0; i < length; i++) {
    int diff = i - num;
    num += s[i];
    if(diff > 0) {
      required += diff;
      num += diff;
    }
  }
  
  printf("Case #%d: %d\n", c, required);
}


int main() {
  freopen("File", "r", stdin);
  scanf("%d", &test_cases);
  
  for(int c = 1; c <= test_cases; c++) {
    scanf("%d", &length);
    length++;
    scanf("%s", str);
    fill_s();
    solve(c);
  }
  
  return 0;
}