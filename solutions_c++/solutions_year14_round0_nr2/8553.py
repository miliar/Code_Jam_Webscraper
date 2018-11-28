#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
	int T;
	//ifstream fin("B-small-attempt0.in");
	//ofstream fout("B-small-attempt0.out");
	ifstream fin("B-large.in");
	ofstream fout("B-large.out");
	fin >> T;
	for (int t = 0; t < T; ++t)
	{
		long double C, F, X;
		vector<long double> vec;
		fin >> C >> F >> X;
		for (int i = 0; i < (int)(X / C)+1; ++i)
		{
			long double sum = 0.0;
			long double tmpC = 2.0;
			for (int j = 0; j < i; ++j)
			{
				sum += C / tmpC;
				tmpC += F;
			}
			vec.push_back(sum + X / tmpC);
		}
		fout.precision(7);
		//cout.precision(7);
		cout << "Case #" << t + 1 << ": " << fixed << *min_element(vec.begin(), vec.end()) << endl;
		fout << "Case #" << t + 1 << ": " << fixed << *min_element(vec.begin(), vec.end()) << endl;
		//for (vector<long double>::iterator it = vec.begin(); it != vec.end(); ++it)
		//	cout << *it << " ";
		//cout << 
		//cout << endl;
	}
}