#include "cmath"
#include "cstdio"
#include "algorithm"
#include "map"
#include "numeric"
#include "queue"
#include "set"
#include "string"
#include "utility"
#include "vector"
#include <iostream>
using namespace std;
typedef long long i64;

int main() {
	int T, Smax; scanf_s("%d", &T);
	string audiance;
	int standing = 0;
	int friends = 0;
	for (int Ti = 1; Ti <= T; ++Ti) {
		fprintf(stderr, "Case #%d of %d...\n", Ti, T);
		standing = 0;
		friends = 0;
		int S = 0;
		scanf_s("%d", &Smax);
		cin >> audiance;
		for (int i = 0; i <= Smax; i++)
		{
			S = (int) (audiance[i] - '0');
			if (standing < i)
			{
				friends += (i - standing);
				standing += (i - standing);
			}
			standing += S;
		}
		printf("Case #%d: %d\n", Ti, friends);
  }
  return 0;
}
