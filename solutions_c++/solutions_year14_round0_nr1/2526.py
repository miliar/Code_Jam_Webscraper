#include <bits/stdc++.h>
using namespace std;
typedef unsigned long long ull;
typedef pair<int,int> ii;

int main() {
  int tests;
  scanf("%d", &tests);
  for(int i = 1; i <= tests; ++i) {
    int m[2][4][4];
    int yy[2];
    for(int j = 0; j < 2; ++j) {
      scanf("%d", &yy[j]);
      --yy[j];
      for(int y = 0; y < 4; ++y)
	for(int x = 0; x < 4; ++x)
	  scanf("%d", &m[j][x][y]);
    }
    int count[17] = {0};
    int dupes = 0;
    for(int j = 0; j < 2; ++j) {
      for(int x = 0; x < 4; ++x) {
	int num = m[j][x][yy[j]];
	if(count[num] != 0) {
	  ++dupes;
	}
        ++count[num];
      }
    }
    printf("Case #%d: ", i);
    if(dupes == 0) {
      printf("Volunteer cheated!");
    } else if(dupes == 1) {
      for(int i = 0; i <= 16; ++i) {
	if(count[i] == 2) {
	  printf("%d", i);
	}
      }
    } else {
      printf("Bad magician!");
    }
    printf("\n");
  }
}

