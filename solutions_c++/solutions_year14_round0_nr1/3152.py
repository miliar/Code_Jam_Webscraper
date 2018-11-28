#include <iostream>
#include <algorithm>
#include <functional>
#include <deque>
#include <cstring>
#include <cstdio>
#include <cstdlib>

using namespace std;

int main()
{
  int T;

  int card[16];
  int row, v, pos;

  cin >> T;
  for (int i = 0; i < T; ++i) {
    for (int j = 0; j < 16; ++j) {
      card[j] = 0;
    }

    cin >> row;
    for (int j = 0; j < 4; ++j) {
      if (j != (row-1)) {
	cin >> v;
	cin >> v;
	cin >> v;
	cin >> v;
      } else {
	for (int k = 0; k < 4; ++k) {
	  cin >> v;
	  ++card[v-1];
	}
      }
    }

    cin >> row;
    for (int j = 0; j < 4; ++j) {
      if (j != (row-1)) {
	cin >> v;
	cin >> v;
	cin >> v;
	cin >> v;
      } else {
	for (int k = 0; k < 4; ++k) {
	  cin >> v;
	  ++card[v-1];
	}
      }
    }

    
    v = 0;
    for (int j = 0; j < 16; ++j) {
      if (card[j] == 2) {
	++v;
	pos = j+1;
      }
    }
    printf ("Case #%d: ", (i+1));
    if (v == 0) {
      printf ("Volunteer cheated!\n");
    } else if (v == 1) {
      printf ("%d\n", pos);
    } else {
      printf ("Bad magician!\n");
    }
  }
  
  return 0;
}

