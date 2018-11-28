#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
#include <map>
#include <string>
#include <string.h>
#include <set>
#include <stdio.h>
#include <assert.h>
#include <sstream>
using namespace std;
int grid[4][4][2];
char pos[17];
int main(int argc, char* argv[]) {
  int nocases;
  cin >> nocases;
  getchar();
  for (int rr = 1; rr <= nocases; ++rr) {
    int a1, a2;
    memset(pos, 1, sizeof(pos));
    cin >> a1;
    for (int i = 0; i < 4; ++i)
      for (int j = 0; j < 4; ++j) {
	cin >> grid[i][j][0];
	if (i+1 != a1)
	  pos[grid[i][j][0]] = 0;
      }
    cin >> a2;
    for (int i = 0; i < 4; ++i)
      for (int j = 0; j < 4; ++j) {
	cin >> grid[i][j][1];
	if (i+1 != a2)
	  pos[grid[i][j][1]] = 0;
      }
    int x = -1;
    for (int i = 1; i <= 16; ++i)
      if (pos[i]) {
	if (x != -1) {
	  x = -2;
	  break;
	} else
	  x = i;	  
      }
    if (x == -1)
      printf("Case #%d: Volunteer cheated!\n", rr);
    else if (x == -2)
      printf("Case #%d: Bad magician!\n", rr);
    else
      printf("Case #%d: %d\n", rr, x);
  }
  return 0;
}
