#include <iostream>
#include <vector>
#include <string>
#include <set>
#include <cmath>

using namespace std;

long long k, c, s;

long long fun(long long x){
	long long tren = 0;

	for(int i = 0; i < c; i++){
		tren += pow(k, i) * (x - 1);
	}

	return tren + 1;
} 

int main(){
	long long t;
	cin >> t;

	for(long long cnt = 1; cnt <= t; cnt++){
		cout << "Case #" << cnt << ": ";
		cin >> k >> c >> s;
		for(int i = 1; i <= s; i++) cout << i << " ";
		cout << "\n";

		/*cout << "1";
		for(int i = 2; i <= k; i++){
			cout << " " << fun(i);
		}
		cout << "\n"; */
	}
	return 0;
}