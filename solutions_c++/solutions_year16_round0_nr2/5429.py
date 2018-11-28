
#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <queue>

using namespace std;

int number(string s)
{
	int res = 0;
	for (int i = 0; i < s.length(); i++) {
		res = res * 2 + ((s[i] == '-') ? 1 : 0);
	}
	return res;
}

string pattern(int n, int len)
{
	string s = "";
	for (int i = 0; i < len; i++) {
		s = ((n % 2 == 0) ? '+' : '-') + s;
		n /= 2;
	}
	return s;
}

string swap_pattern(string t, int len)
{
	string s = "";
	for (int i = 0; i < len; i++) {
		s = s + ((t[len - i - 1] == '-') ? '+' : '-');
	}
	for (int i = len; i < t.length(); i++) {
		s = s + t[i];
	}
	return s;
}

int main()
{
	ifstream fin("input.txt");
	ofstream fout("output.txt");

	int cases, len;
	int path[1024];
	char buf[100];
	queue<int> q;
	string s;
	
	fin >> cases;
	fin.getline(buf, 100);
	for (int i = 1; i <= cases; i++) {
		
		for (int t = 0; t < 1024; t++)
			path[t] = -1;

		fin.getline(buf, 100);
		s = string(buf);
		len = s.length();

		q.push(number(s));
		path[number(s)] = 0;

		while (!q.empty()) {
			int v = q.front();
			if (v == 0) break;
			string t = pattern(v, len);

			for (int i = 1; i <= len; i++) {
				int u = number(swap_pattern(t, i));
				if (path[u] == -1) {
					path[u] = path[v] + 1;
					q.push(u);
				}
			}
			q.pop();
		}

		while (!q.empty()) q.pop();

		fout << "Case #" << i << ": " << path[0] << endl;
		
	}

	fin.close();
	fout.close();
	return 0;
}
