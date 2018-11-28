#include <iostream>
#include <sstream>
#include <string>

using namespace std;

stringstream out;

void function()
{
	string input;
	cin >> input;
	char previous = '1';
	int counter = 0;
	for (int i = 0; i < input.length(); i++)
	{
		if (input[i] == '-')
		{
			if (previous == '+')
				counter += 2;
			else if (previous == '1')
				counter++;
		}
		previous = input[i];
	}
	out << counter << endl;
}

int main()
{
	ios_base::sync_with_stdio(0);
	int t;
	cin >> t;

	for (int i = 1; i <= t; i++)
	{
		out << "Case #" << i << ": ";
		function();
	}

	cout << out.str();

	return 0;
}