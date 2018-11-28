#include <iostream>
#include <vector>
#include <string>
#include <set>

using namespace std;

set<long long> s;

void f(long long x){
	while(x > 0){
		long long st = x % 10;
		s.insert(st);
		x /= 10;
	}
}

int main(){
	long long t;
	cin >> t;

	for(long long cnt = 1; cnt <= t; cnt++){
		s.clear();
		cout << "Case #" << cnt << ": ";
		long long n;
		cin >> n;
		if(n == 0) {cout << "INSOMNIA\n"; continue;}

		long long tren = n;

		f(tren);
		while(s.size() < 10){
			tren += n;
			f(tren);
		}

		cout << tren << "\n";
	}
}