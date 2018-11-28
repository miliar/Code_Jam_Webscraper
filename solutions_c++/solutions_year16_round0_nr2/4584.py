#include <iostream>
#include <string>
using namespace std;

void doManeuver(string& s, int lastPos)
{
	for (int i = 0; i <= lastPos / 2; i++)
	{
		swap(s[i], s[lastPos - i]);
	}
	for (int i = 0; i <= lastPos; i++)
	{
		s[i] = (s[i] == '+') ? '-' : '+';
	}
}

int main(char* argv, int argc)
{
	int cases = 0;
	cin >> cases;
	for (int i = 1; i <= cases; i++)
	{
		int maneuver = 0;
		string s = "";
		cin >> s;
		char first = s[0];
		auto pos = s.find_first_not_of(first);
		while (pos != string::npos)
		{
			doManeuver(s, pos-1);
			first = s[0];
			pos = s.find_first_not_of(first);
			maneuver++;
		}
		if (s[0] == '-')
		{
			maneuver++;
		}
		cout << "Case #" << (i) << ": ";
		cout << maneuver << endl;
	}

}