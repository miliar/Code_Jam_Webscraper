#include <cstdio>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

vector <long long> a;

bool isPal(long long n) {
	string s;
	while(n != 0) {
		s.push_back(n % 10LL + '0');
		n = n / 10LL;
	}
	for(int i = 0; i < s.length(); i ++)
		if(s[i] != s[s.length() - 1 - i])
			return false;
	return true;
}

void init(long long curr) {
	if(curr <= 10000000LL) {
		long long temp;
		temp = curr * 10LL;
		if(isPal(temp)) {
			if(isPal(temp * temp)) {
				a.push_back(temp * temp);
			}
		}
		if(temp != 0LL)
			init(temp);
		temp ++;
		if(isPal(temp))
			if(isPal(temp * temp))
				a.push_back(temp * temp);
		init(temp);
		temp ++;
		if(isPal(temp))
			if(isPal(temp * temp))
				a.push_back(temp * temp);
		init(temp);
	}
}

int main() {
	init(0);
	a.push_back(9);
	a.push_back(1000000000000000LL);
	sort(a.begin(), a.end());
	int T;
	scanf(" %d", &T);
	for(int t = 0; t < T; t ++) {
		long long A, B;
		scanf(" %lld %lld", &A, &B);
		int lowl = 0, highl = 0;
		for(lowl = 0; a[lowl] < A; lowl ++);
		for(highl = 0; a[highl] <= B; highl ++);
		printf("Case #%d: %d\n", t + 1, highl - lowl);
	}
	return 0;
}
