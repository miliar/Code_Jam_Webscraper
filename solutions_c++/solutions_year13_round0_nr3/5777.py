#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

int digits(long long n) {
	int conta = 1;
	while (n>=10) {
		conta++;
		n/=10;
	}
	return conta;
}

vector<int> gira(long long n) {
	vector<int> v(0);
	if (n == 0) v.push_back(0);	
	while (n>0) {
		v.push_back(n%10);
		n/=10;
	}
	return v;
}

bool palindrom(long long n) {
	vector<int> girat = gira(n);
	for (int i=girat.size()-1; i>=0; i--) {
		if (girat[i] != n%10) return false;
		n/=10;
	}
	return true;	
}

bool sqfair(long long i) {
	double d = sqrt(i);
	long long n = sqrt(i);
	if (d!=n) return false;
	if (palindrom(n) and palindrom(i)) return true;
	return false;
}

int main() {
	int t;
	cin >> t;
	for (int cas = 1; cas<=t; cas++) {
		cout << "Case #" << cas << ": ";
		long long a,b,total;
		total = 0;
		cin >> a >> b;
		for (long long i=a; i<=b; i++) {
			if (sqfair(i)) total++;
		}
		cout << total << endl;
	}
}
