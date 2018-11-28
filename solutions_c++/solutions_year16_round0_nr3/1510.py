#include <iostream>
#include <string>

using namespace std;

const int N = 16;
const int J = 50;

#define ULL unsigned long long

ULL convert(string s, ULL base) {
	ULL mul = 1;
	ULL res = 0;
	for (int i = s.length() - 1; i >= 0; i--) {
		res += (s[i]-'0')*mul;
		mul *= base;
	}
	return res;
}

string generate(ULL x) {
	string s = "";
	while (x != 0) {
		s += (x%2)+'0';
		x /= 2;
	}
	
	s = string(s.rbegin(), s.rend());
	
	while (s.length() < N-2)
		s = "0"+s;
	
	return "1"+s+"1";
}

ULL findDivisor(ULL a) {
	for (ULL i = 2; i*i <= a; i++)
		if (a % i == 0 && i != a)
			return i;
			
	return 0;
}

int main() {
	ios_base::sync_with_stdio(0);
	
	int numOfRes = 0;
	
	cout << "Case #1:\n";
	ULL x = 1;
	while (numOfRes != J) {
		string s = generate(x);
		ULL div[9];
		bool ok = true;
		for (int i = 2; i <= 10; i++) {
			ULL tmp = findDivisor(convert(s, i));
			if (tmp != 0)
				div[i - 2] = tmp;
			else {
				ok = false;
				break;
			}
		}
		
		if (ok) {
			cout << s << " ";
			for (int i = 2; i <= 10; i++)
				cout << div[i-2] << " ";
			cout << "\n";
			numOfRes++;
		}
		x++;
	}
	
	return 0;
}
