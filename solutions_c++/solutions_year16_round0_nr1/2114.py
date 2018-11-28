#include <iostream>
using namespace std;

const int N = 1e5, target = 1023;

short mask[N];

inline int digits(int n){
	return mask[n / N] | mask[n % N];
}

inline int count(int n){
	if ( n == 0 ) return -1;

	int mask = 0, ans = 0;
	for (int i = n; mask != target; i += n, ans++)
		mask |= digits(i);
	return ans;
}

inline int compute(int n){
	int mask = 0, inc = n;
	while (mask != target){
		mask |= digits(n);
		n += inc;
	}
	return n - inc;
}

int main(){
	mask[0] = 0;
	for (int i = 1; i < N; i++)
		mask[i] = mask[ i / 10 ] | (1 << i%10);

	int times, n;
	cin >> times;
	for (int i = 1; i <= times; i++){
		cin >> n;
		cout << "Case #" << i << ": ";
		if ( n == 0 )
			cout << "INSOMNIA" << '\n';
		else
			cout << compute(n) << '\n';
	}
/*
	int best = 0;
	for (int i = 1; i < 1e6; i++){
		int val = count(i);
		if ( best < val ){
			best = val;
			cout << i << ' '  << best << '\n';
		}
	}
*/
	return 0;
}
