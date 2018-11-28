#include <iostream>
#include <string>
#include <map>
#include <algorithm>
#include <fstream>

using namespace std;

void solve(string s, int&i, char color)
{
	while(i<s.size() && s[i] == color)
	{
		i++;
	}
}

void flip_color(char& c)
{
	if (c == '+')
		c = '-';
	else
		c = '+';
}

int main()
{
	ifstream cin("B-large.in");
	ofstream cout("output.txt");

	int n;
	cin >> n;
	
	for (int ci = 1; ci <= n; ci++)
	{
		string s;
		cin >> s;

		int res = 0;
		reverse(s.begin(), s.end());
		int i = 0;
		char color = '-';

		while (i < s.size() && s[i] == '+')
			i++;

		while (i < s.size())
		{
			solve(s, i, color);
			res++;
			flip_color(color);
		}

		cout << "Case #" << ci << ": " << res << endl;
	}


}