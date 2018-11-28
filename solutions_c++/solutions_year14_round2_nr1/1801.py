// Codejam2014_1A.cpp : Defines the entry point for the console application.
//



#include "vector"
#include "string"
#include "set"
#include "map"
#include "sstream"
#include "algorithm"
#include "cmath"
#include "cassert"
#include "iostream"
#include "numeric"
#include "fstream"
#ifdef __GNUC__
#include  <tr1/unordered_map>
#define unordered_map tr1::unordered_map
#else
#include <unordered_map>
#endif

using namespace std;

#define int64 long long
#define F(vec, index) for (int index = 0; index  < vec.size(); ++index)
#define F_S(vec, index, start) for (int index = start; index  < vec.size(); ++index)






int main(int argc, char* argv[])
{
	ifstream cin("in.txt");
	ofstream cout("out.txt");

	int T;
	cin >> T;
	for (int t = 0; t < T; ++t)
	{
		int N;
		cin >> N;
		vector<string> data(N);

		for (int i = 0; i < N; ++i)
			cin >> data[i];

		vector<int> globalCount(N, 0);
		vector<int> count;
		bool notPoss = false;
		int res = 0;
		for (int i = 0; i < data[0].size(); ++i)
		{
			count.clear();
			count.resize(N, 0);
			char first = data[0][i];

			for (int j = 0; j < data.size(); ++j)
			{
				int k = globalCount[j];
				while (first == data[j][k])
				{
					k++;
					count[j]++;
					globalCount[j]++;
				}
			}
			i = globalCount[0] - 1;
			int average = 0;
			
			F(count, j)
			{
				if (count[j] == 0)
				{
					notPoss = true;
					break;
				}
				average += count[j];
			}
			if (notPoss) break;
			average = average / (double)data.size() + 0.5;

			F(count, j)
			{
				res += abs(average - count[j]);
			}

		}
		F(globalCount, j)
		{
			if (globalCount[j] != data[j].size())
				notPoss = true;
		}
		if (notPoss) 
		{
			cout << "Case #" << t + 1 << ": "  << "Fegla Won" << endl;
		}
		else
		{
			cout << "Case #" << t + 1 << ": "  << res << endl;
		}
		
	}

	return 0;
}
