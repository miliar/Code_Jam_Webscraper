#include <stdio.h>
#include <string.h>
#include <queue>
#include <map>
#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

int r, c, w;

int main (){

	freopen ("a-small.in", "r", stdin);
	freopen ("a-small.out","w",stdout);

	int t;
	scanf ("%d", &t);

	for (int tc = 1; tc <= t; tc++){
	
		scanf ("%d %d %d", &r, &c, &w);

		printf ("Case #%d: %d\n", tc, c/w + (c%w?1:0) -1 + w);
	}


	return 0;

}
