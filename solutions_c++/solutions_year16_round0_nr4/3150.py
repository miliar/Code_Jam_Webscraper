#include<cstdio>
#include<cstring>

#define N 100
#define ll long long

void solve(int K, int C, int S, ll set[N], int& size) {
  if (S < K) {
    size = 0;
    return;
  }

  for (int i = 0; i < K; i ++) {
    set[i] = i+1;
  }
 
  size = K;
  return;
}

int main()
{
  int t = 0;
  scanf("%d", &t);
  for (int i = 1; i <= t; i++) {
    int K, C, S;
    scanf("%d%d%d", &K, &C, &S);
    ll set[N];
    memset(set, -1, sizeof(ll)*N);
    int set_size = 0;

    solve (K,C,S, set, set_size);
    if (set_size == 0)
      printf("Case #%d: IMPOSSIBLE\n", i);
    else {
      printf("Case #%d:", i);
      for (int j = 0; j < set_size; ++j)
        printf(" %lld", set[j]);
      printf("\n");
    }
  }
  return 0;
}
