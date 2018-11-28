#include <cstdio>
#include <iostream>
#include <cassert>
#include <ctime>
#include <cmath>
#include <cstring>
#include <cstdlib>
#include <string>
#include <vector>
#include <set>

using namespace std;

typedef long long int int64;
typedef long double ext;

#define pb push_back
#define mp make_pair
#define fs first
#define sc second
#ifdef LOCALD
#define eprintf(...) fprintf(stderr, __VA_ARGS__)
#else
#define eprintf(...) {}
#endif

int T;

const int size = 4;

int x, y;
int a;
bool c1[size * size];
bool c2[size * size];

int main() {
  assert(scanf("%d", &T) == 1);
  for (int test = 1; test <= T; test++) {
    for (int i = 0; i < size * size; i++)
      c1[i] = c2[i] = false;
    assert(scanf("%d", &x) == 1);
    x--;
    for (int i = 0; i < size; i++)
      for (int j = 0; j < size; j++) {
        assert(scanf("%d", &a) == 1);
        a--;
        if (i == x)
          c1[a] = true;
      }
      
    assert(scanf("%d", &y) == 1);
    y--;
    for (int i = 0; i < size; i++)
      for (int j = 0; j < size; j++) {
        assert(scanf("%d", &a) == 1);    
        a--;
        if (i == y)
          c2[a] = true;
      }
    int cnt = 0;
    int id = -1;
    for (int i = 0; i < size * size; i++) 
      if (c1[i] && c2[i]) {
        id = i;
        cnt++;
      }
    printf("Case #%d: ", test);
    if (cnt == 1)
      printf("%d", id + 1);
    else if (cnt == 0)
      printf("Volunteer cheated!");
    else
      printf("Bad magician!");
    printf("\n");
  }
  return 0;
}