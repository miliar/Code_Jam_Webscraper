#include <iostream>
#include <cmath>
using namespace std;

bool isPalindrom (long long num) {
	 long long n = num;
	 long long rev = 0;
	 while (num > 0)
	 {
	      int dig = num % 10;
	      rev = rev * 10 + dig;
	      num = num / 10;
	 }
	 return (n == rev);
}

int checkNum (long long a) {

	long long sq = sqrt (a);
	long long check;
	check = sq*sq;
	if (a != check) return 0;
	if (not isPalindrom(sq)) return 0;
	//cout << "is square" << endl;
	if (not isPalindrom(a)) return 0;

	return 1;
}

int main () {

	int total;
	int ccase = 0;
	cin >> total;
	while (ccase < total) {
		long long a, b;
		cin >> a;
		cin >> b;
		long long count = 0;
		while (a <= b) {
			count += checkNum(a);
			++a;
		}
		++ccase;
		cout << "Case #"<<ccase<<": "<<count<<endl;
	}

}