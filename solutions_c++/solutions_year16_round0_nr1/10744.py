#include <iostream>
#include <string>
#include <bitset>
#include <vector>
#include <fstream>

using namespace std;


int doTestA(int num)
{
	string s = "";
	bool found[10] = { false };
	int c = 1;
	int totalFound = 0;

	if (num == 0)
	{
		return 0;
	}

	while (true)
	{
		s = std::to_string(num * c);

		for (int i = 0; i < s.length(); i++)
		{
			int current = s[i] - 48;

			if (!found[current])
			{
				totalFound++;

				if (totalFound == 10)
				{
					return num * c;
				}

				found[current] = true;
			}
		}

		c++;
	}
}


int main()
{
	string line;
	ifstream f("C:\\Users\\nick\\Documents\\Visual Studio 2015\\Projects\\google\\input.txt");

	if (f.is_open())
	{
		if (getline(f, line))
		{
			int numTests = atoi(line.c_str());

			for (int i = 0; i < numTests; i++)
			{
				if (getline(f, line))
				{
					int num = doTestA(std::atoi(line.c_str()));
					
					if (num == 0)
					{
						cout << "Case #" << (i + 1) << ": INSOMNIA\n";
					}
					else
					{
						cout << "Case #" << (i + 1) << ": " << num << "\n";
					}
					
				}
			}
		}

		f.close();
	}

	cin.get();
	return 0;
}
