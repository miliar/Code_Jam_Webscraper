#include <cstdio>
#include <cstdlib>
#include <cassert>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;
typedef long long LL;
typedef unsigned long long ULL;

string compress(string s){
	string res;
	res += s[0];
	for (int i = 1; i < s.length(); i++){
		if (s[i] != res[res.length() - 1]){
			res += s[i];
		}
	}
	return res;
}

int main() {
	FILE *fin = freopen("B-large.in", "r", stdin);
	assert(fin != NULL);
	FILE *fout = freopen("B-large.out", "w", stdout);
	int T;
	cin >> T;
	string s;
	bool first = true;
	for (int t = 1; t <= T; t++){
		if (first) first = false;
		else cout << endl;
		cin >> s;
		cout << "Case #" << t << ": ";
		string r = compress(s);
		int i = 0;
		if (r[r.length() - 1] == '+') cout << r.length() - 1;
		else cout << r.length();
	}
	exit(0);
}