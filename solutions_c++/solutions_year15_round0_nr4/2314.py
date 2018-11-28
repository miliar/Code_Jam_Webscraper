// https://code.google.com/codejam/contest/6224486/dashboard#s=p3

#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>

using namespace std;

int X, R, C;

int parse() {
  scanf("%d%d%d", &X, &R, &C);
}

bool solve() {
  if(X >= 7)
    return true;
  if((R*C) % X != 0)
    return true;
  if(X <= 2)
    return false;
  if(X > max(R, C))
    return true;
  if(X%2 && X/2 > min(R,C))
    return true;
  if((X+1)/2 > min(R, C))
    return true;
  if(X == 4 && (R == 2 || C == 2))
    return true;
  return false;
}

int main() {
  int T;
  scanf("%d", &T);
  for(int i = 0; i < T; i++) {
    parse();
    cout << "Case #" << i+1 << ": ";
    if(solve())
      cout << "RICHARD" << endl;
    else
      cout << "GABRIEL" << endl;
  }
}
