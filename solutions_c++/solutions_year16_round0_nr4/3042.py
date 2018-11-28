#include<bits/stdc++.h>

using namespace std;

#define dbg(x) (cout<<#x<<" = "<<(x)<<'\n')

typedef long long int lld;
const int INF = (1LL << 30) - 1;
const lld LINF = (1LL << 62) - 1;

int K, C, S;

void solution() {
      scanf("%d%d%d", &K, &C, &S);

      for (int i = 1; i <= K; i++)
            printf("%d ", i);
      printf("\n");
}

int main() {
      cin.sync_with_stdio(false);

      #ifndef ONLINE_JUDGE
      freopen("input.txt", "r", stdin);
      freopen("output.txt", "w", stdout);
      #endif

      int nrtests;

      scanf("%d", &nrtests);

      for (int testcase = 1; testcase <= nrtests; testcase++) {
            printf("Case #%d: ", testcase);
            solution();
      }

      return 0;
}