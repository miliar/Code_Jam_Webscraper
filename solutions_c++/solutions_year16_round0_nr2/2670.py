#include <stdio.h>
#include <vector>
#include <algorithm>
#include <utility>
#include <queue>
#include <map>
#include <tuple>
#include <string>
#include <iostream>

using namespace std;

int main() {
  int n;
  scanf(" %d ", &n);
  for (int i = 0; i < n; i++) {
    char tmp[200];
    scanf(" %s ", tmp);
    string input = tmp;
    int ans = 0;
    char last = '+';
    for(auto it = input.rbegin(); it != input.rend(); it++){
      if(*it != last) {
        ans ++;
        last = *it;
      }
    }
    printf("Case #%d: %d\n", i+1, ans);
  }
}
