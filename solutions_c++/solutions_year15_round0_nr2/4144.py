#include <iostream>
#include <stdio.h>
#include <string.h>
#include <vector>
#include <algorithm>
#include <math.h>

using namespace std;

class Dish {
  public:
    int num;
    double div;
    Dish () {}
    Dish (int,double);
    int avg (void) {return ceil(num/div);}
    int avg1 (void) {return ceil(num/(div+1.0));}
};

Dish::Dish (int n, double d) {
  num = n;
  div = d;
}

bool comp(const Dish& a, const Dish& b) {
  return ceil(a.num/a.div) > ceil(b.num/b.div);
}

int main() {

  int T;
  cin >> T;

  for (int x=1; x<=T; ++x) {

    int D;
    cin >> D;
    vector<Dish> P;
    int p;

    for (int i=0; i<D; ++i) {
      cin >> p;
      Dish pa (p,1);
      P.push_back(pa);
    }

    sort(P.begin(), P.end(), comp);

    int cost = 0;
    int total = 0;
    int max = P[0].avg();

    while ( cost < ( P[0].avg() - P[0].avg1() ) ) {
      P[0].div += 1;
      sort(P.begin(), P.end(), comp);
      cost++;
      int benefit = max - P[0].avg();
      if (benefit>=cost) {
        total += cost;
        max = P[0].avg();
        cost = 0;
      }
    }

    printf("Case #%i: %i\n", x, max + total);
  }
  return 0;
}
