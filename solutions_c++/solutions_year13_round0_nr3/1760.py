//============================================================================
// Name        : GCJC.cpp
// Author      : Hossam El-Deen, Waleed, Bassem
// Version     :
// Copyright   : 
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <utility>
#include <algorithm>
#include <sstream>
#include <cstdio>
using namespace std;

char temp;
int temp2;

void nextPalindrome(string& s) {
	int i = s.size() / 2;
	while(i < s.size() && s[i] == '9') {
		s[i] = '0';
		s[s.size() - 1 - i] = '0';
		++i;
	}
	if (i != s.size()) {
		++s[i];
		if (i != s.size() - 1 - i)
			++s[s.size() - 1 - i];
		return;
	}
	for (int i = 1; i < s.size(); ++i)
		s[i] = '0';
	s[0] = '1';
	s += '1';
}

string sqr(string& s) {
	reverse(s.begin(), s.end());
	string res;
	for (unsigned int i = 0; i < s.size(); ++i) {
		s[i] -= '0';
		res += (char)0;
		res += (char)0;
	}

	for (unsigned int i = 0; i < s.size(); ++i)
		for (unsigned int j = 0; j < s.size(); ++j) {
			res[i + j] += s[i] * s[j];
			if (res[i + j] > 9) {
				temp = res[i + j] / 10;
				res[i + j] -= temp * 10;
				res[i + j + 1] += temp;
			}
		}
	for (unsigned int i = 0; i < res.size(); ++i)
		if (res[i] > 9) {
			temp = res[i] / 10;
			res[i] -= temp * 10;
			res[i + 1] += temp;
		}
	temp = res.size() - 1;
	while(res[temp] == 0)
		--temp;
	res.erase(res.begin() + temp + 1, res.end());

	reverse(s.begin(), s.end());
	for (unsigned int i = 0; i < s.size(); ++i)
		s[i] += '0';

	reverse(res.begin(), res.end());
	for (unsigned int i = 0; i < res.size(); ++i)
		res[i] += '0';
	return res;
}

bool isPalindrome(string& s) {
	temp2 = s.size() / 2;
	for (int i = 0; i < temp2; ++i)
		if (s[i] != s[s.size() - 1 - i])
			return 0;
	return 1;
}

bool comp1(string& A, string& s) {
	if (A.size() < s.size())
		return 1;
	if (A.size() > s.size())
		return 0;
	for (unsigned int i = 0; i < s.size(); ++i)
		if (A[i] < s[i])
			return 1;
		else if (A[i] > s[i])
			return 0;
	return 1;
}

bool comp2(string& B, string& s) {
	if (B.size() > s.size())
		return 1;
	if (B.size() < s.size())
		return 0;
	for (unsigned int i = 0; i < s.size(); ++i)
		if (B[i] > s[i])
			return 1;
		else if (B[i] < s[i])
			return 0;
	return 1;
}

int main() {
	freopen("C-large-1.in", "rt", stdin);
	freopen("C-large-1.out", "wt", stdout);
	string s = "1", tempo;
	int ctr = 0;
	string arr[100000];
	while(s.size() < 8) {
		tempo = sqr(s);
		if (isPalindrome(tempo)) {
			arr[ctr++] = tempo;
		}
		nextPalindrome(s);
	}
	int T, ctr2;
	cin >> T;
	string A, B;
	for (int i = 0; i < T; ++i) {
		cout << "Case #" << i + 1 << ": ";
		cin >> A >> B;
		ctr2 = 0;
		for (int i = 0; i < ctr; ++i)
			if (comp1(A, arr[i]) && comp2(B, arr[i]))
				++ctr2;
		cout << ctr2 << endl;
	}
	return 0;
}






















