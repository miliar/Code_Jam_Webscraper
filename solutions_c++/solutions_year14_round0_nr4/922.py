#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <algorithm>
#include <vector>
#include <deque>

using namespace std;

void doit(vector <double> & v1, vector <double> & v2, int & f)
{
	int itBeg1 = 0;
	int itEnd1 = v1.size() - 1, itEnd2 = v1.size() - 1;
	f = 0;
	while (itBeg1 <= itEnd1)
	{
		if (v1[itEnd1] > v2[itEnd2])
		{
			++f;
			--itEnd1;
			--itEnd2;
		}
		else
		{
			++itBeg1;
			--itEnd2;
		}
	}
}

void dosimple(vector <double> & v1, vector <double> & v2, int & s)
{
	s = 0;
	for (int i = 0; i < v1.size(); ++i)
	{
		bool f = false;
		for (size_t j = 0; j < v2.size(); ++j)
		{
			if (v2[j] > v1[i])
			{
				f = true;
				v2[j] = -1;
				break;
			}
		}
		if (!f)
		{
			++s;
			for (size_t j = 0; j < v2.size(); ++j)
			{
				if (v2[i] != -1)
				{
					v2 [i] = -1;
					break;
				}
			}
		}
	}

}

int doit(vector <double> & v1, vector <double> & v2, int & f, int & s)
{
	sort(v1.begin(), v1.end());
	sort(v2.begin(), v2.end());
	doit(v1, v2, f);
	dosimple(v1, v2, s);
}

int main()
{
	fstream file("D-large.in");
	fstream output("out.txt");
	std::string s;
	std::getline(file, s);
	int n = atoi(s.c_str());
	for (int i = 0; i < n; ++i)
	{
		int k;
		file >> k;
		vector <double> v1(k), v2(k);
		for (size_t j = 0; j < k; ++j)
			file >> v1[j];
		for (size_t j = 0; j < k; ++j)
			file >> v2[j];
		int f, s;
		doit(v1, v2, f, s);
		output << "Case #" << i+1 << ": " << f << " " << s << endl;

	}
	file.close();
	output.close();
	return 0;
}