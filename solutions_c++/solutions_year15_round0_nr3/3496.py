#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <string>
#include <cstdlib>
#include <queue>

using namespace std;



pair<char, char> quat_eval(pair<char, char> x, pair<char, char> y) {
	bool neg;
	if (x.first == '-') {
		if (y.first == '-') neg = false;
		else if (y.first == '+') neg = true;
	}
	else if (x.first == '+') {
		if (y.first == '-') neg = true;
		else if (y.first == '+') neg = false;
	}

	char ans;
	if (x.second == y.second) { neg = !neg; ans = '1'; }
	else if (x.second == '1') {
		ans = y.second;
	}
	else if (y.second == '1') {
		ans = x.second;
	}
	else if (x.second == 'i') {
		if (y.second == 'j') ans = 'k';
		if (y.second == 'k') { neg = !neg; ans = 'j'; }
	}
	else if (x.second == 'j') {
		if (y.second == 'i') { neg = !neg; ans = 'k'; }
		if (y.second == 'k') {ans = 'i'; }
	}
	else if (x.second == 'k') {
		if (y.second == 'i') {ans = 'j';}
		if (y.second == 'j') {neg = !neg; ans = 'i';}
	}

	if (neg) {
		return {'-', ans};
	}
	else return {'+', ans};

}

string solve(string s) {
	if (s.length() < 3) return "NO";

	pair<char, char> res = {'+', '1'};
	vector<int> pos;
	int i, j;
	for (i = 0; i < s.length()-2; i++) {
		res = quat_eval(res, {'+', s[i]});
		if (res == make_pair('+', 'i')) pos.push_back(i+1);
	}

	vector<int> pos2;
	for (i = 0; i < pos.size(); i++) {
		pair<char, char> res = {'+', '1'};
		for (j = pos[i]; j < s.length()-1; j++) {
			res = quat_eval(res, {'+', s[j]});
			if (res == make_pair('+', 'j')) pos2.push_back(j+1);
		}
	}

	sort(pos2.begin(), pos2.end());
	vector<int>::iterator it = unique(pos2.begin(), pos2.end());
	pos2.resize(distance(pos2.begin(),it));

	for (i = 0; i < pos2.size(); i++) {
		pair<char, char> res = {'+', '1'};
		for (j = pos2[i]; j < s.length(); j++) {
			res = quat_eval(res, {'+', s[j]});
		}
		if (res == make_pair('+', 'k')) return "YES";
	}

	return "NO";
}

int main() {

	freopen("C-small-attempt1.in", "r", stdin);

	int i, j, tc, d, p[1005], l, x;
	scanf("%d", &tc);
	string s, e;

	for (i = 0; i < tc; i++) {
		scanf("%d%d", &l, &x);
		cin >> s;
		e = "";
		for (j = 0; j < x; j++) {
			e += s;
		}
		cout << "Case #" << i+1 << ": " << solve(e) << "\n";
	}


	return 0;
}