// https://code.google.com/codejam/contest/6224486/dashboard

#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>

using namespace std;

int N;
int Smax;
int S[1001];

int parse() {
  scanf("%d", &Smax);
  scanf(" ");
  for(int i =0; i <= Smax; i++) {
    char c;
    scanf("%c", &c);
    S[i] = c-'0';
  }
}

int solve() {
  int up = 0;
  int rep = 0;
  for(int i = 0; i <= Smax; i++) {
    if(up < i) {
      rep += i-up;
      up = i;
    }
    up += S[i];
  }
  return rep;
}

int main() {
  int T;
  scanf("%d", &T);
  for(int i =0; i < T; i++) {
    parse();
    cout << "Case #" << i+1 << ": " << solve() << endl;
  }
}
