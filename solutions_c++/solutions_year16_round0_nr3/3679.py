#include <iostream>
#include <cstdio>
#include <algorithm>
#include <string>

using namespace std;

typedef long long LL;

const int N = 16;

int T;
int n, m;
int d[50];

void generate(int x)
{
  d[0] = d[N - 1] = 1;
  int tx = x;
  for (int i = 1; i <  N - 1; i += 2) {
    int t = tx % 2;
    if (t) {
      d[i] = d[i + 1] = 1;
    }
    else {
      d[i] = d[i + 1] = 0;
    }
    tx /= 2;
  }
}

void print()
{
  for (int i = 0; i < N; i++) {
    printf("%d", d[i]);
  }
  for (int i = 2; i <= 10; i++) {
    printf(" %d", i + 1);
  }
  printf("\n");
}

void work()
{
  for (int i = 0; i < m; i++) {
    generate(i);
    print();
  }
}

int main()
{
  freopen("data.in", "r", stdin);
  freopen("data.out", "w", stdout);
  scanf("%d", &T);
  scanf("%d%d", &n, &m);
  printf("Case #%d:\n", 1);
  work();
}
