#include <bits/stdc++.h>
using namespace std;
typedef unsigned long long ull;
typedef pair<int,int> ii;

int main() {
  int tests;
  scanf("%d", &tests);
  for(int i = 1; i <= tests; ++i) {
    int n;
    scanf("%d", &n);
    vector<double> vN (n);
    vector<double> vK (n);
    for(int j = 0; j < n; ++j) {
      scanf("%lf", &vN[j]);
    }
    for(int j = 0; j < n; ++j) {
      scanf("%lf", &vK[j]);
    }
    sort(vN.begin(), vN.end());
    sort(vK.begin(), vK.end());
    int lN = 0, rN = n - 1, lK = 0, rK = n - 1;
    int scoreD = 0;
    while(rN >= lN) {
      if(vN[lN] < vK[lK]) {
	--rK;
	++lN;
      } else {
	++lK;
	++lN;
	++scoreD;
      }
    }
    int scoreW = 0;
    lN = 0, rN = n - 1, lK = 0, rK = n - 1;
    while(rN >= lN) {
      if(vK[rK] > vN[rN]) {
	--rK;
	--rN;
      } else {
	++lK;
	--rN;
	++scoreW;
      }      
    }
    printf("Case #%d: %d %d \n", i, scoreD, scoreW);
  }
}

