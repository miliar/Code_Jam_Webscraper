// Problem C - Coin Jam

#include <iostream>
#include <fstream>
#include <cmath>
using namespace std;

int n = 16;
int k = 50;
int cnt = 0;
string jams[500];
long long powertwo[32];
long long divisors[500][11];

string convert_string(long long m, int len)
{
	string s = "";
	long long l = m;
	for (int i = 0; i < len; i++)
	{
		if (l % 2) 
			s = '1' + s;
		else
			s = '0' + s;
		l /= 2;
	}
	return '1' + s + '1';
}

long long to_base(string s, int b)
{
	long long total = 0;
	for (int i = 0; i < s.length(); i++)
		total = total * b + ((s[i] == '1') ? 1 : 0);
	return total;
}

long long is_prime(long long m)
{
	if (m % 2 == 0) return 2;
	for (long long i = 3; i <= sqrt(m); i += 2)
	{
		if (m % i == 0)
			return i;
	}
	return 1;
}

bool valid(string s)
{
	long long setdiv[11];
	for (int i = 2; i <= 10; i++)
	{
		long long m = to_base(s, i);
		long long divi = is_prime(m);
		if (divi == 1) 
			return false;
		setdiv[i] = divi;
	}
	for (int i = 2; i <= 10; i++)
		divisors[cnt][i] = setdiv[i];
	return true;
}

int main()
{
	ifstream fin("C-small-attempt0.in");
	ofstream fout ("C-small.txt");
	fout << "Case #1:" << endl;
	string converted;
	long long curr = 0;
	while (cnt < k)
	{
		converted = convert_string(curr, n - 2);
		if (valid(converted))
		{
			jams[cnt] = converted;
			cnt++;
		}
		curr++;
	}
	for (int i = 0; i < k; i++)
	{
		fout << jams[i];
		for (int j = 2; j <= 10; j++)
			fout << " " << divisors[i][j];
		fout << endl;
	}



	return 0;
}
