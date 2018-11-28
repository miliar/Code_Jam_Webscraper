#include <bits/stdc++.h>

using namespace std;

string str;

int main() {
  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);
  int t;
  scanf("%d", &t);
  for(int test = 1; test <= t; test++) {
    int r = 0;
    cin >> str;
    for(int i = 0; i<str.size()-1; i++) {
      if(str[i] != str[i+1]) r++;
    }
    if(str[str.size()-1] == '-') r++;
    printf("Case #%d: %d\n", test, r);
  }
  return 0;
}
