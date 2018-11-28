// Author: Death.Light

#include <cmath>
#include <cstdio>
#include <conio.h>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <algorithm>

using namespace std;

void testcase (int numtest) {
	double c, f, x, time, basecake;
	time = 0;
	basecake = 2;	
	cin >> c >> f >> x;
	do {
		if ((x / basecake) > (c / basecake + x / (basecake + f))) {
			time += c / basecake;
			basecake += f;			
		} else {
			time += x / basecake;
			break;
		}
	} while (1);
	printf ("Case #%d: %.9f", numtest, time);
	printf ("\n");
}

int main () {
  freopen ("Death.Light", "r", stdin);
  freopen ("Light.Death", "w", stdout);
  int test;
  cin >> test;
  for (int i = 1; i <= test; i++) testcase (i);
  return 0;
}

