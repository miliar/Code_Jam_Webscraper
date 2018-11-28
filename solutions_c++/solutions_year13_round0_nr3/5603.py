#include <iostream>
#include <cmath>
using namespace std;
typedef long long int64;
bool good(int64 x) {
	int64 t = x;
	int64 y = 0;
	while(t) {
		y = y * 10 + t % 10;
		t /= 10;
	}
	return y == x;
}
int main() {
	int T, casn = 1;
	cin >> T;
	while(T--) {
		long long ans=0;
		int64 A, B;
		cin >> A >> B;
		for(int64 i=int(sqrt(A)); i*i<=B; ++i) {
			if(i*i<A) continue;
			if(good(i) && good(i*i))
				ans++;
		}	
		cout << "Case #" << casn++ << ": ";
		cout << ans;
		cout << endl;
	}
	
	return 0;
}
