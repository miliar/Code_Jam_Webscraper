#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

bool pallin (double x)
{
	if ( (int)x != x )
		return false;
	
	int n = (int)x;
	int N = n;
	
	int p = 1;
	int d = 0;
	while ( N ) {
		N = N/10;
		d++;
		p = p * 10;
	}
	p = p/10;
	
	N = n;

	bool f = true;

	while(N) {
		int r = N % 10;
		int q = N / p;
		if ( r != q ) {
			f = false;
			break;
		}
		N = N % p;
		N = N / 10;
		p = p / 100;
	}
		
	return f;
}

int main()
{
	int t,a,b;
	cin >> t;

	for ( int i = 0; i < t; i++ ) {
		int cnt = 0;
		cin >> a >> b;
		for ( int j = a; j <= b; j++ ) {
			if ( pallin(sqrt(j)) && pallin(j) )
				cnt++;
		}
		cout << "Case #" << i + 1 << ": " << cnt << "\n";
	}

	return 0;
}
