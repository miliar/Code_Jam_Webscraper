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
string G = "GABRIEL";
string Ri = "RICHARD";
string solve(int X, int R, int C)
{
	if (X == 1) return G;
	if ((R == 1) || (C == 1))
		if (X > 2) return Ri;
	if (((R*C) % X) != 0)
		return Ri;
	if ((X > C) && (X > R))
		return Ri;
	if (X == 4)
	{
		if ((C == 2) || (R == 2)) return Ri;
	}
	return G;
}
int main() {
	int T,X,R,C; scanf_s("%d", &T);
	for (int Ti = 1; Ti <= T; ++Ti) {
		fprintf(stderr, "Case #%d of %d...\n", Ti, T);
		scanf_s("%d %d %d", &X, &R, &C);
		string result = solve(X, R, C);
		printf("Case #%d: ", Ti);
		cout << result << endl;
  }
  return 0;
}
