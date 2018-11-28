#include <iostream>
#include <string>
#include <stdlib.h>
#include <math.h>
using namespace std;
typedef long long int int64;

// >:(

void init() {
	// create prime array
}

void process(int n,int j) {
	int64 v, vf;
	int64 f[11], d[11];	//d: debug
	int r = 0;
	// init
	v = pow(2,n-1)+1;
	vf = pow(2,n);
	while (r < j && v < vf) {
		bool c = true;
		// find any existing factor
		for (int i=2; i<=10 && c; i++) {
			int64 vn=0;
			int64 k=1;
			for (int64 l=v; l; l/=2) {
				vn += (l%2) * k;
				k *= i;
			}
			c = false;
			for (int64 j=2; j<sqrt(vn)+1; j++) {
				if (vn%j==0) {
					f[i]=j;
					d[i]=vn;
					c = true;
					break;
				}
			}
		}
		// factor found?
		if (c) {
			string s;
			for (int64 l=v;l; l/=2)
				s.insert(0, 1, l%2+'0');
			cout << s << " ";
			for (int i=2; i<=10; i++)
				cout << " " << f[i];	
			cout << endl;
			r++;
		}
		// next iter
		v+=2;
	}
}

int main() {
	init();
	int m;
	cin >> m;
	for (int i=0; i<m; i++) {
		int n,j;
		cin >> n >> j;
		cout << "Case #" << i+1 << ":" << endl;
		process(n, j);
	}
	return 0;
}
