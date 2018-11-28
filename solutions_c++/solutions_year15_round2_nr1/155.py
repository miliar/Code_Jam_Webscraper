#include <iostream>
#include <string>
using namespace std;

long long rev(long long i) {
	long long res = 0;
	while (i>0) {
		res*=10;
		res += i%10;
		i/=10;
	}
	return res;
}

long long get001(long long x) {
	if (x <= 20) return x;
	string s = to_string(x);
	for (int i=s.length()/2; i<s.length(); i++)
		s[i] = '0';
	s[s.length()-1] = '1';
	long long tmp = stoll(s);
	if (x<tmp || rev(tmp)==tmp) {
		tmp -= 2;
		return get001(tmp);
	} else {
		return tmp;
	}
}

long long getAns(long long x) {
	if (x<=20) return x;
	long long tmp = get001(x);
	long long res = x - tmp + 1;
	tmp =  rev(tmp);
	return res + getAns(tmp);
}

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int Tn;
	cin >> Tn;
	long long n;
	for (int T=1;T<=Tn;T++) {
		cin >> n;
		
		cout << "Case #" << T << ": " << getAns(n) << endl;
	}
}