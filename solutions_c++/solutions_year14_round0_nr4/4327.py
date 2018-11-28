#include <iostream>
#include <fstream>
#include <algorithm>
#include <iomanip>
#include <vector>
#include <string>
#include <queue>

using namespace std;

int deceitfulWar(vector<double> &v1, vector<double> &v2)
{
	const int n = v1.size();
	int i = 0;
	int count = 0;
	for (; i < n; i++)
	{
		bool flag = false;
		for (int j = i; j < n; j++)
		{
			if (v1[j] < v2[j - i])
			{
				flag = true;
				break;
			}
		}
		if (!flag)
			break;
		if (v1[i] < v2[n - i - 1])
			count++;
	}
	return n - i;
}

int war(vector<double> &v1, vector<double> &v2)
{
	const int n = v1.size();
	for (int i = 0; i < n; i++)
	{
		double cur = v1[i];
		int j = 0;
		for (; j < v2.size(); j++)
		{
			if (v2[j] > cur)
				break;
		}
		if (j == v2.size())
			break;
		v2.erase(v2.begin() + j);
	}
	return v2.size();
}

int main()
{
	ifstream in("D-large.in");
	ofstream out("D-large.out");
	int T;
	in >> T;
	int N;
	for (int k = 0; k < T; k++)
	{
		in >> N;
		vector<double> v1, v2;
		for (int i = 0; i < N; i++)
		{
			double temp;
			in >> temp;
			v1.push_back(temp);
		}
		for (int i = 0; i < N; i++)
		{
			double temp;
			in >> temp;
			v2.push_back(temp);
		}
		sort(v1.begin(), v1.end());
		sort(v2.begin(), v2.end());
		int result = deceitfulWar(v1, v2);
		int result2 = war(v1, v2);
		out << "Case #" << k + 1 << ": " << result << ' ' << result2 << endl;
	}
	system("PAUSE");
	return 0;
}