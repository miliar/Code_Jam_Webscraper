//#include<iostream>
#include<string>
#include<fstream>
using namespace std;
long long dp[200];
int cnt(string s)
{
	string t = "";

		t += s[0];
	for (int i = 1; i < (int)s.length(); i++)		if (s[i] != s[i - 1]) t += s[i];
	if (t[t.length() - 1] == '+') return t.length() - 1;
	return t.length();
}
int main()
{
	ifstream cin("input.txt");
	ofstream cout("output.txt");
	int T;
	cin >> T;
	string s;
	for (int i = 1; i <= T; i++)
	{
		cin >> s;
		cout << "Case #" << i << ": " << cnt(s) << endl;
	}

		

	return 0;
}