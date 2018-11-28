#include <iostream>
//#include <string>
using namespace std;

long rev(long z) {
	long x = 0;
	while (z) {
		x = x*10 + z%10;
		z /= 10;
	}
	return x;
}
long div10(long n, long c) { long x=1;while (c--)x*=10;return n%x;}
void cas() {
	string N; cin >> N;
	long y = 0, n = stol(N), c;
	string a, b;
	while (n) {//cout<<n<<',';
		//if (n % 10 == 1) { 
		a = to_string(n);
		c = a.length()/2;
		//b = to_string(rev(n));
		//;
		//long l = 0;bool f=true;
		//for (string::iterator it=a.end()-1; it!=a.end()-/2-1; --it) if (*it != '0') f = false;
		//if (b.size() > 2) l = stol(a.substr(1,-1));
		if (div10(n,c) == 1 && n > rev(n)) n = rev(n); //else --n; }
		else --n;
		++y;
		//cout<<y<<' ';
	}
	cout << y << endl;
}

int main() {
	int t; cin >> t;
	int i = 1;
	while (t--) {
		cout << "Case #" << i++ << ": ";
		cas();
	}
}
