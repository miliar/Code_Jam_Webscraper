#include <iostream>
#include <algorithm>
#include <cmath>
using namespace std;
long long set(long long n, long long k){
	if(!((n >> k) & 1))
		n+=pow(2,k);
	return n;	
}
long long check(long long n, long long ch) {
	while(n) {
		ch = set(ch,n%10);
		n = n/10;
	}
	return ch;
}
int main() {
	long long int t, n, ch, i,j;
	cin >> t;
	for(j = 1; j <= t; j++) {
		ch = 0;
		cin >> n;
		i = 1;
		if(n == 0) {
			cout << "Case #"<<j<<": "<<"INSOMNIA\n";
		}
		else {
			while (ch != (pow(2,10) - 1)) {
			ch = check(i*n,ch);
				i++;
			}
			cout <<"Case #"<<j<<": "<< ((i-1)*n) << "\n";
		}
				
	}
	
	return 0;
}
