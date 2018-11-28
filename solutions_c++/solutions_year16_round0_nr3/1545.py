#include <iostream>
#include <sstream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cctype>
#include <cstring>
#include <vector>
#include <list>
#include <queue>
#include <deque>
#include <stack>
#include <map>
#include <set>
#include <algorithm>
#include <numeric>
#include <ctime>
#include <fstream>
#include <iomanip>
#include <stdexcept>
#include <functional>
#include <math.h>
#include <utility>
#include <sstream>
#pragma comment(linker, "/STACK:133217728")

using namespace std;

vector <int> primes;
bool pr[1000100];

void getPrimes() {
	for(int i=2; i<=1000000; i++) {
		if(!pr[i]) {
			primes.push_back(i);
			if(i < 10000)
				for(int j = i * i; j <= 1000000; j += i)
					pr[j] = 1;
		}
	}
}

int f(int n) {
	int res = 0;
	while(n) {
		res += n & 1;
		n /= 2;
	}
	return res;
}

long long pw(int a, int b) {
	long long res = 1;
	for(int i=1; i<=b; i++)
		res = res * a;
	return res;
}

long long pwMod(int a, int b, int c) {
	long long res = 1;
	for(int i=1; i<=b; i++)
		res = (res * a) % c;
	return res;
}

long long calc(int len, int mask, int p, int mod) {
	long long res = 1 + pwMod(p, len-1, mod);
	for(int i=0; i<len; i++)
		if(mask & (1 << i))
			res =(res + pwMod(p, i + 1, mod)) % mod;

	return res;
}

long long toDecimal(int len, int mask, int p) {
	long long res = 1 + pw(p, len-1);
	for(int i=0; i<len; i++)
		if(mask & (1 << i))
			res += pw(p, i + 1);

	return res;
}

string toBinary(int len, int mask) {
	string res = "1";
	for(int i=0; i<len-2; i++)
		if(mask & (1 << i))
			res += "1";
		else
			res += "0";
	res += "1";

	reverse(res.begin(), res.end());
	return res;
}

int check2(int n, int mask) {
	
	vector<int>	ans;
	for(int p=2; p<=10; p++) {
	long long nn = toDecimal(n, mask, p);
	for(int i = 0; i < primes.size() && 1LL * primes[i] * primes[i] <= nn; i++)
		if(!(nn % primes[i])) {
			ans.push_back(primes[i]);
			break;
		}
	}
	return ans.size() == 9;
}

void check() {
	for(int i=1; i<=50; i++) {
		int mask;
		cin >> mask;
		cout << check2(16, mask) << endl;
	}
}
int main() {  
	freopen("in.txt", "r", stdin);
	freopen("ans.txt", "w", stdout);
	getPrimes();
	
	int T;
	cin >> T;
	for(int t=1; t<=T; t++) {
		int n, cnt;
		cin >> n >> cnt;
		cout << "Case #" << t << ":\n";
		for(int mask = 0; mask < (1 << (n-2)) && cnt; mask++) {
			if(f(mask) & 1) continue;
			vector<int> ans;
			for(int p = 2; p <= 10; p++) {
				if(p & 1) {
					ans.push_back(2);
					continue;
				}
				//long long nn = toDecimal(n, mask, p);
				//cout << nn << " " ;
				for(int i = 0; i < 100; i++)
					if(!calc(n, mask, p, primes[i])) {
						ans.push_back(primes[i]);
						break;
					}
			}
			if(ans.size() == 9) {
				cnt--;
				cout << toBinary(n, mask) << " ";
				for(int i=0; i<ans.size(); i++)
					cout << ans[i] << " ";
				cout << endl;
			}
		}
		
	}
	
	return 0;
}