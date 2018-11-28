#include <stdio.h>
#include <vector>
#include <algorithm>
#include <string>
#include <iostream>

using namespace std;

long long myPow(long long x, long long e) {
  long long result;

  if (e == 0) result = 1;
  else if (e == 1) result = x;
  else {
    result = myPow(x, e / 2);
    result = result * result;
    if (e % 2) result = result * x;
  }
  return result;
}

void solve() {
    long long b;
    long long m;
    scanf("%lld %lld", &b, &m);
    long long maxPaths = myPow(2, b-2);
    if(maxPaths < m) {
        printf("IMPOSSIBLE\n");
        return;
    } else {
        printf("POSSIBLE\n");
    }
    int mat[50][50];
    for(int i = 0; i < 50; i++) {
        for(int j = 0; j < 50; j++) {
            mat[i][j] = 0;
        }
    }
    for(int i = 1; i < 50; i++) {
        for(int j = i+1; j < 50; j++) {
            mat[i][j] = 1;
        }
    }
    if(maxPaths==m) {
        mat[0][b-1] = 1;
        m--;
    }
    maxPaths = maxPaths / 2;
    int i = 1;
    while(m != 0) {
        if(m/maxPaths==1) {
            m = m - maxPaths;
            mat[0][i] = 1;
        }
        maxPaths = maxPaths / 2;
        i++;
    }
    for(int i = 0; i < b; i++) {
        for(int j = 0; j < b; j++) {
            printf("%d", mat[i][j]);
        }
        printf("\n");
    }
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
