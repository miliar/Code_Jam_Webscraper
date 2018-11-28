#include <cstdio>
#include <iostream>
#include <cstring>
#include <set>
#include <algorithm>

using namespace std;

const int MaxN = 10010;

multiset <int> S;
int N, X, a[MaxN];

void solve (int tc) {
  S.clear();
  scanf("%d %d",&N,&X);
  for (int i = 0; i < N; ++i)
    scanf("%d",&a[i]);
  sort(a, a + N);

  int res = 0;

  for (int i = N - 1; i >= 0; --i)
    if (!S.empty()) {
      set <int> :: iterator it = S.lower_bound(a[i]);
      if (it != S.end() && *it >= a[i]) 
	S.erase(it);
      else {
	++res;
	S.insert(X - a[i]);
      }
    }
    else {
      ++res;
      S.insert(X - a[i]);
    }

  printf("Case #%d: %d\n",tc,res);
}

int main (void) {
  int t;
  scanf("%d",&t);
  for (int c = 1; c <= t; ++c)
    solve(c);
  return 0;
}
