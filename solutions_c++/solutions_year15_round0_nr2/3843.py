//#include <iostream>
#include <cmath>
#include <vector>
#include <string>
#include <algorithm>
#include <fstream>
using namespace std;

ifstream cin("B-small-attempt0.in");
ofstream cout("B-small.out");

int main() {
    int T;
    cin >> T;
    int A[1001], V[1001], C[1001]; 
    for (int t=0; t<T; t++) {
      int D; cin >> D; int curmax=0, curmaxi=0, secmax = 0, secmaxi=0, curmaxall=0;
      for (int i=0; i<D; i++) { cin >> A[i]; if (A[i]>=curmax) curmax = A[i]; V[i] = A[i]; C[i] = 1; } 
      int truns = curmax; int zsofar = 0; curmaxall = curmax;
      while (zsofar < curmaxall) {curmax=0; curmaxi=0; secmax = 0; secmaxi=0;
        for (int i=0; i<D; i++) if (A[i]>curmax) { secmax = curmax; secmaxi = curmaxi; curmax = A[i]; curmaxi = i; } else if (A[i] > secmax) { secmax = A[i]; secmaxi = i; }
       if (curmax <= 2) break;
       int roundz = round((double)(V[curmaxi])/(double)(C[curmaxi]+1)); int cleft = V[curmaxi]-C[curmaxi]*roundz;
       A[curmaxi] = max(roundz,cleft); int newmax = max(A[curmaxi],secmax);
       zsofar += 1; truns = min(truns,newmax+zsofar); C[curmaxi]+=1;
      }
      cout << "Case #" << t+1 << ": " << truns << endl;
    }
return 0;
}
