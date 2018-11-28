#include <iostream>
#include <stdio.h>
#include <vector>
#include <algorithm>
#include <math.h>

using namespace std;

vector <int> num;

int extract_digits(long long int n)
{
	long long int i, j, k, x;
	while (n) {
		x = n % 10;
		if (find(num.begin(), num.end(), x) == num.end()) {
			num.push_back(n % 10);
			//cout << "D: "<< x << endl;
		}
		if (num.size() == 10)
			return 0;
		n /= 10;
	}
	return 1;
}

int extract_numbers(long long int n)
{
	if (n == 0)
		return -1;
	long long int i = 0;
	for (i = 1; ;i++) {
		if (!extract_digits(i * n)) {
			//cout << "I: " << i << endl;
			return (i * n);
		}
	}
}

int main()
{
	freopen("c_s1.in", "rt", stdin);
	freopen("c_s1.out", "wt", stdout);
	long long int t, n, x;
	int i, j, k;
	cin >> t;
	for (i = 1; i <= t; i++) {
		cin >> n;
		x = extract_numbers(n);
		if (x == -1) {
			cout << "Case #" << i <<": INSOMNIA" << endl;
		} else {
			cout << "Case #" << i <<": " << x << endl;
		}
		num.clear();
			
	}
	return 0;
}
