#include <iostream>
#include <cstring>

using namespace std;

bool isPal (int n ) {
	int a[5], i = 0;
	
	while ( n > 0 ) {
		a[i] = n%10;
		n /= 10;
		i++;
	}
	
	if ( i == 1 ) return true;
	
	int j = 0;
	while ( j <= i ) {
		if ( a[j] != a[i-1] ) return false;
		j++; i--;
	}
	return true;
}

int main() {
	int a[1001], T, l, r;
	memset(a,0,sizeof(a));
	
	for (int i = 1; i*i <= 1000; i++)
		if ( isPal(i) && isPal(i*i) )
			a[i*i] = 1;
	
	cin >> T;
	
	for (int t = 1; t <= T; t++) {
		int cont = 0;
		cin >> l >> r;
		
		for (int i = l; i <= r; i++)
			if ( a[i] == 1 )
				cont++;
		cout << "Case #" << t << ": " << cont << endl;
	}
	return 0;
}
