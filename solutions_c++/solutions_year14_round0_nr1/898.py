#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <algorithm>
#include <vector>

using namespace std;

void convert(vector<int> & v, string const & s)
{
	stringstream ss(s);
	for (int i = 0; i < 4; ++i)
		ss >> v[i];
}

string intersect(vector <int> & v1, std::vector<int> & v2)
{
	sort(v1.begin(), v1.end());
	sort(v2.begin(), v2.end());
	int it1 = 0, it2 = 0;
	int res = -1;
	int num = 0;
	while(it1 != v1.size(), it2 != v2.size())
	{
		if (v1[it1] == v2[it2])
		{
			++num;
			res = v1[it1];
			++it1;
			++it2;
		}
		else if (v1[it1] < v2[it2])
			++it1;
		else
			++it2;
	}

	if (num == 1)
	{
		stringstream s;
		s << res;
		return s.str();
	}
	else if (num == 0)
		return "Volunteer cheated!";
	else
		return "Bad magician!";
}

int main()
{
	fstream file("A-small-attempt0.in");
	fstream output("output.txt");
	std::string s;
	std::getline(file, s);
	int n = atoi(s.c_str());
	for (int i = 0; i < n; ++i)
	{
		std::getline(file, s);
		int num1 = atoi(s.c_str());
		vector <int> v1(4);
		for (int j = 0; j < 4; ++j)
		{
			std::getline(file, s);
			if (j + 1 == num1)
				convert(v1, s);
		}

		std::getline(file, s);
		int num2 = atoi(s.c_str());
		vector <int> v2(4);
		for (int j = 0; j < 4; ++j)
		{
			std::getline(file, s);
			if (j + 1 == num2)
				convert(v2, s);
		}
		output << "Case #" << i+1 << ": " << intersect(v1, v2) << endl;
	}
	file.close();
	output.close();
}