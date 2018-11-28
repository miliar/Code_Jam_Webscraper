#include <iostream>
#include <math.h>

using namespace std;

typedef unsigned long long ull;

int digs;

ull div(ull j) {
	for (ull i = 2; i<=sqrt(j); i++) {
		if (!(j%i)) return i;
	} return 0;
}

ull tobase(ull n, ull b) {
	ull res = 0;
	for (ull i=0; n; i++) {
		if (n & 1) res += pow (b,i);
		n >>= 1;
	} return res;
}

bool sirve(ull n){
	ull divs[10];	

	for (int i=2; i<=10; i++) {
		ull j = tobase(n, i);
		ull d = div(j);
		if (!d) return false;
		divs[i] = d;
		
	}
	for (int i=digs-1; i>=0;i--) cout << (bool)(n & (1 << i));
	cout << ' ';
	for (int i=2; i<=9;i++) cout << divs[i] << ' ';
	cout << divs[10];
	cout << endl;
	return true;
}

int main(){
    int j;
    cin >> j;
    cin >> digs >> j;
	int f = 0;
	cout << "Case #1:\n";
    for (ull i = (1<<digs-1) + 1; f<j; i+=2) {
		if (sirve(i)) f++;
	}
}
