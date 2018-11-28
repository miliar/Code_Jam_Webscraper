#include <iostream>

using namespace std;

string flipPancakes(string s)
{
	int index = s.rfind("-");

	for(int i = 0; i < index + 1; i++)
	{
		if(s[i] == '+')
			s[i] = '-';
		else if (s[i] == '-')
			s[i] = '+';
	}

	return s;
}

int getFlips(string s, int &count)
{
	if(s.find("-") == string::npos)
		return count;

	s = flipPancakes(s);

	count = 1 + getFlips(s, count);

	return count;
}

int main()
{
	int t, count;

	string s;

	cin >> t;

	for(int i = 0; i < t; i++) {
		count = 0;
		cin >> s;
		cout << "Case #" << i+1 << ": " << getFlips(s, count) << endl;
	}
}
