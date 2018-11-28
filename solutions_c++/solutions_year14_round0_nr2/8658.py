#include <fstream>
#include <string>
#include <vector>
#include <set>
#include <queue>
#include <algorithm>
#include <iostream>
#include <iomanip>
#include <cstdlib>



using namespace std;


int commonCard(vector<int> &v, set<int> &s, int &ans)
{
	int count = 0;
	for (unsigned int i = 0; i < v.size(); i++)
	{
		if (s.find(v[i]) != s.end()) {
			count++;
			ans = v[i];
		}
	}
	return count;
}

int main()
{

	int T;

	ifstream fin("C:\\weilin\\Competition\\GCJ2014Qualification\\GCJ2014Qualification\\B-large (1).in");
	ofstream fout("output.txt");

	fin >> T;

	long long total = 0;


	for (int i = 0; i < T; i++)
	{
		double C, F, X;
		fin >> C >> F >> X;
		 
		double base = 2.0;

		double numF = 0.0;

		double min = X / 2.0;
		double tf = 0.0;
		while (numF < X)
		{
			tf = tf + C / base;
			numF = numF++;
			base = 2.0 + numF * F;
			double newMin = tf + X / base;
			if (newMin < min)
				min = newMin;
		}
		
		
		fout << "Case #" << i + 1 << ": " << std::setprecision(7) << min << endl;
		

	}
	return 0;
}