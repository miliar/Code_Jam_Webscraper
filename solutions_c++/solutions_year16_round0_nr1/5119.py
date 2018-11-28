#include <iostream>
#include <vector>
#include <sstream>
#include <stdlib.h>

using namespace std;

vector<int> digits;

void inDigit(int n)
{
	string v;
	stringstream out;
	out << n;
	v = out.str();
	for (int i=0; i<v.length(); i++)
	{
		int b = 0;
		for (int o=0; o<digits.size(); o++)
		{
			if (digits.at(o) == v[i])
			{
				b = 1;
				break;
			}
		}

		if (b == 0)
			digits.push_back(v[i]);
	}
}

int main() {
	
	string line;
	long nVal = 0;

	getline(cin, line);

	int nCase = 1;

	while(getline(cin, line))
	{
		int mul = 1;
		nVal = atoi(line.c_str());
		digits.clear();

		cout << "Case #" << nCase << ": ";
		if (nVal == 0)
		{
			cout <<  "INSOMNIA";
		}
		else
		{
			int ans = 0;
			while(digits.size() < 10)
			{
				ans = mul*nVal;
				inDigit(ans);
				mul++;
			}

			cout << ans;
		}

		cout << endl;

		nCase++;
	}

	return 0;
}