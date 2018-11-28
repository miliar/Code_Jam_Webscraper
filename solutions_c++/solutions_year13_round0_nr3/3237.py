#include <iostream>
#include <cmath>

using namespace std;


bool nice(long long n) {

	char d[100];
	
	int i=0;
	while (n) {
		d[i] = n%10;
		n/=10;
		i++;
	}
	for (int p = 0; p<i/2;p++ ) {
		if (d[p]!=d[i-p-1]) return false;
	}

	return true;
}

int main() {

	int T;
	cin >> T;
	
	for (int t=0; t<T; t++) {
	
		long long A,B;
		cin >> A >> B;
		
		long ans = 0;
		long b = sqrt(B) + 1;
		long a = sqrt(A);
		if (a==0) a++;
		for (long long n = a; n <= b; n++) {
			if (n*n < A) continue;
			if (n*n > B) break;
			if (nice(n) && nice(n*n)) ans++;
		}
	
		cout << "Case #" << (t+1) << ": " << ans << endl;
	
	}

	return 0;
}


