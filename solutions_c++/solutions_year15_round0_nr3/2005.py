#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <algorithm>
#include <queue>
#include <numeric>
#include <array>
#include <map>
#include <unordered_map>
#include <functional>
#include <iostream>
#include <thread>
#include <sstream>
#include <atomic>

using namespace std;


int tab[4][4] = {
	{0, 1, 2, 3},
	{1, 4, 3, 6},
	{2, 7, 4, 1},
	{3, 2, 5, 4}
};

int mult(int x, int y) {
	return (x&4) ^ (y&4) ^ tab[x&3][y&3];
}

int main () {
	int T;
	scanf("%d", &T);
	for (int t=1; t<=T; t++) {
		int L, X;
		scanf("%d%d", &L, &X);
		int X4=X%4;
		char S[41000];
		scanf("%s", S);
		memcpy(S+L, S, L);
		memcpy(S+L+L, S, L+L);
		int x=0;
		int i=0;
		while (x!=1 && i<4*L) {
			x=mult(x, S[i]-'i'+1);
			i++;
		}
		x=0;
		int j=0;
		while (x!=3 && j<4*L) {
			x=mult(S[4*L-j-1]-'i'+1, x);
			j++;
		}
		x=0;
		for (int k=0; k<X4*L; k++) x=mult(x, S[k]-'i'+1);
		bool OK=(x==4);
		OK = OK && (i<4*L);
		OK = OK && (j<4*L);
		OK = OK && (i+j < 1LL*L*X);

		printf("Case #%d: %s\n", t, OK?"YES":"NO");
	}
	return 0;
}
