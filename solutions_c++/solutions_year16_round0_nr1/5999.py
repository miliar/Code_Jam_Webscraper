#include <iostream>
#include <fstream>
#include <cstdlib>
#include <vector>
#include <string>
#include <cmath>
#include <algorithm>
using namespace std;

ifstream in("data.in");
ofstream out("data.out");

bool seen[10];
int numSeen;

long long getLast(int n);
void clearEverything();
void update(int x);

int main() {
  int t;
  
  in >> t;

  for (int c = 1; c <= t; c++) {
    int n;
    in >> n;

    out << "Case #" << c << ": ";
    long long last = getLast(n);
    if (last == -1) {
      out << "INSOMNIA";
    } else {
      out << last;
    }
    out << endl;
  }
}

long long getLast(int n) {
  if (n == 0) return -1;
  clearEverything();

  long long x = n;
  for (int i=0; i<100; i++, x+=n) {
    update(x);
    if (numSeen == 10) {
      return x;
    }
  }
  return -1;
}

void clearEverything() {
  numSeen = 0;
  for (int i=0; i<10; i++) {
    seen[i] = false;
  }
}

void update(int x) {
  while (x > 0) {
    int y = x%10;
    if (!seen[y]) {
      numSeen++;
      seen[y] = true;
    }
    x /= 10;
  }
}
