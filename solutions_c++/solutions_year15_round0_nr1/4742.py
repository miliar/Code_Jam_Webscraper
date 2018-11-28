#include <algorithm>
#include <iostream>
#include <string>
#include <vector>
#include <memory.h>

using namespace std;

string del(string s) {
	string st = "";
	for (int i = 1; i < s.size(); ++i) st += s[i];
	return st;
}

int a[1111], n;

bool f(int v) {
	int sum = a[0] + v;
	for (int i = 1; i <= n; ++i) {
		if (i > sum) return false;
		sum += a[i];
	}
	return true;
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int test;
	cin >> test;
	for (int tst = 1; tst <= test; ++tst) {
		cin >> n;
		string s;   
		getline(cin, s);  
		s = del(s);          
		for (int i = 0; i <= n; ++i) {
			a[i] = s[i] - '0';
		} 
		int l = 0, r = 10000;
		while (r - l > 1) {
			int mid = (l + r) / 2;
			if (f(mid)) r = mid; else l = mid;
		}           
		int ans = r;
		if (f(l)) ans = l;  
		cout << "Case #" << tst << ": " << ans << endl; 
	}
	return 0;
}          