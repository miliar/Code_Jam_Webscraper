#include<iostream>
using namespace std;

int add(int n, int mask) {
	while(n) {
		mask |= (1<<(n%10));
		n/=10;
	}
	return mask;
}

int main() {
	int t;
	cin >> t;
	for(int c=1;c<=t;c++) {
		int n, x;
		cin >> n;
		if (n==0) {
		  cout << "Case #" << c << ": INSOMNIA" << endl;
			continue;
		}
		x = n;
		int m=0;
		while(1) {
			m = add(x,m);
			if (m == (1<<10) -1) {
				break;
			}
			x += n;
		}
		cout << "Case #" << c << ": " << x << endl;
	}
	return 0;
}
