#include <stdio.h>
#include <string.h>
#include <vector>

#define MAX 2510
using namespace std;

int a[MAX];
vector<int> p;

int main(int argc, char const *argv[])
{
  int T, N;
  scanf("%d", &T);
  for (int i = 0; i < T; i++) {
    scanf("%d", &N);
    p.clear();
    memset(a, 0, MAX*4);

    int size = 2*N - 1;
    int tmp;
    for (int j = 0; j < size; j++) {
      for (int k = 0; k < N; k++) {
        scanf("%d", &tmp);
        //printf("%d ", tmp);
        a[tmp]++;
      }
    }
    // for (int j = 0; j < MAX; j++) {
    //   printf("%d ", a[j]);
    // }
    for (int j = 0; j < MAX; j++) {
      if (a[j] % 2 != 0) p.push_back(j);
    }

    printf("Case #%d: ", i+1);
    size = p.size();
    for (int j = 0; j < size; j++) {
      printf("%d ", p[j]);
    }
    printf("\n");
  }
  return 0;
}