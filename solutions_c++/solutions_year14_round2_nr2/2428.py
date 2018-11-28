#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cstring>
//#include <cmath>
using namespace std;

int main()
{
	int t;
	int cnt = 0;
	scanf ("%d", &t);
	while (t--) {
		int a, b, k;
		int s = 0;
		scanf ("%d %d %d", &a, &b, &k);
		for (int i = 0; i < a; i++) {
			for (int j = 0; j < b; j++) {
				if ((i & j) < k) s++;
			}
		}
		printf ("Case #%d: %d\n", ++cnt, s);
	}
	return 0;
}
