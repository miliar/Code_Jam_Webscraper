#include <iostream>
#include <map>
#include <sstream>

using namespace std;

map<unsigned long, unsigned long> fs;
map<unsigned long, unsigned long> rfs;

bool isPal(unsigned long n)
{
	stringstream ss;
	ss << n;
	string str = ss.str();

	for (int i = 0; i < str.size() / 2; ++i)
	{
		if (str[i] != str[str.size() - i - 1])
			return false;
	}

	return true;
}

int main()
{
	for (int i = 1; i <= 1000; ++i)
	{
		unsigned long temp = i * i;
		fs[i] = temp;
		rfs[temp] = i;
	}

	int T = 0;
	
	cin >> T;
	
	for (int i = 0; i < T; ++i)
	{
		int A, B;

		cin >> A >> B;
		unsigned long count = 0;
		map<unsigned long, unsigned long>::iterator it;

		for (int j = A; j <= B; ++j)
		{
			it = rfs.find(j);
			if (it == rfs.end())
				continue;

			if (isPal(j) && isPal(rfs[j]))
				count++;
		}

		cout << "Case #" << i + 1 << ": " << count << endl;
	}

	return 0;
}