#include <iostream>
#include <string>
#include <map>
#include <deque>
#include <queue>
#include <stack>
#include <sstream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <algorithm>
#include <vector>
#include <set>
#include <complex>
#include <list>

using namespace std;

bool ispos(long long P, long long Q);
int solve(long long P, long long Q);

int main() {
	int T, y;
	long long P, Q;
	char sl;
	bool could;
	cin >> T;
	for (int x = 1; x <= T; x++) {
		cin >> P >> sl >> Q;
		could = ispos(P, Q);
		y = solve(P, Q);	
		cout << "Case #" << x << ": ";
		if (could) 	cout << y;
		else 		cout << "impossible";
		cout << endl;
	}
}

bool ispos(long long P, long long Q) {
	long long num = 1;
	for (int i = 0; i < 40; i++, num*=2);
	num *= P;
	bool ok = (num % Q == 0);
	return ok; 
}

int solve(long long P, long long Q) {
	long long nP = P;
	int mingen = 0;
	while (nP < Q) {
		mingen++;
		nP *= 2;
	}
	return mingen;
}
