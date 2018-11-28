// Codejam2014_1C.cpp : Defines the entry point for the console application.
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
		
		int res = 0;
		int N, X;
		cin >> N >> X;

		vector<int> data(N, 0);
		vector<bool> selected(N, false);

		for (int i = 0; i < data.size(); ++i)
		{
			cin >> data[i];
		}

		sort(data.rbegin(), data.rend());

		for (int i = 0; i < data.size(); ++i)
		{
			if (selected[i]) continue;
			int remain =  X - data[i];
			selected[i] = true;
			res++;
			int last = -1;
			for (int j = data.size() - 1; j >= 0; --j)
			{
				if (selected[j]) continue;

				
				if (data[j] - remain == 0)
				{
					last = j;
					//selected[j] = true;
					//res++;
					break;
				}
				if (remain - data[j] < 0)
				{		
					break;
				}
				last = j;
				
			}
			if (last != -1)
				selected[last] = true;
		}

		
		cout << "Case #" << t + 1 << ": "  << res << endl;
		
		
	}

	return 0;
}
