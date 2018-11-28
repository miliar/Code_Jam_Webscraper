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

#define PROB_ID "C"
#define INPUT_SIZE  "small" //"large" // 

typedef long double LD;

char c[10016];

char multiplyChar(char a, char b, bool& bNegative) {
	if (a == '1') return b;
	if (b == '1') return a;
	if (a == b) { bNegative = !bNegative; return '1'; }
	if ((a == 'i') && (b == 'j')) { return 'k'; }
	if ((a == 'i') && (b == 'k')) { bNegative = !bNegative; return 'j'; }
	if ((a == 'j') && (b == 'k')) { return 'i'; }
	if ((a == 'j') && (b == 'i')) { bNegative = !bNegative; return 'k'; }
	if ((a == 'k') && (b == 'i')) { return 'j'; }
	if ((a == 'k') && (b == 'j')) { bNegative = !bNegative; return 'i'; }
	return '1';
}

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
		int L;
		ll X;
		scanf("%d %lld\n", &L, &X); // remember to put \n
		scanf("%s\n", c); // remember to put \n
		bool bSuccess = false;
		do {
			if (L == 1) break;
			if ((L < 3) && (X == 1)) break;
			// Check for repeated characters
			bool bRepeated = true;
			char currentC = c[0];
			for (int j = 1; j < L; ++j) {
				if (c[j] != currentC) { bRepeated = false; break; }
			}
			if (bRepeated) break;

			// Process to find ijk

			bool bMinus = false; // to see if minus place holder is present
			int findijk = 0; // 0 - find i, 1 - find j, 2 - find k, 3 all found, 5 find end, 10 found number of iteration for 1 result
			char cResult = '1';
			ll FirstEnd = -1;
			ll LastEnd = -1;
			for (ll k = 1; k <= X; ++k) {
				for (int l = 0; l < L; ++l) {
					cResult = multiplyChar(cResult, c[l], bMinus);
					if ((findijk == 0) && (cResult == 'i') && (!bMinus)) { ++findijk; cResult = '1'; }
					else if ((findijk == 1) && (cResult == 'j') && (!bMinus)) { ++findijk; cResult = '1'; }
					else if ((findijk == 2) && (cResult == 'k') && (!bMinus)) { findijk = 5; cResult = '1'; }
				}
				if ((findijk == 5) && (cResult == '1') && (!bMinus)) { FirstEnd = k; findijk = 10; }
				else if ((FirstEnd != -1) && (cResult == '1') && (!bMinus)) { LastEnd = k; break; }
			}
			if (LastEnd != -1) { if ((X - FirstEnd) % (LastEnd - FirstEnd) == 0) bSuccess = true; }
			else if (FirstEnd == X) bSuccess = true;
			//else if (findijk > 2) bSuccess = true;
		} while (false);
		if (bSuccess) printf("Case #%d: YES\n", i + 1);
		else printf("Case #%d: NO\n", i + 1);
	}
	return 0;
}

