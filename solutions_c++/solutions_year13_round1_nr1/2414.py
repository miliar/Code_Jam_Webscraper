#include <iostream>
#include <cstdio>
#include <cstdlib>

using namespace std;
#define ull unsigned long long

ull r, t;
const ull maxn = 2E9;
ull cal(ull m) {
	//ull ret = m*m*2+r*m*2-m;
	ull ret = r*2+m*2-1;
	return ret;
}

//ull check(ull m) {
//	ull ret = m*m*2+r*m*2-m;
//	//ull ret = r*2+m*2-1;
//	return ret;
//}

ull bsearch(ull x, ull y, ull v) {

	ull m;
	while(x<y)
	{
		if(x==y-1) return x;
		m=x+(y-x)/2;
		ull cv = v/cal(m);
		if(m== cv) return m;
		else if(m>cv) y = m;
		else x = m+1;
	}
}

int main() {

	freopen("A-small-attempt1.in", "r", stdin);
	freopen("a.out", "w", stdout);

	int T;
	cin >> T;
	// build the table

	for(int kase = 1; kase <=T; kase++) {
		cin >> r >> t;
		ull ret = 1;
		//ull ret = bsearch(1LL,maxn,t);
		while(ret <= t/cal(ret)) ret++;
		while(ret > t/cal(ret)) ret--;

		cout << "Case #" << kase << ": " << ret << endl;

	}

	return 0;
}