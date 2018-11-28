#include <algorithm>
#include <cstdio>
#include <iomanip>
#include <iostream>
#include <string>
#include <queue>
using namespace std;
#define DEBUG

const int MAXN = 1000 + 5;
double naomi[MAXN], ken[MAXN];
int mKen[MAXN];
inline void clear(int n){ for (int i = 0; i < n; ++i) mKen[i] = 0; }
int getRawWar(int n){
	clear(n);
	int res = 0;
	for (int i = 0; i < n; ++i){
		int isFound = 0;
		for (int j = 0; j < n; ++j)
			if (!mKen[j] && ken[j] > naomi[i]) { mKen[j] = 1; isFound = 1; break; }
		if (!isFound) for (int j = 0; j < n; ++j) 
			if (!mKen[j]){ mKen[j] = 1; ++res; break; }
	}
	return res;
}
int getDeceifulWar(int n){
	clear(n);
	int res = 0, ks = 0, ke = 0;
	for (int i = 0; i < n; ++i){
		if (naomi[i] < ken[ks]) --ke;
		else { ++ks; ++res; }
	}
	return res;
}
int main(){
#ifdef DEBUG
	freopen("D-large.in", "r", stdin);
	freopen("data.out", "w", stdout);
#endif
	int t = 0, T, dw, rw, n;
	cin >> T;
	while (++t <= T){
		cin >> n;
		for (int i = 0; i < n; ++i) cin >> naomi[i];
		for (int i = 0; i < n; ++i) cin >> ken[i];
		dw = rw = 0;
		sort(naomi, naomi + n);
		sort(ken, ken + n);
		dw = getDeceifulWar(n);
		rw = getRawWar(n);
		cout << "Case #" << t << ": " << dw << " " << rw << endl;
	}
	
	return 0;
}
