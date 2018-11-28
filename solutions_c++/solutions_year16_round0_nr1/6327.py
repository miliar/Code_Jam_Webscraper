#include <cstdio>
#include <cstdlib>
#include <fstream>

using namespace std;

bool marked[10];

void mark(int num) {
  while (num > 0) {
    marked[num % 10] = true;
    num /= 10;
  }
}

bool allMarked() {
  for (int i = 0; i < 10; i++) {
    if (!marked[i]) {
      return false;
    }
  }
  return true;
}

int main() {
  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);

  int T;
  scanf("%d", &T);
  for (int i = 0; i < T; i++) {
    int N;
    scanf("%d", &N);

    if (N == 0) {
      printf("Case #%d: INSOMNIA\n", i + 1);
      continue;
    }

    int last = N;
    memset(marked, false, sizeof(marked));

    mark(last);
    while (!allMarked()) {
      last += N;
      mark(last);
    }
    printf("Case #%d: %d\n", i + 1, last);
  }

  return 0;
}
