#include <cstdio>
#include <iostream>
#include <algorithm>
#include <vector>
#include <set>

using namespace std;

void solve() {
  int A,B,K,wyn=0,i,j;
  scanf("%d%d%d", &A, &B, &K);
  for (i=0; i<A; i++)
    for (j=0; j<B; j++)
      if ((i&j)<K)
	wyn++;
  printf("%d\n",wyn);
}

int main() {
  int n;
  scanf("%d", &n);
  for (int i=1; i<=n; i++) {
    printf("Case #%d: ", i);
    solve();
  }
  return 0;
}

/*
*/