#include <iostream>
#include <vector>
#include <string>

using namespace std;

bool simple(unsigned long long x) {
	for (unsigned long long i = 2; i <= sqrt(x) + 1; i++)
		if (x%i == 0) return false;
	return true;
}

unsigned long long toBin(unsigned long long x) {
	unsigned long long ans = 0;
	vector<unsigned long long> bac;

	while (x != 0) {
		bac.push_back(x % 2);
		x /= 2;
	}
	unsigned long long p = 1;
	for (unsigned long long i = 0; i < bac.size(); i++) {
		ans += bac[i] * p;
		p *= 10;
	}
		
	return ans;
}

unsigned long long from(unsigned long long x, int base) {
	unsigned long long ans = 0;
	vector<unsigned long long> bac;

	while (x != 0) {
		bac.push_back(x % 10);
		x /= 10;
	}
	unsigned long long p = 1;
	for (unsigned long long i = 0; i < bac.size(); i++) {
		ans += bac[i] * p;
		p *= base;
	}

	return ans;
}

void del(unsigned long long x) {
	for (unsigned long long i = 2; i <= 10; i++) {
		//if (i % 2) cout << "2 ";
		//else {
			unsigned long long number = from(x, i);
			for (unsigned long long j = 2; j<=sqrt(number)+1; j++)
				if (number%j == 0)
				{
					cout << j << " ";
					break;
				}
		//}
	}
}

void main() {

	FILE *str, *abc;
	freopen_s(&str, "input.txt", "r", stdin);
	freopen_s(&abc, "out.txt", "w", stdout);

	unsigned long long t;
	cin >> t;

	for (unsigned long long i = 0; i < t; i++) {

		unsigned long long n, j;
		vector <unsigned long long> ans;
		cin >> n >> j;

		unsigned long long num = 0;
		unsigned long long x = (1 << (n-1)) + 1;

		while (num != j) {
			bool sim = false;
			for (int k = 2; k <= 10; k++) {
				unsigned long long number = toBin(x);
				number = from(number, k);
				if (simple(number)) {
					sim = true;
					break;
				}
			}			
			if (!sim) {
				num++;
				ans.push_back(x);
			}
			x += 2;
		}

		cout << "Case #" << i + 1 << ": " << endl;
		
		for (int k = 0; k < j; k++) {

			cout << toBin(ans[k]) << " ";
			del(toBin(ans[k]));
			cout << endl;
		}
			
	}
	

}