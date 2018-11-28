#include <cstdio>
#include <iostream>
#include <cstdlib>
#include <set>
using namespace std;

int p[] = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29};
int get(string &s, int base, int mod) {
	int ans = 0;
	for (int i=0; i<s.length(); i++) {
		ans = (ans * base) % mod;
		ans += (s[i] - '0');
	}
	return ans % mod;
}

int valid[20];
bool check(string s) {
	for (int base = 2; base <= 10; base++) {
		bool ok = false;
		for (int i=0; i<10 && !ok; i++) {
			int prime = p[i];
			if (get(s, base, prime) == 0) {
				ok = true;
				valid[base] = prime;
			}
		}
		if (!ok) return false;
	}
	return true;
}

string getR(int n) {
	if (n == 0) return "";
	return getR(n-1) + char('0' + rand()%2);
}

int main() {
	srand(2011);
	int t, n, j;
	cin >> t >> n >> j;
	printf("Case #1:\n");
	set <string> se;
	while(j) {
		string s = "1" + getR(n-2) + "1";
		if (se.find(s) != se.end()) continue;
		se.insert(s);
		if (check(s)) {
			cout << s;
			for (int base = 2; base <= 10; base++) cout << " " << valid[base];
			cout << endl;
			j--;
		}
	}
}
