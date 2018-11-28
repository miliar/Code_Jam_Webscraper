#include<iostream>
#include<iomanip>
#include<queue>
#include<stack>
#include<sstream>
#include<algorithm>
#include<list>
#include<map>
#include<vector>
#include<string>
#include<cstring>
#include<cstdlib>
#include<cstdio>
#include<cmath>
#include<set>

#define Author "DemoVersion"
#define DBG(x) cout<<#x<<" = "<<x<<";\n"


using namespace std;
int dx[] = { 0,0,-1,1,1,-1,1,-1 };
int dy[] = { 1,-1,0,0,1,1,-1,-1 };
typedef pair<int, int> pii;
typedef long long ll;
typedef unsigned long long ull;

/// Hey yo man, lets do some contest!
vector<int> primes;
string plus_s(string in1, string in2) {
	reverse(in1.begin(), in1.end());
	reverse(in2.begin(), in2.end());
	int i,carry = 0,s;
	string ret = "";
	for (i = 0;i < min(in1.length(), in2.length());i++) {
		s = carry + in1[i] + in2[i] - '0' - '0';
		carry = s / 2;
		s %= 2;
		ret += (char)(s + '0');
	}
	for (;i < in1.length();i++) {
		s= carry + in1[i]- '0';
		carry = s / 2;
		s %= 2;
		ret += (char)(s + '0');
	}
	for (;i < in2.length();i++) {
		s = carry + in2[i] - '0';
		carry = s / 2;
		s %= 2;
		ret += (char)(s + '0');
	}
	if (carry) {
		ret+= (char)(carry + '0');
	}
	reverse(ret.begin(), ret.end());
	return ret;
}
string plus_i(string in1, int in2) {
	stringstream ss;
	ss << in2;
	return plus_s(in1, ss.str());
}
int isDiv(string &str,int base, int mod) {
	int i;
	int alpha = 0;
	for (i = 0;i < str.length();i++) {
		alpha = alpha * base + str[i] - '0';
		alpha %= mod;
	}
	return (alpha == 0);
}
int sureDivisable(string &str,int base) {
	for (int i = 0;i < primes.size();i++) {
		if (isDiv(str, base, primes[i])) {
			return primes[i];
		}
	}
	return 0;
}
vector<int> divs;
int isJamCoin(string &str) {
	int i;
	divs.clear();
	for (i = 2;i <= 10;i++) {
		int alpha = sureDivisable(str, i);
		if (alpha == 0)break;
		divs.push_back(alpha);
	}
	if (i == 11)return 1;
	return 0;
}
void generate(int size,int cnt) {
	string it(size-1, '0');
	it[0] = '1';
	string num;
	for (;cnt;it = plus_i(it, 1)) {
		num = it + string("1");
		if (isJamCoin(num)) {
			cout << num;
			for (int i=0;i < divs.size();i++) {
				cout <<' '<< divs[i];
			}
			cout << endl;
			cnt--;
		}
	}
}
void generate_primes() {
	const int maax = 5000;
	short is_no_prime[maax] = {0};
	int i, j;
	for (i = 2;i < maax;i++) {
		if (is_no_prime[i])continue;
		primes.push_back(i);
		for (j = i+i;j < maax;j += i) {
			is_no_prime[j] = 1;
		}
	}
}
int main() {

	int test, t;
	cin >> t;
	generate_primes();
	int siz, cnt;
	for (test = 1;test <= t;test++) {
		cin >> siz >> cnt;
		cout << "Case #" << test << ":\n";
		generate(siz, cnt);
	}
	return 0;
}
