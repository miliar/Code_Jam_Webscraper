#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <queue>

#include <assert.h>
#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <memory.h>
#include <time.h>

#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>

using namespace std;

typedef long long ll;

double all[300];
int k;
int n;
double calc(int x1, int x2) {
  //assert( x1<=x2);
  //assert(x2<=n-(k-x1));

  double prob[300][300]; // prob[i+1][j] is prob i yes's after j votes
  for(int i=0; i<=n+2;i++) {
    prob[i][0]=0;
    prob[0][i]=0;
  }
  prob[1][0]=1;
  for(int j=0; j<x1; j++) {
    double p=all[j];
    //    cout << j << endl;
    for(int i=1; i<=n+1;i++) {
      prob[i][j+1]=p*prob[i-1][j]+(1-p)*prob[i][j];
    }
  }

  double p=all[x2];
  // cout << x1 << endl;
  for(int i=1; i<=n+1;i++) {
    prob[i][x1+1]=p*prob[i-1][x1]+(1-p)*prob[i][x1];
  }
  
  
  for(int j=n-(k-x1)+1; j<n; j++) {
    double p=all[j];
    int it=j-n+k;
    //cout << it << endl;
    for(int i=1; i<=n+1;i++) {
      prob[i][it+1]=p*prob[i-1][it]+(1-p)*prob[i][it];
    }
  }

  return prob[1+(k/2)][k];
}


int main()
{
  freopen("red.in", "r", stdin);
  freopen("red.out", "w", stdout);

  int t2;
  cin >> t2;
  for (int t1 = 1; t1 <= t2; ++t1) {
    printf("Case #%d: ", t1);
    cin >> n >> k;
    for(int i = 0; i < n; i++) {
      cin >> all[i];
    }
    sort(all, all+n);
    double best=0;
      /*
    for(int i =0; i < n; i++) {
      cout << all[i] << " ";
    }
    cout << endl;
    cout << calc((k/2)-1,(k/2)-1) << endl;*/
    for(int i=0; i<k;i++) {
      for(int j=i; j<n+i-(k-1); j++) {
	//cout << "calc: " << i << " " << j << " " << calc(i,j) << endl;
	best = max(best, calc(i,j));
      }
    }
    cout << best;
				
    printf("\n");
  }
  return 0;
}
