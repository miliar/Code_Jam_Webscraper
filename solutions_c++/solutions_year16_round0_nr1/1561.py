#include <iostream>
#include <string.h>

using namespace std;

bool dig[10];
#define LIM 1000

bool digupd(int i) {
	int d;
	string s;
	do {
		d=i%10;	
		dig[d]=true;
	} while ((i/=10)!=0);
/*
		for ( bool b : dig) cout << b << " ";
		cout << endl;
		getline(cin,s);
*/
	for (bool b : dig) {
		if (!b) return false;
	}
	return true;
}

int main(void) {
	int t;
	cin >> t;
//	t=500;
	int n;
	for ( int i=0; i<t; i++) {
		fill(begin(dig), end(dig), false);
		cin >> n;
		int N=n;
		int l=1;
		if (n==0) { 
			cout << "Case #" << i+1 << ": INSOMNIA" << endl;
			continue;
		}
		while (!digupd(N) && l<=LIM) {
			l++;
			N+=n;
		}
		cout << "Case #" << i+1;
		//cout << "Case #" << i+1 << "(" << l << ")";
		if ((LIM+1)==l) cout << ": INSOMNIA" << endl;
		else cout << ": " << l*n << endl;	
	}	
	return 0;
}
