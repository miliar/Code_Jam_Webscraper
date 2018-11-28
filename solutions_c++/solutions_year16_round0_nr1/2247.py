#include <iostream>
#include <sstream>

using namespace std;

stringstream out;

bool isComplete(bool *digits)
{
	for (int i = 0; i < 10; i++)
		if (!digits[i])
			return false;
	return true;
}

void function()
{
	long long n;
	cin >> n;
	bool digits[10];
	if (n == 0) {
		out << "INSOMNIA\n";
		return;
	}
	for (int i = 0; i < 10; i++)
		digits[i] = false;
	long long currentNumber = n;

	int mult = 0;
	while (!isComplete(digits))
	{
		mult++;
		currentNumber = n * mult;
		while (currentNumber > 0)
		{
			digits[currentNumber % 10] = true;
			currentNumber /= 10;
		}
	}

	out << n * mult << endl;
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