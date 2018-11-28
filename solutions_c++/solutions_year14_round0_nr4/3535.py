#include <iostream>
#include <vector>
#include <algorithm>
#include <fstream>

using namespace std;

int CalculateWar(vector<double> &pn, vector<double> &pk){
	vector<double> n(pn);
	vector<double> k(pk);

	int point = 0;

	while (n.size() > 0)
	{
		double nn = *(n.end() - 1);
		n.erase(n.end() - 1);

		bool found = false;
		for (int j = 0; j < k.size(); j++)
		{
			if (k[j] > nn)
			{
				found = true;
				k.erase(k.begin() + j);
				break;
			}
		}

		if (!found)
		{
			k.erase(k.begin());
			point++;
		}
	}

	return point;
}

int CalculateDecitfulWar(vector<double> &pn, vector<double> &pk){
	vector<double> n(pn);
	vector<double> k(pk);

	int point = 0;

	while (n.size() > 0)
	{
		double nn = *(n.end() - 1);

		bool found = false;
		for (int j = 0; j < k.size(); j++)
		{
			if (k[j] > nn)
			{
				found = true;
				k.erase(k.begin() + j);
				n.erase(n.begin());
				break;
			}
		}

		if (!found)
		{
			double kk = *(k.begin());
			k.erase(k.begin());
			for (int i = 0; i < n.size(); i++)
			{
				if (n[i] > kk)
				{
					n.erase(n.begin() + i);
					break;
				}
			}

			point++;
		}
	}

	return point;
}

int main(void)
{
	ifstream input;
	ofstream output;
	input.open("input.txt");
	output.open("output.txt");

	vector<double> n;
	vector<double> k;

	int testCases;

	input >> testCases;

	for (int testCase = 1; testCase <= testCases; testCase++)
	{
		int s;

		input >> s;

		n.clear();
		k.clear();

		for (int i = 0; i < s; i++)
		{
			double temp;
			input >> temp;
			n.push_back(temp);
		}

		for (int i = 0; i < s; i++)
		{
			double temp;
			input >> temp;
			k.push_back(temp);
		}

		sort(n.begin(), n.end());
		sort(k.begin(), k.end());

		output << "Case #" << testCase << ": " << CalculateDecitfulWar(n, k) << " " << CalculateWar(n, k) << endl;
	}

	return 0;
}