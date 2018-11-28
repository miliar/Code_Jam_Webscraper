
#include<stdlib.h>
#include<iostream>
#include<vector>
#include<string>
#include <cstdio>
using namespace std;
int main() {

  int T;

  cin >> T;

  for (int t = 0; t < T; ++t) {
      double C, F, X;

      cin >> C >> F >> X;

      double prod = 2.0;
      double prevRest = X;
      double rest = X/prod;

      double tFarm = 0;
      while(rest < prevRest) {
        // Time to create a farm
        prevRest = rest;
        tFarm += C/prod;
        prod += F;

        // New production time
        rest = tFarm + X/prod;
        
      }

      printf("Case #%d: %0.7f\n", t+1, prevRest);
  }

  return EXIT_SUCCESS;
}
