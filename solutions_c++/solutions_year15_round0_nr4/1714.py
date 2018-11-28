#define _CRT_SECURE_NO_DEPRECATE

#include <algorithm>
#include <cmath>
#include <complex>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <map>
#include <numeric>
#include <set>
#include <sstream>
#include <string>
#include <vector>
#include <queue> 
#include <cctype> 
#include <cassert>

using namespace std;

#define VV vector
#define PB push_back
#define SZ(v) ((int)(v).size()) 
#define ll long long
#define ld long double
#define rep(i,b) for(int i=(0);i<(b);++i)
#define fo(i,a,b) for(int i=(a);i<=(b);++i)
#define ford(i,a,b) for(int i=(a);i>=(b);--i)
#define fore(a,b) for(decltype((b).begin()) a = (b).begin();a!=(b).end();++a)
#define all(x) (x).begin(),(x).end()
#define clr(x,a) memset(x,a,sizeof(x))
#define vi VV<int>
#define vs VV<string>
#define MAX(a,b) ((a)>(b))?((a):(b))
#define MIN(a,b) ((a)<(b))?((a):(b))

#define PROB_ID "D"
#define INPUT_SIZE  "small" // "large" //

typedef long double LD;



int main()
{
	//freopen("my_input.txt", "r", stdin);
	//freopen("my_output.txt", "w", stdout);

	freopen(PROB_ID "-" INPUT_SIZE "-attempt0.in", "r", stdin);
	freopen(PROB_ID "-" INPUT_SIZE "-attempt0.out", "w", stdout);

	int T;
	scanf("%d\n", &T); // remember to put \n

	rep(i, T) {
		// inputs
		int X, R, C;
		scanf("%d %d %d\n", &X, &R, &C); // remember to put \n

		bool Gab = false;
		do {
			// Definite
			if ((R * C) % X != 0) break;
			if (X > 6) break; // because there will be hole in the middle
			if ((R < X) && (C < X)) break;
			if ((R >= X) && (C >= X)) { Gab = true; break; }

			// Other
			if (X < 3) { Gab = true; break; }
			if (X == 3) {
				if ((R == 1) || (C == 1)) break;
				else { Gab = true; break; }
			}
			if (X == 4) {
				if ((R < 3) || (C < 3)) break;
				else { Gab = true; break; }
			}

			Gab = true;
		} while (false);

		if (Gab) printf("Case #%d: GABRIEL\n", i + 1);
		else printf("Case #%d: RICHARD\n", i + 1);
	}
	return 0;
}

