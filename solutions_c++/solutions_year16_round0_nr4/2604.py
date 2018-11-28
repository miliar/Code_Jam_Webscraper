#include <iostream>
#include <math.h>
using namespace std;

typedef long long ll;

int main(){
	int t;
	cin >> t;
	ll k, c, s;
	for(int i = 1; i <= t; i ++){
		cin >> k >> c >> s;
		cout << "Case #" << i << ": ";
		ll gap = pow(k, c - 1);
		for(int j = 1; j <= k; j ++){
			ll r = (j - 1)  * gap + 1LL;
			cout << r << " ";
		}
		cout << endl;
	}
	return 0;
}

