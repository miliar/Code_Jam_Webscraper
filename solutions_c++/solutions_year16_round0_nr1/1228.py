#include <stdio.h>
#include <vector>
#include <string.h>
#include <iostream>
#include <sstream>

using namespace std;

string toString(long long n) {
  stringstream ss;
  ss << n;
  string s = ss.str();
  return s;
}

void solve() {
  long long n;
  bool visited[10];
  for(int i = 0; i < 10; i++) visited[i] = false;
  scanf("%lld", &n);
  if(n==0) {
    printf("INSOMNIA\n");
    return;
  }
  long long m = 0;
  long long mul = 1;
  int counter = 0;
  int l;
  string s;
  while(true) {
    m += n;
    s = toString(m);
    l = s.length();
    for(int i = 0; i < l; i++) {
      if(!visited[s[i]-'0']) {
        visited[s[i]-'0'] = true;
        counter++;
      }
    }
    if(m < 0) {
      printf("INSOMNIA\n");
      return;
    }
    if(counter > 9) break;
  }
  printf("%lld\n", m);
}

int main() {
  int t;
  scanf("%d", &t);
  for(int i = 1; i <= t; i++) {
    printf("Case #%d: ", i);
    solve();
  }
  return 0;
}
