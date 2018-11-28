#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <fstream>

using namespace std;

int d[5000][5000];

char f(char a){
	if (a == 'R') return 'S';
	if (a == 'P') return 'R';
	if (a == 'S') return 'P';
}
char c[3] = { 'P', 'R', 'S' };

string rec(char c, int n){
	string s = " ";
	if (n == 0) {
		s[0] = c;
		return s;
	}
	string a = rec(c, n - 1);
	string b = rec(f(c), n - 1);
	if (a > b) swap(a, b);
	return a + b;
}

string solve(int n, int r, int p, int s){
	string result = "Z";
	//cout << n << " " << r <<  " " << p << " "  << s << endl;
	for (char t = 0; t < 3; t++){
		string a = rec(c[t], n);
		vector<int> cnt(256);
		for (int i = 0; i < 1 << n; i++){
			cnt[a[i]]++;
		}
		if (cnt['R'] == r && cnt['P'] == p && cnt['S'] == s){
			if (a < result) result = a;
		}
	}
	if (result == "Z") return "IMPOSSIBLE";
	return result;
}

char win(string s){
	if (s.length() == 1) return s[0];
	char a = win(s.substr(0, s.length() / 2));
	char b = win(s.substr(s.length() / 2, s.length() / 2));
	if (a == b || a == 'Z' || b == 'Z') return 'Z';

	char r = 'P' + 'R' + 'S' - a - b;
	if (r == 'R') return 'S';
	if (r == 'S') return 'P';
	if (r == 'P') return 'R';
}

string solve1(int n, int r, int p, int s){
	string result = "Z";
	vector<pair<int, char> > v(1 << n);
	for (int i = 0; i < r; i++){
		v[i] = { i, 'R' };
	}
	for (int i = r; i < r + p; i++){
		v[i] = { i, 'P' };
	}
	for (int i = r + p; i < r + p + s; i++){
		v[i] = { i, 'S' };
	}
	do{
		string s = "";
		for (int i = 0; i < (1 << n); i++){
			s += v[i].second;
		}
		if (win(s) != 'Z'){
			if (result > s) result = s;
		}
	}
	while (next_permutation(v.begin(), v.end()));
	return result == "Z" ? "IMPOSSIBLE" : result;
}

//string solve(){
//	int n, a, b, c;
//	cin >> n >> a >> b >> c;
//
//	for (int i )
//
//	vector<char> p(1 << n);
//	int i = 0;
//	for (int j = 0; j < a; j++) p[i++] = 'R';
//	for (int j = 0; j < b; j++) p[i++] = 'P';
//	for (int i = 0; i < c; i++) p[i++] = 'S';
//	vector<int> xx(1 << n);
//	for (int i = 0; i < 1 << n; i++) p[i] = i;
//	for (;;){
//		vector<char> prev(1 << n);
//		
//		for (int i = 0; i < 1 << n; i++) prev[i] = p[xx[i]];
//
//		for (int lev = 0; lev < n; lev++){
//			vector<char> x(1 << lev);
//			for (int i = 0; i < 1 << lev; i++) {
//				if (prev[2 * i] == prev[2 * i + 1])
//				x[i] =  ? min(prev[2 * i], prev[2 * i + 1]);
//			}
//			prev = x;
//		}
//		next_permutation(xx.begin(), xx.end());
//	}
//	return 
//}

int main() {
	//cout << win("PRRS") << endl;
	freopen("in.txt", "r", stdin);
	freopen("out1.txt", "w", stdout);
	int tests;
	cin >> tests;
	for (int t = 0; t < tests; t++){
		int n, r, p, s;
		cin >> n >> r >> p >> s;
		cout << "Case #" + to_string(t + 1) + ": " + solve(n, r, p, s) << endl;
			//<< " " << solve(n, r, p, s) << endl;
	}
	return 0;
}