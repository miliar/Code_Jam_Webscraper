#include <cstdio>
#include <iostream>

using namespace std;

int main() {
  int T; scanf("%d\n", &T);
  for (int tt = 1; tt <= T; ++tt) {
  	int a[4][4], b[4][4];
  	int x, y;
  	cin >> x;
  	for (int i = 0; i < 4; ++i) {
  		for (int j = 0; j < 4; ++j) {
  			cin >> a[i][j];
  		}
  	}
  	cin >> y;
  	for (int i = 0; i < 4; ++i) {
  		for (int j = 0; j < 4; ++j) {
  			cin >> b[i][j];
  		}
  	}
  	int c[17];
  	for (int i = 1; i <= 16; ++i) {
  		c[i] = 0;
  	}
  	for (int i = 0; i < 4; ++i) {
  		++c[a[x - 1][i]];
  		++c[b[y - 1][i]];
  	}
  	int k = 0;
  	for (int i = 1; i <= 16; ++i) {
  		if (c[i] == 2) {
  			if (k) {
  				k = -1;
  				break;
  			}
  			k = i;
  		}
  	}
    printf("Case #%d: ", tt);
    if (k > 0) printf("%d", k);
    else if (k == 0) printf("Volunteer cheated!");
    else printf("Bad magician!");
    putchar('\n');
  }
  return 0;
}

