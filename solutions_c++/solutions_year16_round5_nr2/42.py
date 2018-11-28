#include <cstdio>
#include <iostream>
#include <vector>
#include <algorithm>
#include <cstdlib>
using namespace std;

const int MAXN = 111;
int T;
int N, M;
int par[MAXN];
int gone[MAXN];
char labels[MAXN];
char cool[MAXN][MAXN];
char output[MAXN];

int size[MAXN];

double cnt[MAXN];

void runSim() {
  vector<int> remaining;
  for(int i = 1; i <= N; ++i) {
    remaining.push_back(i);
    gone[i] = 0;
  }

  for(int i = 0; i < N; ++i) {
    int j = rand() % (remaining.size());
    int cur = remaining[j];
    while (par[cur] && !gone[par[cur]]) {
      cur = par[cur];
    }

    output[i] = labels[cur];
    for(int j = 0; j < remaining.size(); ++j) {
      if (remaining[j] == cur) {
        swap(remaining[j], remaining[remaining.size() - 1]);
        remaining.pop_back();
        gone[cur] = 1;
        break;
      }
    }
  }
  output[N] = 0;

//  printf("Ran trial, %s\n", output);
  for(int i = 0; i < M; ++i) {
    string a = output;
    string b = cool[i];
    if (a.find(b) != -1) {
      cnt[i] += 1;
    }
  }
}

int main() {
  scanf("%d", &T);
  for(int t = 1; t <= T; ++t) {
    scanf("%d", &N);
    for(int i = 1; i <= N; ++i) {
      scanf("%d", par + i);
    }
    scanf("%s", labels + 1);
    scanf("%d", &M);
    for(int i = 0; i < M; ++i) {
      scanf("%s", cool[i]);
    }
    printf("Case #%d:", t);
    for(int i = 0; i < M; ++i) {
      cnt[i] = 0;
    }
    int S = 100000;
    for(int i = 0; i < S; ++i) {
      runSim();
    }
    for(int i = 0; i < M; ++i) {
      printf(" %.3lf", cnt[i] / S);
    }
    printf("\n");
  }
}
