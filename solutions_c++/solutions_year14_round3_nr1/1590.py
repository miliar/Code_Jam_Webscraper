#include <sstream>
#include <iostream>
using namespace std;
long long gcdOfTwoNumbers(long long a, long long b);
long long getNoOfLevels(long long a, long long b) {
	long long halfq = b / 2;
	if (a - halfq >= 0) {
		return 1;
	} else {
		return 1 + getNoOfLevels(a, halfq);
	}
}
bool p2(long long b) {
	if (b == 1 || b == 0)
		return true;
	else if (b % 2 == 0)
		return p2(b / 2);
	return false;
}
long long getAns(long long a, long long b) {
	long long g = gcdOfTwoNumbers(a, b);
	a = (long long) (a / g);
	b = (long long) (b / g);
	if (p2(b) == false) {
		return -1;
	} else {
		return getNoOfLevels(a, b);
	}
}
void printAnswer(long long a, long long b) {
	long long res = -2;
	if (a > b)
		res = -1;
	else{
		res = getAns(a, b);
	}
	if (res == -1)
		cout << "impossible" << endl;
	else
		cout << res << endl;
}

int main() {
	long long a, b;
	int nT,t=1;
	cin >> nT;
	while(t <= nT) {
		string ip;
		cin >> ip;
		size_t found = ip.find("/");
		string first = ip.substr(0, found);
		string second = ip.substr(found + 1);
		istringstream fir(first);
		fir >> a;
		istringstream sec(second);
		sec >> b;
		cout << "Case #" << t << ": ";
		printAnswer(a, b);
		t++;
	}
	return 0;
}
long long gcdOfTwoNumbers(long long a, long long b) {
	if (b == 0)
		return a;
	return gcdOfTwoNumbers(b, a % b);
}

