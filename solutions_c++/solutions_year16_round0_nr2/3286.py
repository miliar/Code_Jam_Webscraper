#include <cstdio>
#include <iostream>
#include <algorithm>
#include <string>
#define ll long long
using namespace std;

bool seen[10]; 
int cnt;

int solve(string a) {
	int sz = 1;
	for (int i = 1; i < a.size(); i++) {
		if (a[i] != a[i-1]) sz++;
	}
	if (a[a.size()-1] == '-') {
		return sz;
	}
	else return sz-1;
}	

int main() {
	int T; scanf("%d", &T);
	for (int k = 1; k <= T; k++) {
		string s;
		cin >> s;
		printf("Case #%d: %d\n", k, solve(s));
	}
	return 0;
}