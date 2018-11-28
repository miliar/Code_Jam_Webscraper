#include <cstdio>

using namespace std;

void run(int t) {
  char shyness[1001];
  int smax;
  scanf("%d %s", &smax, shyness);
  int acc = 0;
  int inv = 0;
  for (int i = 0; i <= smax; i++) {
    if (acc < i) {
      inv += (i - acc);
      acc = i;
    }
    int thisLevel = shyness[i] - '0';
    acc += thisLevel;
  }
  printf("Case #%d: %d\n", t, inv);
}


int main() {
  int T;
  scanf("%d", &T);
  for (int i = 0; i < T; i++) {
    run(i+1);
  }
}
