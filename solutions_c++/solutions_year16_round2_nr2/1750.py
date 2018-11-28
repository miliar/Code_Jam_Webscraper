#pragma comment(linker, "/STACK:134217728")
#define _CRT_SECURE_NO_WARNINGS

#include <cstdio>
#include <iostream>
#include <vector>
#include <queue>
#include <map>
#include <set>
#include <string>
#include <numeric>
#include <complex>
#include <functional>
#include <cmath>
#include <time.h>

using namespace std;

typedef unsigned long long LL;

struct answ{
	string s1;
	string s2;
	LL d;
	answ(string s1,string s2,LL d) {
		this->s1 = s1;
		this->s2 = s2;
		this->d = d;
	}
};

bool operator <(const answ a, const answ b) {
	return a.d < b.d || a.d == b.d && a.s1 < b.s1
		|| a.d == b.d && a.s1 == b.s1 && a.s2 < b.s2;
}

char LT(char c) {
	if (c == '0')
		return '9';
	return c - 1;
}
char GT(char c) {
	if (c == '9')
		return '0';
	return c + 1;
}
answ res(string s1, string s2) {
	LL a = 0; 
	LL b = 0;
	for (int i = 0; i < s1.size(); i++) {
		a = a * 10 + s1[i] - '0';
		b = b * 10 + s2[i] - '0';
	}
	if (a < b)
		swap(a, b);
	return answ(s1,s2, a - b);
}
answ calc(string s1, string s2, int pos) {
	if (pos == s1.size()) {
		return res(s1, s2);
	}
	if (s1[pos] == '?' && s2[pos] == '?') {
		s1[pos] = '0';
		s2[pos] = '0';
		answ res = calc(s1, s2, pos + 1);
		s1[pos] = '9';
		res = min(calc(s1, s2, pos + 1), res);
		s1[pos] = '0';
		s2[pos] = '9';
		res = min(calc(s1, s2, pos + 1), res);
		s1[pos] = '1';
		s2[pos] = '0';
		res = min(calc(s1, s2, pos + 1), res);
		s1[pos] = '0';
		s2[pos] = '1';
		res = min(calc(s1, s2, pos + 1), res);
		s1[pos] = s2[pos] = '?';
		return res;
	}
	else if (s1[pos] == '?') {
		s1[pos] = LT(s2[pos]);
		answ res = calc(s1, s2, pos + 1);
		s1[pos] = GT(s2[pos]);
		res = min(calc(s1, s2, pos + 1), res);
		s1[pos] = s2[pos];
		res = min(calc(s1, s2, pos + 1), res);
		s1[pos] = '0';
		res = min(calc(s1, s2, pos + 1), res);
		s1[pos] = '9';
		res = min(calc(s1, s2, pos + 1), res);
		s1[pos] = '?';
		return res;
	}
	else if (s2[pos] == '?') {
		s2[pos] = LT(s1[pos]);
		answ res = calc(s1, s2, pos + 1);
		s2[pos] = GT(s1[pos]);
		res = min(calc(s1, s2, pos + 1), res);
		s2[pos] = s1[pos];
		res = min(calc(s1, s2, pos + 1), res);
		s2[pos] = '0';
		res = min(calc(s1, s2, pos + 1), res);
		s2[pos] = '9';
		res = min(calc(s1, s2, pos + 1), res);
		s2[pos] = '?';
		return res;
	}
	else {
		return calc(s1,s2,pos + 1);
	}
}
int main()
{
	freopen("input.in","r",stdin);
	freopen("output.out","w",stdout);
	int k;
	cin >> k;
	int t = 1;
	while (k-- > 0) {
		string s1, s2;
		cin >> s1 >> s2;
		answ aa = calc(s1, s2,0);
		printf("Case #%d: ",t++);
		cout << aa.s1 << ' ' << aa.s2 << endl;
	}
	return 0;
}