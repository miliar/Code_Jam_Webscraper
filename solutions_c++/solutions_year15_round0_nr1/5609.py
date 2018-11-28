#include <iostream>
#include <typeinfo>
#include <fstream>
#include <functional>
#include <utility>
#include <vector>
#include <atomic>
#include <string>

using namespace std;

int getAdditionalPersons(int sz, const char *initialSet)
{
	int add = 0,
		standed = 0;

	for (int i = 0; i < sz; ++i)
	{
		int count = initialSet[i] - '0';

		if (count > 0)
		{
			int total = standed + add;
			if (i > total)
				add += i - total;

			standed += count;	
		}
	}

	return add;
}


int main()
{
	ifstream file("D:\\A-large.in");
	ofstream outF("D:\\out.txt");

	if (!file.is_open())
		cout << " Error open " << endl;

	int count;
	file >> count;

	for (int i = 0; i < count; ++i)
	{
		int len;
		file >> len;

		string str;
		file >> str;

		// cout << "process " << str.c_str() << endl;

		outF << "Case #" << i + 1 << ": " << getAdditionalPersons(len + 1, str.c_str()) << endl;
	}
	
	file.close();
	outF.close();
	

	return 0;
}