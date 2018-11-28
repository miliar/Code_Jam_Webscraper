#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <vector>
#include <queue>
#include <deque>
#include <cctype>
#include <bitset>
#include <algorithm>

using namespace std;

string work(int i, char ch)
{
	if (i == 0)
	{
		string s = "A";
		s[0] = ch;
		return s;
	}
	else {
		string left = work(i - 1, ch);
		string right;
		if (ch == 'R')
			right = work(i - 1, 'S');
		else if (ch == 'S')
			right = work(i - 1, 'P');
		else
			right = work(i - 1, 'R');
		if (left < right)
			return left + right;
		else
			return right + left;
	}
}

int main()
{
	int Cases;
	cin >> Cases;
	for (int Case = 1; Case <= Cases; Case++)
	{
		int N, R, P, S, r, p, s;
		string t;
		cin >> N >> R >> P >> S;
		string res = "Z";
		t = work(N, 'P');
		r = R; p = P; s = S;
		for (int i = 0; i < t.length(); i++)
		{
			if (t[i] == 'P')
				p--;
			else if (t[i] == 'R')
				r--;
			else
				s--;
		}
		if (p == r && r == s && s == 0)
			if (t < res)
				res = t;
		t = work(N, 'R');
		r = R; p = P; s = S;
		for (int i = 0; i < t.length(); i++)
		{
			if (t[i] == 'P')
				p--;
			else if (t[i] == 'R')
				r--;
			else
				s--;
		}
		if (p == r && r == s && s == 0)
			if (t < res)
				res = t;
		t = work(N, 'S');
		r = R; p = P; s = S;
		for (int i = 0; i < t.length(); i++)
		{
			if (t[i] == 'P')
				p--;
			else if (t[i] == 'R')
				r--;
			else
				s--;
		}
		if (p == r && r == s && s == 0)
			if (t < res)
				res = t;
		if (res != "Z")
			cout << "Case #" << Case << ": " << res << endl;
		else
			cout << "Case #" << Case << ": " << "IMPOSSIBLE" << endl;
	}
}