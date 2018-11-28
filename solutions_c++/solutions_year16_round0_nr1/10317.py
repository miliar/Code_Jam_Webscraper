#include <iostream>
#include <cstdlib>
#include <cstdio>

using namespace std;

int b[20];

int getNumber() {
	int s = 0;
	for (int i=0; i<10; ++i)
		s += b[i];
	return s;
}

void calc(int number) {
	int n = number;
	while (n > 9) {
		b[n % 10] = 1;
		n /= 10;
	}
	b[n] = 1;
}

int getSleepTime(int number) {
	if (number == 0) return -1;
	for (int i=0; i<100; ++i) b[i] = 0;
	int c = 1, n = number;
	for (;;) {
		if (c > 10000) break;
		calc(n*c);
//		cout<<c<<" "<<c*n<<"\n";
//		for (int i=0; i<10; ++i) cout<<b[i]<<" ";
//		cout<<"\n\n";
		if (getNumber() == 10)
			return c*n;
		c++;
	}
	return -1;
}

int main() {
	int t;
	cin>>t;
	int a[200];
	for (int i=0; i<t; ++i) cin>>a[i];
	
	for (int i=0; i<t; ++i) {
		int re = getSleepTime(a[i]);
		if (re == -1)
			cout<<"Case #"<<(i+1)<<": INSOMNIA\n";
		else
			cout<<"Case #"<<(i+1)<<": "<<re<<"\n";
//		break;
	}
	
}