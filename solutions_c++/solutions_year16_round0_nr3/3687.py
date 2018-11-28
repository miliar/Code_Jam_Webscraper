#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <map>
#include <fstream>
using namespace std;

string GetNext(string current);
bool IsJam(string s, vector<int> &divs);
unsigned long long IsPrime(unsigned long long n);

int main() {
	ifstream inp("C-small-attempt1.in");
	ofstream outp("output.txt");
	int t;
	inp >> t;
	for (int i = 0; i < t; i++)
	{
		outp << "Case #" << i + 1 << ":\n";
		int n, j;
		inp >> n >> j;
		string s = "1";
		for (int i = 0; i < n - 2; i++) s += "0";
		s += "1";
		vector<int> divs(11);
		while (j)
		{
			if (IsJam(s, divs))
			{
				outp << s;
				for (int tt = 2; tt <= 10; tt++) outp << " " << divs[tt];
				outp << endl;
				j--;
			}
			s = GetNext(s);
		}
	}
}

string GetNext(string current) {
	current = current.substr(1, current.length() - 2);
	if (current[current.length() - 1] == '0')
	{
		current[current.length() - 1] = '1';
		return "1" + current + "1";
	}
	for (int i = current.length() - 1; i >= 0; i--)
	{
		if (current[i] == '1') current[i] = '0';
		else
		{
			current[i] = '1';
			break;
		}
	}
	return "1" + current + "1";
}

bool IsJam(string s, vector<int> &divs) {
	unsigned long long dec = 0, sz = s.length();
	for (int b = 2; b <= 10; b++)
	{
		dec = 0;
		for (int i = s.length() - 1, p = 0; i >= 0; i--, p++)
			dec += (s[i] - '0')*pow(b, p);
		int p = IsPrime(dec);
		if (p == 0) return false;
		else divs[b] = p;
	}
	return true;
}

unsigned long long IsPrime(unsigned long long n) {
	for (long long i = 2; i <= sqrt(n); i++)
	{
		if (n % i == 0)
			return i;
	}
	return 0;
}
