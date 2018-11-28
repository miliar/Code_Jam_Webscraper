// a.cpp : Problem A
// author : John Thekkekara
//

#include <math.h>
#include <iostream>
#include <vector>
#include <array>
#include <list>
#include <map>
#include <string>


#define ll long long int
#define BIG_PRIME 1000000007

using namespace std;

string DIGITS[] = { "ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE" };

string str;
string out;
int letters[26];

void solve(int t)
{

	cin >> str;
	out = "";
	sort(str.begin(), str.end());
	memset(letters, 0, sizeof(letters));

	for (auto istr = str.begin(); istr != str.end(); istr++)
	{
		letters[*istr - 'A']++;
	}

	int N = letters['Z' - 'A'];

	for (int i = 0; i < N; i++)
	{
		for (auto istr = DIGITS[0].begin(); istr != DIGITS[0].end(); istr++)
		{
			letters[*istr - 'A']--;
		}
		out += '0';
	}

	N = letters['W' - 'A'];
	for (int i = 0; i < N; i++)
	{
		for (auto istr = DIGITS[2].begin(); istr != DIGITS[2].end(); istr++)
		{
			letters[*istr - 'A']--;
		}
		out += '2';
	}
	
	N = letters['U' - 'A'];
	for (int i = 0; i < N; i++)
	{
		for (auto istr = DIGITS[4].begin(); istr != DIGITS[4].end(); istr++)
		{
			letters[*istr-'A']--;
		}
		out += '4';
	}
	
	N = letters['X' - 'A'];
	for (int i = 0; i < N; i++)
	{
		for (auto istr = DIGITS[6].begin(); istr != DIGITS[6].end(); istr++)
		{
			letters[*istr - 'A']--;
		}
		out += '6';
	}

	N = letters['G' - 'A'];
	for (int i = 0; i < N; i++)
	{
		for (auto istr = DIGITS[8].begin(); istr != DIGITS[8].end(); istr++)
		{
			letters[*istr - 'A']--;
		}
		out += '8';
	}
	
	N = letters['T' - 'A'];
	for (int i = 0; i < N; i++)
	{
		for (auto istr = DIGITS[3].begin(); istr != DIGITS[3].end(); istr++)
		{
			letters[*istr - 'A']--;
		}
		out += '3';
	}

	N = letters['S' - 'A'];
	for (int i = 0; i < N; i++)
	{
		for (auto istr = DIGITS[7].begin(); istr != DIGITS[7].end(); istr++)
		{
			letters[*istr - 'A']--;
		}
		out += '7';
	}

	N = letters['V' - 'A'];
	for (int i = 0; i < N; i++)
	{
		for (auto istr = DIGITS[5].begin(); istr != DIGITS[5].end(); istr++)
		{
			letters[*istr - 'A']--;
		}
		out += '5';
	}

	N = letters['I' - 'A'];
	for (int i = 0; i < N; i++)
	{
		for (auto istr = DIGITS[9].begin(); istr != DIGITS[9].end(); istr++)
		{
			letters[*istr - 'A']--;
		}
		out += '9';
	}


	
	N = letters['O' - 'A'];
	for (int i = 0; i < N; i++)
	{
		for (auto istr = DIGITS[1].begin(); istr != DIGITS[1].end(); istr++)
		{
			letters[*istr - 'A']--;
		}
		out += '1';
	}
	sort(out.begin(), out.end());
	cout << "Case #" << t << ": " << out << endl;
}

int main()
{
	int T;
	scanf("%d", &T);
	for (int t = 1; t < T + 1; t++)
	{
		solve(t);
	}
	return 0;
}


