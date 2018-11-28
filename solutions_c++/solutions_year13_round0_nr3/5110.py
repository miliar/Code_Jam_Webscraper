using namespace std;

#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <iostream>
#include <algorithm>
#include <string>
#include <vector>

vector <long long> ans;

void isAnAnswer (string str) {
	char copy [20];
	long long num, temp, tot;
	for (int i = str.size () - 1, j = 0, k = 0; i >= 0; --i) if (str [i] != '0') {
		while (str [j] == '0') ++j;
		while (j <= i) copy [k++] = str [j++];
		copy [k] = 0;
	}
	num = atoi (copy);
	num *= num;
	temp = num;
	tot = 0;
	while (temp) {
		copy [tot++] = temp % 10LL;
		temp /= 10LL;
	}
	for (long long i = 0, len = tot - 1; i < len; ++i, --len) if (copy [i] != copy [len]) return;
	ans.push_back (num);
}

void makePalindrome (string str) {
	string rev = str;
	reverse (rev.begin (), rev.end ());
	isAnAnswer (str + rev);
	for (char i = '0'; i <= '9'; ++i) isAnAnswer (str + i + rev);
}

void pregen (string str) {	
	if (str.length () >= 4) makePalindrome (str);
	else for (char i = '0'; i <= '9'; ++i) pregen (str + i);
}

int main () {
	//freopen ("input.txt", "r", stdin);
	//freopen ("output.txt", "w", stdout);
	pregen ("");
	sort (ans.begin (), ans.end ());
	int t;
	cin >> t;
	for (int cs = 1; cs <= t; ++cs) {
		long long a, b;
		cin >> a >> b;
		if (a > b) swap (a, b);		
		cout << "Case #" << cs << ": " << - (int) (ans.begin () - upper_bound (ans.begin (), ans.end (), b)) + (int) (ans.begin () - lower_bound (ans.begin (), ans.end (), a)) << endl;
	}
	return 0;
}