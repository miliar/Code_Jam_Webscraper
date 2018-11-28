#include <set>
#include <map>
#include <queue>
#include <stack>
#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <limits.h>
#include <string.h>
#include <string>
#include <algorithm>
#define MID(x,y) ( ( x + y ) >> 1 )
#define L(x) ( x << 1 )
#define R(x) ( x << 1 | 1 )
#define FOR(i,s,t) for(int i=(s); i<(t); i++)
#define FORD(i,s,t) for(int i=(s-1); i>=t; i--)
#define BUG puts("here!!!")
#define STOP system("pause")
#define file_r(x) freopen(x, "r", stdin)
#define file_w(x) freopen(x, "w", stdout)

using namespace std;

const int MAX = 1010;
double naomi[MAX], ken[MAX];
bool f[MAX];
bool find(double x, int n) {
	for(int k=0; k<n; k++) {
		if( !f[k] && ken[k] > x ) {
			f[k] = true;
			return true;
		}
	}
	for(int k=0; k<n; k++)
		if( !f[k] ) {
			f[k] = true;
			return false;
	}
}
int war(int n) {
	memset(f, 0, sizeof(f));
	int score = 0;
	for(int i=0; i<n; i++) {
		if( !find(naomi[i], n) )
			score++;
	}
	return score;
}

int deceitful_war(int n) {
	double tmp[MAX];
	memcpy(tmp, naomi, sizeof(naomi));
	memcpy(naomi, ken, sizeof(ken));
	memcpy(ken, tmp, sizeof(tmp));
	return n - war(n);
}

int main() {
	int ncases;
	int n;
	
	file_r("D-large.in");
	file_w("out.txt");
	cin >> ncases;
	for(int ncase=1; ncase<=ncases; ncase++) {
		cin >> n;
		for(int i=0; i<n; i++)
			cin >> naomi[i];
		for(int i=0; i<n; i++)
			cin >> ken[i];
		
		sort(naomi, naomi+n);
		sort(ken, ken+n);
		int w = war(n);
		int dw = deceitful_war(n);
		cout << "Case #" << ncase << ": " << dw << ' ' << w << endl;
		
	}
	return 0;
}

