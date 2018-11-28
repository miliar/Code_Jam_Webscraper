#include <iostream>
#include <fstream>
#include <bitset>

typedef unsigned int uint;
typedef std::bitset<10> digits;

void checkDigits(uint n, digits & was)
{
	if (0 == n)
		was.set(0);
	while (n > 0)
	{
		was.set(n % 10);
		n /= 10;
	}
}

int main()
{
	using namespace std;

	ifstream in("a.in");
	ofstream out("a.out");

	uint T;
	in >> T;

	cout << T << endl;
	
	for (uint i = 0; i < T; ++i)
	{
		out << "Case #" << (i + 1) << ": ";

		uint N;
		in >> N;
		
		if (0 == N)
		{
			out << "INSOMNIA" << endl;
			continue;
		}

		uint j = N;
		for (digits was; !was.all(); j += N)
			checkDigits(j, was);
		out << (j - N) << endl;
	}
	return 0;
}
