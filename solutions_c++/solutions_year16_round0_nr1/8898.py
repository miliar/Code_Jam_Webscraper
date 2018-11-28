#include <iostream>
#include <stdio.h>
#include <unordered_set>
using namespace std;

int countSleep(const int n) {
  if (n == 0) {
    return -1;
  }
  int notCounted = 10;
  unordered_set<int> s;
  int ret = 0;

  for (int i = n; notCounted; i += n) {
    int num = i;
    while (num && notCounted) {
      int tmp = num % 10;
      if (s.find(tmp) == s.end()) {
        s.insert(tmp);
        --notCounted;
      }
      num /= 10;
    }
    ret = i;
  }

  return ret;
}

int main(int argc, char const* argv[])
{
  int N;
  int num;
  int ret;

  scanf("%d", &N);

  for (int i = 0; i < N; ++i) {
    scanf("%d", &num);
    ret = countSleep(num);
    printf("Case #%d: ", i + 1);
    if (ret == -1) {
      printf("INSOMNIA\n");
    } else {
      printf("%d\n", ret);
    }
  }
  return 0;
}
