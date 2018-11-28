#include <iostream>
#include <fstream>
#include <string>
#include <map>
#include <set>

using namespace std;

long long f(long long a) {
	long long c = 0, i = 0, b;
	bool used[10];
	for (int i = 0; i < 10; i++)
		used[i] = false;
	while (c != 10) {
		i++;
		b = a * i;
		while (b != 0) {
			if (!used[b % 10]) {
				c++;
				used[b % 10] = true;
			}
			b /= 10;
		}
	}
	return a * i;
}

long long t, n;

int main() {
	ifstream cin("in.txt");
	ofstream cout("out.txt");
	cin >> t;
	for (int i = 1; i <= t; i++) {
		cin >> n;
		if (n != 0)
			cout << "Case #" << i << ": " << f(n) << endl;
		else
			cout << "Case #" << i << ": " << "INSOMNIA" << endl;
	}	
	return 0;
}