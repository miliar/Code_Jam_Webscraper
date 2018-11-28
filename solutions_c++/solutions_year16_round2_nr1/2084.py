#include<iostream>
#include<fstream>
#include<algorithm>
#include<vector>
#include<queue>
#include<string>
using namespace std;

ifstream in;
ofstream out;
int test;
string s;
int a[26];
string ans;
vector<string> t;

bool Has(int i)
{
	int check;
	for (int k = 0; k < t[i].size(); ++k)
	{
		check = 0;
		if (i == 3 && t[i][k] == 'E') check = 1;
		if (i == 7 && t[i][k] == 'E') check = 1;
		if (i == 9 && t[i][k] == 'N') check = 1;
		if (a[t[i][k] - 'A'] <= check)
			return false;
	}
	return true;
}
void Get(int i)
{
	for (int k = 0; k < t[i].size(); ++k)
		a[t[i][k] - 'A']--;
	ans += (i + '0');
}
int main()
{
	in.open("A-large.in");
	//in.open("input.txt");
	out.open("output.txt");

	for (int i = 0; i <= 9; ++i)
	{
		string tt;
		if (i == 0) tt = "ZERO";
		else if (i == 1) tt = "ONE";
		else if (i == 2) tt = "TWO";
		else if (i == 3) tt = "THREE";
		else if (i == 4) tt = "FOUR";
		else if (i == 5) tt = "FIVE";
		else if (i == 6) tt = "SIX";
		else if (i == 7) tt = "SEVEN";
		else if (i == 8) tt = "EIGHT";
		else if (i == 9) tt = "NINE";
		t.push_back(tt);
	}
	

	in >> test;
	for (int t = 1; t <= test; ++t)
	{
		ans = "";
		for (int i = 0; i < 26; ++i)
			a[i] = 0;

		// input
		in >> s;

		for (int i = 0; i < s.size(); ++i)
			a[s[i] - 'A']++;
		
		while (a['Z'-'A'] > 0)
			Get(0);
		while (a['W'-'A'] > 0)
			Get(2);
		while (a['U'-'A'] > 0)
			Get(4);
		while (a['X'-'A'] > 0)
			Get(6);
		while (a['G'-'A'] > 0)
			Get(8);
		while (a['O'-'A'] > 0)
			Get(1);
		while (a['R'-'A'] > 0)
			Get(3);
		while (a['F'-'A'] > 0)
			Get(5);
		while (a['V'-'A'] > 0)
			Get(7);
		while (a['I'-'A'] > 0)
			Get(9);

		sort(ans.begin(), ans.end());

		/*
		z = 0
		w = 2
		v = 5, 7
		x = 6
		u = 4
		h = 3, 8
		g = 8
		*/

		// output
		out << "Case #" << t << ": " << ans << endl;
	}

	in.close();
	out.close();
	return 0;
}