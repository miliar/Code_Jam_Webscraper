#include <cstdlib>

#include <iostream>
#include <string>
using namespace std;

string s;

int check_s()
{
	int c = 0;
	bool f = true;
	for (int i = s.size() - 1; i >= 0; i--)
	{
		if ((f && s[i] == '-') || (!f && s[i] == '+'))
		{
			c++;
			f = !f;
		}
	}
	return c;
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int t;
	std::cin >> t;
	for (int i = 0; i < t; i++)
	{
		cin >> s;
		cout << "Case #" << i + 1 << ": " << check_s() << "\n";
	}
	return 0;
}