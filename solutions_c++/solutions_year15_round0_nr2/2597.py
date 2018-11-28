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

#define PROB_ID "B"
#define INPUT_SIZE  "small" // "large" //

typedef long double LD;

int P[1024];
int main()
{
	//freopen("my_input.txt", "r", stdin);
	//freopen("my_output.txt", "w", stdout);

	freopen(PROB_ID "-" INPUT_SIZE "-attempt2.in", "r", stdin);
	freopen(PROB_ID "-" INPUT_SIZE "-attempt2.out", "w", stdout);

	int T;
	scanf("%d\n", &T); // remember to put \n

	rep(i, T) {
		// inputs
		int D;
		scanf("%d\n", &D); // remember to put \n

		int maxP = 0;
		rep(j, D) { scanf("%d", &(P[j]));  if (maxP < P[j]) maxP = P[j]; }

		// processing
		int minMinutes = maxP;
		fo(k, 1, maxP) {
			int TotalMins = k;
			rep(j, D) {
				if (P[j] > k) {
					if (P[j] % k == 0) TotalMins += ((P[j] / k) - 1);
					else TotalMins += (P[j] / k);
				}
			}
			if (minMinutes > TotalMins) minMinutes = TotalMins;
		}
		// Output
		printf("Case #%d: %d\n", i + 1, minMinutes);
	}
	return 0;
}

