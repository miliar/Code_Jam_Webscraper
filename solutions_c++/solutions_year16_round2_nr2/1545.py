
#include "stdafx.h"
#include <fstream>
#include <iostream>
#include <string>

using namespace std;

void solve(string &s1, string &s2, string &res1, string &res2, long long &m_diff, int n)
{
	if (n == s1.length()) {
		long long r1, r2, diff;
		r1 = stoll(s1);
		r2 = stoll(s2);
		diff = abs(r1 - r2);
		if (diff > m_diff) return;
		else if (diff == m_diff && r1 > stoll(res1)) return;
		else if (diff == m_diff && r1 == stoll(res1) && r2 >= stoll(res2)) return;
		else {
			res1 = s1;
			res2 = s2;
			m_diff = diff;
			return;
		}
	}	
	if (n > 0) {
		long long r1 = stoll(s1.substr(0, n)) * (long long)pow(10, s1.length() - n);
		long long r2 = stoll(s2.substr(0, n)) * (long long)pow(10, s2.length() - n);
		if (r1 < r2) r1 = r1 + pow(10, s1.length() - n) - 1;
		else if (r2 < r1) r2 = r2 + pow(10, s1.length() - n) - 1;
		if (abs(r1 - r2) > m_diff) return;
	}

	if (s1[n] == '?' && s2[n] == '?') {
		s1[n] = '0';
		s2[n] = '1'; 
		solve(s1, s2, res1, res2, m_diff, n + 1);
		s1[n] = '1';
		s2[n] = '0';
		solve(s1, s2, res1, res2, m_diff, n + 1);
		s1[n] = '0';
		s2[n] = '9';
		solve(s1, s2, res1, res2, m_diff, n + 1);
		s1[n] = '9';
		s2[n] = '0';
		solve(s1, s2, res1, res2, m_diff, n + 1);
		s1[n] = '0';
		s2[n] = '0';
		solve(s1, s2, res1, res2, m_diff, n + 1);
		s1[n] = '?';
		s2[n] = '?';
	}
	else if (s1[n] == '?') {
		if (s2[n] != '0') {
			s1[n] = s2[n] - 1;
			solve(s1, s2, res1, res2, m_diff, n + 1);
		}
		s1[n] = s2[n];
		solve(s1, s2, res1, res2, m_diff, n + 1);
		if (s2[n] != '9') {
			s1[n] = s2[n] + 1;
			solve(s1, s2, res1, res2, m_diff, n + 1);
		}
		s1[n] = '0';
		solve(s1, s2, res1, res2, m_diff, n + 1);
		s1[n] = '9';
		solve(s1, s2, res1, res2, m_diff, n + 1);
		s1[n] = '?';
	}
	else if (s2[n] == '?') {
		if (s1[n] != '0') {
			s2[n] = s1[n] - 1;
			solve(s1, s2, res1, res2, m_diff, n + 1);
		}
		s2[n] = s1[n];
		solve(s1, s2, res1, res2, m_diff, n + 1);
		if (s1[n] != '9') {
			s2[n] = s1[n] + 1;
			solve(s1, s2, res1, res2, m_diff, n + 1);
		}
		s2[n] = '0';
		solve(s1, s2, res1, res2, m_diff, n + 1);
		s2[n] = '9';
		solve(s1, s2, res1, res2, m_diff, n + 1);
		s2[n] = '?';
	}
	else {
		solve(s1, s2, res1, res2, m_diff, n + 1);
	}

}

int main()
{
	ifstream cin("input.txt");
	ofstream cout("output.txt");

	int k;
	char buf[40];
	string s1, s2, res1, res2;
	 
	cin >> k;
	cin.getline(buf, 40);

	for (int t = 0; t < k; t++) {
		
		int idx;

		cin.getline(buf, 40);
		s1 = "";
		idx = 0;
		while (buf[idx] != ' ') {
			s1.push_back(buf[idx++]);
		}
		s2 = "";
		idx++;
		while (buf[idx] != '\0') {
			s2.push_back(buf[idx++]);
		}

		res1 = s1;
		res2 = s2;
		for (int i = 0; i < res1.length(); i++) {
			if (res1[i] == '?') res1[i] = '0';
		}
		for (int i = 0; i < res2.length(); i++) {
			if (res2[i] == '?') res2[i] = '0';
		}

		long long diff = abs(stoll(res1) - stoll(res2));
		solve(s1, s2, res1, res2, diff, 0);

		cout << "Case #" << t+1 << ": ";
		cout << res1 << " " << res2 << endl;

	}

	cin.close();
	cout.close();

	return 0;
}
